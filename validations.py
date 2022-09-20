import os
from constants import MIN_REQUIRED_ARGS


def is_args_not_given(arguments):
    if not (arguments.e or arguments.a or arguments.c or arguments.cs):
        raise Exception(
            "You must specify the values with proper flag")


def isNotValidDirectoryPath(folder_path):
    return not os.path.isdir(folder_path)
