"""
Survey -- automated test (bot). Added in 2026 for the replication package.

The bot submits every page of `page_sequence` with a valid value for each form field,
derived from the field definition in models.py (first choice, minimum, or a short text).
It does not change the survey; it only checks that all 14 pages can be completed.
"""

from . import pages
from ._builtin import Bot
from .models import Player


def _valid_value(field_name):
    field = Player._meta.get_field(field_name)
    if field.choices:
        return field.choices[0][0]
    internal = field.get_internal_type()
    if internal in ('IntegerField', 'PositiveIntegerField', 'FloatField', 'BigIntegerField'):
        minimum = getattr(field, 'min', None)
        return minimum if minimum is not None else 1
    return 'test'


class PlayerBot(Bot):
    def play_round(self):
        for page in pages.page_sequence:
            yield (page, {name: _valid_value(name) for name in page.form_fields})
