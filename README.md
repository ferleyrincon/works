# IAT Sexo-STEM: gender–STEM Implicit Association Test and survey (oTree 3)

Replication package for the software used in a field study with eleventh-grade students at a public technical high school in Chía, Colombia (26–29 September 2022). Each participant took a 7-block gender–STEM Implicit Association Test (IAT) and then a 14-page survey on career aspirations and beliefs about STEM.

This repository contains exactly the version used in the field (v3), so the experiment can be run again as it was run then. It contains no participant data.

The study builds on the master's thesis by Medrano León and Carrillo Cadena (2023), *Modelos a seguir y aspiraciones educativas de las adolescentes por áreas STEM*, Escuela de Gobierno Alberto Lleras Camargo, Universidad de los Andes. Maintainer: Ferley Rincón ([@ferleyrincon](https://github.com/ferleyrincon)).

## Requirements

- Python **3.8** (tested with 3.8.20 on Windows 11). oTree 3.3.11 does not support newer Python versions.
- The packages in `requirements.txt`, all pinned. The key ones are `otree==3.3.11` (the version used in the field), `otreeutils==0.10.0` and `pandas==1.3.5`.
- A desktop browser and a physical keyboard. The IAT is answered with the **E** and **I** keys.

## Install and run

```bash
git clone https://github.com/ferleyrincon/works.git
cd works
python3.8 -m venv venv              # Windows: py -3.8 -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt

otree test questions                # bots: full IAT (7 blocks) + full survey
otree devserver                     # then open http://localhost:8000
```

Keep the virtual environment activated: `otree devserver` launches `otree` from your `PATH`, so a different global oTree installation would be picked up otherwise.

In the admin interface, open **Demo → questions** (or create a session named `questions`) and follow a participant link. That is the only session, and it is the one used in the field: `app_sequence = ['iat', 'survey']`, with no payment (`participation_fee = 0`, `USE_POINTS = True`, currency COP), Spanish locale and `TIME_ZONE = 'UTC'`.

For a server deployment, set `OTREE_PRODUCTION=1`, `OTREE_ADMIN_PASSWORD` and a `DATABASE_URL`. PostgreSQL also needs `pip install psycopg2==2.8.6`, the version used in 2022. Run `otree resetdb` once and then `otree prodserver`. The field version ran on Heroku, but no Heroku-specific files are kept.

## Structure and page order

```
settings.py          session config (single session 'questions')
iat/                 IAT app (7 rounds = 7 blocks)
  models.py          stimuli, block definitions, Player fields, Trial model (one row per trial)
  pages.py           welcome -> Intro -> IATPage (x7) -> Outro
  templates/, static/  page templates, iat.css, category images
  tests.py           bot for the 7 blocks
  urls.py            otreeutils admin views (trial data view and export)
survey/              survey app (1 round, 14 pages)
  models.py, pages.py, templates/, static/, tests.py
_templates/, _static/  global oTree base template and static folder
data_exporter.py     exports all IAT data (including trials) to JSON
```

**IAT (`iat`).** `welcome` asks for the participant code (`identificador`) and the group printed on the participant's sheet (`treatment`: 0 = C, 1 = T). `Intro` shows the instructions and stimuli. Then come seven `IATPage` rounds, followed by `Outro`. Stimuli are words in Spanish, and category labels are shown with images. Response keys are E (left) and I (right), with a 250 ms delay between trials.

| Block | Label | Trials | Left (E) | Right (I) |
|---|---|---|---|---|
| 1 | Practica 1 | 10 | Letras (No STEM) | Números (STEM) |
| 2 | Practica 2 | 10 | Hombre | Mujer |
| 3 | Prueba 1 | 20 | Hombre + Letras | Mujer + Números |
| 4 | Prueba 2 | 20 | Hombre + Letras | Mujer + Números |
| 5 | Practica 3 (invertida) | 10 | Números (STEM) | Letras (No STEM) |
| 6 | Prueba 3 | 20 | Hombre + Números | Mujer + Letras |
| 7 | Prueba 4 | 20 | Hombre + Números | Mujer + Letras |

The block order is fixed (not counterbalanced), and trial order is randomized within each block. Stimuli, labels and blocks are defined in `iat/models.py` (`STIMULI`, `STIMULI_LABELS`, `IMAGES`, `BLOCKS`).

**Survey (`survey`), 14 pages in this order:** `beliefs`, `efficacy`, `group`, `saber11`, `explicit`, `subjects`, `occupation`, `occupation2`, `careers`, `education`, `time`, `questions1`, `questions2`, `thanks`.

## Data produced and export

- **Player level** (one row per participant): IAT `identificador` and `treatment` and all survey answers. Download from the admin **Data** page (`/export`) using the standard oTree CSV/Excel exports ("All apps" or per app).
- **Trial level** (one row per IAT trial, 110 per participant): `block`, `trial`, `stimulus`, `stimulus_class`, `stimulus_level`, `response_key`, `response_correct`, `response_time_ms`, linked to the participant. These are the inputs for the IAT *D* score (critical blocks 3–4 vs. 6–7). They are exported in two ways:
  - from the admin interface: the custom export of app `iat` on the Data page, plus a live view of the trials provided by otreeutils;
  - from the command line: `python data_exporter.py iat_data.json` writes all sessions, participants, players and trials as hierarchical JSON. It reads the database, so stop `otree devserver` first, because the devserver writes `db.sqlite3` when it stops. On a production server it reads `DATABASE_URL`.

The custom export covers all sessions in the database. Use `session.code` and `participant.code` to link trials to the player-level data.

Participant data are not part of this repository, and `.gitignore` excludes the database and exported `.json`/`.csv` files.

## How to cite

Please cite this repository (see also `CITATION.cff`):

> Medrano León, E. C., Carrillo Cadena, R. A., & Rincón, F. (2026). *IAT Sexo-STEM: oTree implementation of a gender–STEM Implicit Association Test and survey (field version, Chía, Colombia, 2022)* (Version 3.0.0) [Computer software]. https://github.com/ferleyrincon/works. DOI: 10.5281/zenodo.XXXXXXX (placeholder)

## Credits and license

The `iat` app is adapted from **[otree_iat](https://github.com/WZBSocialScienceCenter/otree_iat)** by Markus Konrad (WZB Berlin Social Science Center), with contributions by Christoph Semken. It is licensed under the Apache License 2.0 (see `LICENSE`). Its full technical documentation is in the original repository.

**Modifications (Apache-2.0, section 4b):** this repository changes the original files. In 2022 the study team replaced the stimuli with Spanish gender–STEM words and images, redefined the blocks, added the `welcome` page and Player fields, adapted the IAT templates, and added the `survey` app and the field session in `settings.py`. In 2026 the IAT bot was updated for the `welcome` page, a survey bot was added, and files not needed for replication (Heroku files, rooms, unused static files) were removed. Modified files carry a notice in their header.

The commit history is kept as it was. Commits from 17 November 2022 accidentally deleted the apps, and they were restored on 22 November 2026 (commit `cab2035`) to the field version of 26 September 2022 (commit `96200d6`).
