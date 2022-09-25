from constants import CURRENT_DIRECTORY

from validations import (check_directory_path_exists,
                         validate_year_month,
                         validate_year
                         )
from report_data_provider import ReportDataProvider
from report_generator import ReportGenerator

import argparse


if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser(
        description="Generates reports from the weather data files"
    )

    arg_parser.add_argument(
        "data_folder",
        type=str,
        action='store',
        nargs=1,
        metavar="path/to/folder",
        help="Folder path where data files are stored"
    )

    arg_parser.add_argument(
        '-e',
        type=validate_year,
        metavar="year",
        help="To display the highest, lowest "
             "temperature and highest humidity"
    )

    arg_parser.add_argument(
        '-a',
        type=validate_year_month,
        metavar="year/mm",
        help="To display the average high, low "
             "temperature and average mean humidity"
    )

    arg_parser.add_argument(
        '-c',
        type=validate_year_month,
        metavar="year/mm",
        help="Display charts of high and low "
             "temperature for each day"
    )

    arg_parser.add_argument(
        '-cs',
        type=validate_year_month,
        metavar="year/mm",
        help="Display one line charts of high and low "
             "temperature for each day"
    )

    args = arg_parser.parse_args()

    weather_data_folder_path = CURRENT_DIRECTORY + args.data_folder[0]
    check_directory_path_exists(weather_data_folder_path)

    report_generator = ReportGenerator()

    if args.e:
        data_provider = ReportDataProvider(args.e, weather_data_folder_path)
        report_data = data_provider.get_high_low_temp_high_humidity_data()

        report_generator.gen_report_highest_lowest_temp_and_humidity(
            report_data
        )

    if args.a:
        data_provider = ReportDataProvider(args.a, weather_data_folder_path)
        report_data = data_provider.get_average_temp_and_humidity()

        report_generator.gen_report_average_max_min_temp_and_mean_humidity(
            report_data
        )

    if args.c:
        data_provider = ReportDataProvider(args.c, weather_data_folder_path)
        report_data = data_provider.get_chart_data()

        report_generator.gen_report_high_low_temperature_charts(
            report_data
        )

    if args.cs:
        data_provider = ReportDataProvider(
            args.cs, weather_data_folder_path
        )
        report_data = data_provider.get_chart_data()

        report_generator.gen_report_high_low_temperature_single_line_chart(
            report_data
        )
