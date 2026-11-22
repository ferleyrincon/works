# AGENTS.md

Instructions for AI agents (and humans) working on this repository. Every statement below can be checked against the files named.

## 1. Purpose

- This repository is the oTree code of one field experiment: a 7-block gender–STEM IAT followed by a 14-page survey, run with 210 eleventh graders in Chía, Colombia, on 26–29 September 2022 (see `README.md`).
- Its job is to let others **replicate the field version exactly** or **adapt it** to a new study.
- It contains no participant data. Do not add real data, exports, databases or credentials; `sample_data/` holds synthetic bot output only.
- One session config exists: `questions` (`app_sequence = ['iat', 'survey']`). The treatment arm is not assigned by oTree; participants enter it on the welcome page (`iat.Player.treatment`, 0 = C, 1 = T).

## 2. File map

| File | Controls |
|---|---|
| `settings.py` | `SESSION_CONFIGS` (only `questions`), `LANGUAGE_CODE = 'es'`, `REAL_WORLD_CURRENCY_CODE = 'COP'`, `USE_POINTS`, admin password from `OTREE_ADMIN_PASSWORD`, `otreeutils` loading |
| `iat/models.py` | `STIMULI` (5 words per category), `STIMULI_LABELS` (category names shown), `IMAGES` (image per category), `BLOCKS` (7 blocks: label, `n`, left/right categories, notice), `Constants.capture_keycodes` (E = left, I = right), `Constants.next_trial_delay_ms` (250), `Player.identificador`, `Player.treatment`, the `Trial` model (one row per trial, incl. `response_time_ms`) |
| `iat/pages.py` | `page_sequence = [welcome, Intro, IATPage, Outro]`; storage of submitted trials in `IATPage.before_next_page` |
| `iat/templates/iat/*.html` | All IAT texts in Spanish (`welcome.html`, `Intro.html`, `IATPage.html` incl. the trial JavaScript, `Outro.html`) |
| `iat/static/images/` | `mujer.png`, `hombre.png`, `numeros.png`, `a-b-c.png` (referenced by `IMAGES`) |
| `iat/static/css/iat.css` | Layout of the IAT page |
| `iat/tests.py` | IAT bot: checks trials per block and stored responses |
| `iat/urls.py`, `data_exporter.py` | `otreeutils` admin views and trial export; JSON export of all data |
| `survey/models.py` | All survey fields with their Spanish labels and choices |
| `survey/pages.py` | `page_sequence` of 14 pages: beliefs, efficacy, group, saber11, explicit, subjects, occupation, occupation2, careers, education, time, questions1, questions2, thanks |
| `survey/templates/survey/*.html`, `survey/static/` | Survey texts in Spanish, sliders and JavaScript checks |
| `survey/tests.py` | Survey bot: random valid answers on every page |
| `_templates/global/Page.html`, `_static/global/empty.css` | oTree base template; `_static/` must exist because oTree adds it to `STATICFILES_DIRS` |
| `docs/` | Screens participants saw, survey page list, variable dictionary |
| `sample_data/` | Synthetic CSVs and `generate_sample_data.py` |
| `requirements.txt` | Exact versions (oTree 3.3.11, Python 3.8) |

## 3. What to adapt

Changes made in this repository relative to WZB's [otree_iat](https://github.com/WZBSocialScienceCenter/otree_iat) (diff against its `master`, commit `7790683`), and what someone adapting the study must change:

| File | What we changed relative to WZB | What an adapter must change |
|---|---|---|
| `iat/models.py` | Stimuli `pos/neg` and `canidae/felidae` → `woman/man` and `stem/no_stem` (Spanish words); labels in Spanish; new `IMAGES` dict; block labels and block-5 notice in Spanish; new fields `identificador`, `treatment` and `Subsession.set_id_players`; hard import of `otreeutils.admin_extensions.custom_export` | `STIMULI`, `STIMULI_LABELS`, `IMAGES` and the `left`/`right` categories in `BLOCKS`; keep `n` equal to the number of stimuli in the block (see warning) |
| `iat/pages.py` | New `welcome` page (round 1); `IATPage.vars_for_template` adds images and a centre column | Remove or edit `welcome` if participants do not type a code or group |
| `iat/templates/iat/IATPage.html` | Spanish texts; three-column layout with images and centre stimulus; CSS moved to `iat/static/css/iat.css` | Instruction texts |
| `iat/templates/iat/Intro.html`, `Outro.html`, new `welcome.html` | Spanish texts, STEM note | Texts |
| `iat/static/` (new) | Category images and `iat.css` | Images named in `IMAGES` |
| `iat/tests.py` | Bot submits the welcome page first | Must match any change to pages or fields |
| `survey/` (new app) | 14-page Spanish survey and its bot | Replace or remove; update `app_sequence` |
| `settings.py` | Session `iat` (4 demo participants) → `questions` (`iat` + `survey`); `LANGUAGE_CODE` `en` → `es`; currency `USD` → `COP`; removed `BROWSER_COMMAND`, `ROOMS`, `ROOM_DEFAULTS` | Session name and `app_sequence`, language, currency |
| `requirements.txt` | `otree>=3.3.0,<4` → exact pins (oTree 3.3.11, otreeutils 0.10.0, pandas 1.3.5, Django 2.2.12, …) | Keep the pins unless you re-test everything |
| Removed from WZB | `Procfile`, `tox.ini`, `manage.py`, `_doc_imgs/`, WZB `README.md` (linked instead) | — |

Unchanged from WZB: `data_exporter.py`, `iat/urls.py`, `iat/templates/iat/Page.html`, `_templates/global/Page.html`, `_static/global/empty.css`, the 7-block structure and trial counts, keys E/I, the 250 ms delay and the trial JavaScript logic.

**Warning:** in `iat/models.py`, `Subsession.creating_session` raises `ValueError` when the number of stimuli on both sides of a block differs from that block's `n`. With 5 words per category, a block with one category per side needs `n = 10` and a combined block needs `n = 20`.

After any change: update `iat/tests.py` and `survey/tests.py` if pages or fields changed, then run `otree test questions 10` (rename the session in the command if you renamed it).

## 4. Do not change if you want to replicate the field version

- The order and content of the 7 blocks in `BLOCKS` (compatible pairing *Hombre+Letras / Mujer+Números* in blocks 3–4, then *Hombre+Números / Mujer+Letras* in blocks 6–7; not counterbalanced).
- `STIMULI`, `STIMULI_LABELS`, `IMAGES` and the images in `iat/static/images/`.
- Keys E (left) and I (right) in `Constants.capture_keycodes`, and `next_trial_delay_ms = 250`.
- The Spanish texts in the templates and the survey `page_sequence` and fields.
- The versions in `requirements.txt` (oTree 3.3.11 on Python 3.8).

## 5. Mandatory check before any commit

```bash
pip install -r requirements.txt     # Python 3.8
otree test questions 10
```

The run must end with `Bots completed session` and no traceback. Also confirm that `git status` shows no `db.sqlite3`, `*.csv` outside `sample_data/`, `*.json` or `.env` files.
