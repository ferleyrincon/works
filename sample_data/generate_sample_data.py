"""
Generate the SYNTHETIC sample data in this folder by running the oTree bots.

Run from the repository root (same environment as `otree test`):

    python sample_data/generate_sample_data.py

It creates a throw-away SQLite database in a temporary folder (it never touches db.sqlite3),
plays one 'questions' session with N bot participants (iat/tests.py and survey/tests.py)
and writes:

    sample_data/all_apps_wide.csv   one row per participant (oTree wide export)
    sample_data/iat.csv             one row per participant and IAT block (oTree app export)
    sample_data/survey.csv          one row per participant (oTree app export)
    sample_data/iat_trials.csv      one row per IAT trial (custom export of the Trial model)

All values are random bot answers. No participant data are produced or included.
"""

import os
import random
import sys
import tempfile
from pathlib import Path

N_PARTICIPANTS = 6
SEED = 2022

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))

tmp_db = Path(tempfile.mkdtemp()) / 'synthetic.sqlite3'
os.environ['DATABASE_URL'] = 'sqlite:///' + tmp_db.as_posix()
random.seed(SEED)

from otreeutils import scripts  # noqa: E402,F401  (configures oTree/Django)
from otree.common import patch_migrations_module  # noqa: E402
from django.core.management import call_command  # noqa: E402

patch_migrations_module()
call_command('migrate', interactive=False, run_syncdb=True, verbosity=0)

import otree.export  # noqa: E402
import otree.session  # noqa: E402
from otree.bots.runner import run_bots  # noqa: E402

session = otree.session.create_session(session_config_name='questions', num_participants=N_PARTICIPANTS)
run_bots(session)

exports = [
    ('all_apps_wide.csv', lambda fp: otree.export.export_wide(fp)),
    ('iat.csv', lambda fp: otree.export.export_app('iat', fp)),
    ('survey.csv', lambda fp: otree.export.export_app('survey', fp)),
    ('iat_trials.csv', lambda fp: otree.export.custom_export_app('iat', fp)),
]
for name, fn in exports:
    with open(OUT / name, 'w', encoding='utf8', newline='') as fp:
        fn(fp)
    print('wrote', OUT / name)
