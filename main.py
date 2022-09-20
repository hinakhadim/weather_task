import sys

from constants import CURRENT_DIRECTORY

from validations import isNotValidDirectoryPath
from validations import is_args_not_given
from report_generator import ReportGenerator

import argparse


if __name__ == "__main__":

    try:

        arg_parser = argparse.ArgumentParser(
            description="Generates reports from the weather data files"
        )

        arg_parser.add_argument("data_folder",
                                type=str,
                                action='store',
                                nargs=1,
                                metavar="path/to/folder",
                                help="Folder path where data files are stored"
                                )

        arg_parser.add_argument('-e',
                                type=str,
                                metavar="year",
                                help="To display the highest, lowest "
                                "temperature and highest humidity"
                                )

        arg_parser.add_argument('-a',
                                type=str,
                                metavar="year/mm",
                                help="To display the average high, low "
                                "temperature and average mean humidit"
                                )

        arg_parser.add_argument('-c',
                                type=str,
                                metavar="year/mm",
                                help="Display charts of high and low "
                                "temperature for each day"
                                )

        arg_parser.add_argument('-cs',
                                type=str,
                                metavar="year/mm",
                                help="Display one line charts of high and low "
                                " temperature for each day"
                                )

        args = arg_parser.parse_args()
        is_args_not_given(args)

        weather_data_folder_path = CURRENT_DIRECTORY + args.data_folder[0]

        if isNotValidDirectoryPath(weather_data_folder_path):
            raise Exception("Invalid path to directory : ",
                            weather_data_folder_path)

        report_generator = ReportGenerator()

        # arg_flags_with_values = sys.argv[2:]

        # if isLengthOdd(arg_flags_with_values):
        #     raise Exception("All flags must have values")

        # for i in range(0, len(arg_flags_with_values), 2):
        #     flag, value = arg_flags_with_values[i],
        #     arg_flags_with_values[i + 1]

        # report_generator = ReportGenerator()
        # report_generator.generate_report_for(
        # flag, value, weather_data_folder_path)

    except Exception as e:
        print(e)
