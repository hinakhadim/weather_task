import os


def is_not_valid_directory_path(folder_path):
    """
    Checks whether the given folder path is valid or not

    :param folder_path:
    :return: bool
    """

    return not os.path.isdir(folder_path)


def check_month_is_valid_number(month_number_string):
    """
    Check month should not contain alphabets/characters and
    the given month number is in the range b/w 1 - 12

    :param month_number_string:
    """

    if not month_number_string.isdigit():
        raise Exception("Month name should be a valid Number")

    month = int(month_number_string)
    if month < 1 or month > 12:
        raise Exception("Month name should be valid number from 1 - 12")


def is_month_exists(split_year_month):
    """
    Checks whether the given splitted year_month has month or not

    :param split_year_month:
    :return: bool
    """

    return len(split_year_month) > 1


def is_month_not_given(year_month):
    """
    Check whether the given year_month does not contain month

    :param year_month:
    :return: bool
    """

    split_year_month = year_month.split("/")
    return len(split_year_month) <= 1
