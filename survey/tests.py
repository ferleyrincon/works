"""
Survey -- automated test (bot). Added in 2026 for the replication package.

The bot submits every page of `page_sequence` with a random valid value for each form field,
drawn from the field definition in models.py (a random choice, an integer within min/max,
or a short text). It does not change the survey; it checks that all 14 pages can be completed
and produces synthetic data (see sample_data/).
"""

import random

from otree.api import Submission

from . import pages
from ._builtin import Bot
from .models import Player

# Pages whose submit button is created by JavaScript, so the bot's static HTML check cannot see it.
NO_HTML_CHECK = {'saber11', 'occupation'}


def _valid_value(field_name):
    field = Player._meta.get_field(field_name)
    if field.choices:
        return random.choice(field.choices)[0]
    internal = field.get_internal_type()
    if internal in ('IntegerField', 'PositiveIntegerField', 'BigIntegerField'):
        low = getattr(field, 'min', None)
        high = getattr(field, 'max', None)
        low = 1 if low is None else low
        high = low + 4 if high is None else high
        return random.randint(low, high)
    if internal == 'FloatField':
        return round(random.uniform(1, 30), 1)
    return 'texto de prueba'


class PlayerBot(Bot):
    def play_round(self):
        for page in pages.page_sequence:
            data = {name: _valid_value(name) for name in page.form_fields}
            yield Submission(page, data, check_html=page.__name__ not in NO_HTML_CHECK)
