import re

from collections import namedtuple


def get_month_year_from(filename):
    matched_result = list(
        re.finditer(
            r'(?P<year>\d+)_(?P<month>\w+)', filename
        )
    )

    DateObj = namedtuple("DateObj", ['month', 'year'], defaults=['', ''])

    if len(matched_result) > 0:
        matched_object = matched_result[0].groupdict()
        date_object = DateObj(matched_object['month'], matched_object['year'])
        return date_object

    return DateObj()


