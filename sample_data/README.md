# Synthetic sample data

These files were produced by the oTree bots (`iat/tests.py`, `survey/tests.py`) with
`python sample_data/generate_sample_data.py` (6 bot participants, seed 2022). Every value is a random
bot answer: **no participant data**. Use them to see the structure of the exports.

| File | Rows | Content |
|---|---|---|
| `all_apps_wide.csv` | 1 per participant | oTree wide export (all apps) |
| `iat.csv` | 1 per participant and block (7) | `identificador`, `treatment` |
| `survey.csv` | 1 per participant | all survey fields |
| `iat_trials.csv` | 1 per IAT trial (110 per participant) | block, trial, stimulus, response key, correctness, `response_time_ms` |

Bot response times are random integers between 100 and 1100 ms and correctness is random, so the
files cannot be used to compute IAT scores.
