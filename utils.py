import re

from custom_types import DateObj


def get_month_year_from_filename(filename):
    """
    Extract month, year from given filename

    :param filename:
    :return: DateObj
    """
    matched_result = list(
        re.finditer(
            r'(?P<year>\d+)_(?P<month>\w+)', filename
        )
    )

    if len(matched_result) > 0:
        matched_object = matched_result[0].groupdict()
        date_object = DateObj(matched_object['month'], matched_object['year'])
        return date_object

    return DateObj()


