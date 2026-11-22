# oTree settings for the gender-STEM IAT field study (Chia, Colombia, 26-29 September 2022).
# Modified from the settings of Markus Konrad's otree_iat (Apache-2.0): the field
# session ('questions' = IAT + survey), Spanish locale and COP currency were added;
# Heroku rooms, test sessions and BROWSER_COMMAND were removed in 2026 for the replication package.

from os import environ
import importlib.util


if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
    APPS_DEBUG = False
else:
    DEBUG = True
    APPS_DEBUG = True   # also enables random fill in of forms


SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

# The only session used in the field: the 7-block IAT followed by the 14-page survey.
SESSION_CONFIGS = [
    dict(
        name='questions',
        display_name="IAT Sexo-STEM + encuesta (version de campo)",
        num_demo_participants=1,
        app_sequence=['iat', 'survey'],
    ),
]

# ISO-639 code
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'

REAL_WORLD_CURRENCY_CODE = 'COP'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, set the admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '<SET_KEY_HERE>'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# otreeutils (with pandas) adds the per-trial data view and the IAT trial export
if importlib.util.find_spec('otreeutils'):
    INSTALLED_APPS.append('otreeutils')

    if importlib.util.find_spec('pandas'):
        ROOT_URLCONF = 'iat.urls'
