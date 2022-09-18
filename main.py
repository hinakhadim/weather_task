import sys
import os
from report_generator import ReportGenerator

CURRENT_DIRECTORY = os.getcwd()
MIN_REQUIRED_ARGS = 4


def isNotValidLengthOfARGS(arguments):
    return len(arguments) < MIN_REQUIRED_ARGS


def isNotValidDirectoryPath(folder_path):
    print(folder_path)
    return not os.path.isdir(folder_path)


def isOdd(args):
    return len(args) % 2 != 0


if __name__ == "__main__":

    if isNotValidLengthOfARGS(sys.argv):
        print("You must specify files path and the command with proper flag")
        sys.exit(0)

    weather_data_folder_path = CURRENT_DIRECTORY + sys.argv[1]
    if isNotValidDirectoryPath(weather_data_folder_path):
        print("Invalid path to directory : ", weather_data_folder_path)
        sys.exit(0)

    arg_flags_with_values = sys.argv[2:]

    if isOdd(arg_flags_with_values):
        print("All flags must have values")
        sys.exit(0)

    for i in range(0, len(arg_flags_with_values), 2):
        flag, value = arg_flags_with_values[i], arg_flags_with_values[i + 1]

        report_generator = ReportGenerator()
        report_generator.generate_report_for(
            flag, value, weather_data_folder_path)
