from website.services.get_timedelta_as_string import get_timedelta_as_string
from unittest import TestCase
from datetime import date


class TimeDeltaAsString(TestCase):
    def test_get_timedelta_as_string_returns_right_value_with_lesser_than_month(self):
        date_one = date(2015, 9, 1)
        date_two = date(2015, 10, 15)
        seconds = (date_two - date_one).total_seconds()
        timedelta_string = get_timedelta_as_string(seconds)
        self.assertEqual(timedelta_string, '1 месяц')

    def test_get_timedelta_as_string_returns_right_value_with_one_year_and_three_months(self):
        date_one = date(2015, 1, 1)
        date_two = date(2016, 3, 3)
        seconds = (date_two - date_one).total_seconds()
        timedelta_string = get_timedelta_as_string(seconds)
        self.assertEqual(timedelta_string, '1 месяц')
