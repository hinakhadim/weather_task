import os
import re
from exceptions import *
from custom_types import DateObj


def check_directory_path_exists(folder_path):
    """
    Checks whether the given folder path is valid or not

    :param folder_path:
    """

    if not os.path.isdir(folder_path):
        raise FolderDoesNotExist("Invalid path to directory : ", folder_path)


def validate_year(year):
    matched_result = re.search(r'^\d{4}$', year)

    if matched_result:
        date_object = DateObj(month=None, year=matched_result[0])
        return date_object

    raise YearRequired("Year should be valid 4 digit number")


def validate_year_month(year_month):
    matched_result = list(
        re.finditer(
            r'^(?P<year>\d{4})/(?P<month>(0?[1-9]|1[0-2]))$', year_month
        )
    )

    if len(matched_result) > 0:
        matched_object = matched_result[0].groupdict()

        date_object = DateObj(matched_object['month'], matched_object['year'])

        return date_object

    raise MonthIsOutOfRange("Month must be valid integer in a range of 1 - 12")
