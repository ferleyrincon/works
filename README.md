# IAT Sexo-STEM: oTree code for a gender–STEM Implicit Association Test and survey

Replication code for the field experiment analyzed in the working paper:

> Medrano León, E. C., Carrillo Cadena, R. A., & Rincón, F. (2026). *One Talk Shifts Beliefs About Science Jobs but Not Detectably Gender Beliefs: A Randomized Role-Model Visit in a Colombian Technical High School.* Working paper, version 1.5 (draft, not yet publicly circulated; authorship to be confirmed).

The experiment was first reported in the master's thesis of E. C. Medrano León and R. A. Carrillo Cadena (Escuela de Gobierno Alberto Lleras Camargo, Universidad de los Andes, 2023).

This repository contains only the code that participants used. **It does not contain participant data**, and real data must never be added to it. `sample_data/` holds synthetic output produced by the bots.

## 1. The experiment

- **Population:** 210 eleventh-grade students (115 girls) from the six eleventh-grade classrooms of a public technical high school.
- **Place:** Chía (Cundinamarca), Colombia, in the school's computer room.
- **Field dates:** 26–29 September 2022. The code deployed in the field is commit `96200d6` (26 September 2022), restored in this repository in commit `cab2035`.
- **What participants did in oTree:** a welcome page (participant code and assigned group), a 7-block Implicit Association Test (IAT) pairing *Hombre/Mujer* with *Números (STEM)/Letras (No STEM)*, and a 14-page survey on beliefs about science jobs, gender equality in aptitudes, self-concept, expected Saber 11 scores, occupational and career aspirations, risk and time preferences and household characteristics. All screens are in Spanish (see [`docs/`](docs/)).

## 2. Design

| Arm in the working paper | What happened | Session config | How the arm is recorded |
|---|---|---|---|
| Treatment (106 students) | 30-minute videoconference with a STEM professional, then oTree (IAT + survey) | `questions` | participant selects **T** on the welcome page → `iat.Player.treatment = 1` |
| Control (104 students) | oTree (IAT + survey) first, in another room; the talk afterwards | `questions` | participant selects **C** on the welcome page → `iat.Player.treatment = 0` |

**Random assignment happened outside oTree.** On the day of each session, the students of a classroom drew tokens of two colors, which assigned each of them individually to treatment or control (16 to 19 students per arm and classroom). Both arms ran the same session config; oTree does not randomize the arm. Within the IAT, the order of the stimuli inside each block is randomized by `iat/models.py` (`random.shuffle`), while the order of the 7 blocks is fixed (compatible pairing *Hombre+Letras / Mujer+Números* in blocks 3–4, then *Hombre+Números / Mujer+Letras* in blocks 6–7).

| Block | Label | Trials | Left key **E** | Right key **I** |
|---|---|---|---|---|
| 1 | Practica 1 | 10 | Letras (No STEM) | Números (STEM) |
| 2 | Practica 2 | 10 | Hombre | Mujer |
| 3 | Prueba 1 | 20 | Hombre + Letras | Mujer + Números |
| 4 | Prueba 2 | 20 | Hombre + Letras | Mujer + Números |
| 5 | Practica 3 (invertida) | 10 | Números (STEM) | Letras (No STEM) |
| 6 | Prueba 3 | 20 | Hombre + Números | Mujer + Letras |
| 7 | Prueba 4 | 20 | Hombre + Números | Mujer + Letras |

Note: the working paper describes students answering the survey and then the IAT; in this code the app sequence is `['iat', 'survey']`, because the welcome page that records the participant code and arm is the first page of the `iat` app. The code is reproduced as deployed.

## 3. Requirements and installation

- Python **3.8** (tested with 3.8.20). The field server used Python 3.7.9; Python 3.8 is required here by the pinned `numpy==1.24.4`. Python ≥ 3.9 is not supported by oTree 3.3.11.
- **oTree 3.3.11** (the version used in the field) and the other exact versions in [`requirements.txt`](requirements.txt).

```bash
python3.8 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 4. Running the experiment and the bots

```bash
otree devserver                   # then open http://localhost:8000 and start a demo of "questions"
otree test questions 10           # bots: 10 participants through the IAT and the 14 survey pages
```

`otree test` must finish with `Bots completed session` and no traceback. The bots are in `iat/tests.py` (they also check that every block has the right trials and that responses are stored) and `survey/tests.py` (random valid answers on every page).

`python sample_data/generate_sample_data.py` reruns the bots against a temporary database and rewrites the synthetic CSV files in `sample_data/`.

For a server deployment set `OTREE_PRODUCTION=1`, `OTREE_ADMIN_PASSWORD` and a `DATABASE_URL`, run `otree resetdb` once and then `otree prodserver`. PostgreSQL also needs `pip install psycopg2==2.8.6`, the driver used in 2022.

## 5. Data produced

| Table | Rows | Main variables |
|---|---|---|
| `iat` (oTree app export) | 7 per participant (one per block) | `player.identificador` (participant code typed by the student), `player.treatment` (0 = C, 1 = T, recorded in round 1) |
| `Trial` (custom model in `iat/models.py`) | 110 per participant (one per IAT trial) | `block` (1–7), `trial` (order within block), `stimulus`, `stimulus_class` (`attributes`/`concepts`), `stimulus_level` (`woman`, `man`, `stem`, `no_stem`), `response_key` (`KeyE`/`KeyI`, first key pressed), `response_correct` (whether the first key was correct), `response_time_ms` |
| `survey` (oTree app export) | 1 per participant | belief items `p_science1-5`, gender-aptitude items `p_gender1-5`, math self-concept `p_math1-4`, beliefs about science jobs `p_jobsci1-3`, liking `l_*` and perceived performance `p_*` by subject, expected Saber 11 scores, occupations `occupation_1-3`, career ratings `career1-20`, higher-education plans `educ_*`, risk and time `p_risk`, `p_time`, `p_time2`, background `p_sex`, `p_age`, … |

`response_time_ms` is measured in the browser from the moment the word appears until the first key press (`new Date().getTime()`), per trial. After an error the participant must press the correct key to continue; that second press is not recorded. Trials are separated by 250 ms. The full list of survey variables, with the labels participants saw, is in [`docs/diccionario_variables.md`](docs/diccionario_variables.md).

**Exporting the data**

- Standard tables: oTree admin → *Data* (all apps wide, per app, page times).
- Trials: with `otreeutils` installed (it is in `requirements.txt`), the admin *Data* page offers a custom export of `iat` with one row per trial, linked to the participant; the session monitor also shows the trials live.
- Everything as JSON: `python data_exporter.py iat_data.json` (reads the database configured for oTree; stop `otree devserver` first). Exported files (`*.csv`, `*.json`) are ignored by git, except the synthetic files in `sample_data/`.

## 6. Based on

The `iat` app is a modified copy of **[otree_iat](https://github.com/WZBSocialScienceCenter/otree_iat)** by Markus Konrad (WZB Berlin Social Science Center), with oTree 3.3 compatibility by Christoph Semken, licensed under Apache 2.0. What we changed:

- **Stimuli and labels:** the English example (positive/negative words; Canidae/Felidae) became Spanish gender–STEM categories, with an image for each category (`IMAGES`, `iat/static/images/`); block labels and the reversal notice in Spanish. The 7-block structure, trial counts, keys E/I and the 250 ms delay are unchanged.
- **Pages:** a new `welcome` page (participant code and assigned group, fields `identificador` and `treatment`); the IAT page uses a three-column layout with images and the word in the centre, Spanish instructions, and its CSS moved to `iat/static/css/iat.css`.
- **Session:** one session config (`questions` = `iat` + a new `survey` app with 14 pages), Spanish locale, COP currency.
- **Removed from the original:** the Heroku files (`Procfile`), `tox.ini`, `manage.py`, `BROWSER_COMMAND`, `ROOMS`, the README images in `_doc_imgs/`, and the original English stimuli.
- **Added in 2026:** bots for the welcome page and the survey, pinned dependencies, synthetic sample data, documentation.

## 7. How to cite

If you use this code, please cite it (see [`CITATION.cff`](CITATION.cff)) together with:

- This repository: Medrano León, E. C., Carrillo Cadena, R. A., & Rincón, F. (2026). *Code for: One Talk Shifts Beliefs About Science Jobs but Not Detectably Gender Beliefs: A Randomized Role-Model Visit in a Colombian Technical High School* (version 1.0.0) [Computer software]. https://github.com/ferleyrincon/works
- oTree: Chen, D. L., Schonger, M., & Wickens, C. (2016). oTree—An open-source platform for laboratory, online, and field experiments. *Journal of Behavioral and Experimental Finance, 9*, 88–97. https://doi.org/10.1016/j.jbef.2015.12.001
- Konrad, M. (2019). oTree: Implementing experiments with dynamically determined data quantity. *Journal of Behavioral and Experimental Finance, 21*, 58–60 (online 2018). https://doi.org/10.1016/j.jbef.2018.10.006
- Greenwald, A. G., McGhee, D. E., & Schwartz, J. L. K. (1998). Measuring individual differences in implicit cognition: The implicit association test. *Journal of Personality and Social Psychology, 74*(6), 1464–1480. https://doi.org/10.1037/0022-3514.74.6.1464

## 8. License

Apache License 2.0 (see [`LICENSE`](LICENSE)), inherited from WZB's otree_iat. Modified files carry a notice of the changes (Apache 2.0, section 4b). Participant data are not part of this repository and are not covered by this license.
