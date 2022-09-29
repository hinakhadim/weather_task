from constants import CURRENT_DIRECTORY

from validations import (check_directory_path_exists,
                         validate_year_month,
                         validate_year
                         )
from report_data_provider import ReportDataProvider
from report_generator import (HighLowTemperatureAndHumidityReport,
                              AverageTemperatureAndHumidityReport,
                              TemperatureChartsReport
                              )

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
        '-display_report',
        type=validate_year,
        metavar="year",
        help="To display the highest, lowest "
             "temperature and highest humidity"
    )

    arg_parser.add_argument(
        '-average_stats_report',
        type=validate_year_month,
        metavar="year/mm",
        help="To display the average high, low "
             "temperature and average mean humidity"
    )
    arg_parser.add_argument(
        '-charts',
        type=validate_year_month,
        metavar="year/mm",
        help="Display charts of high and low "
             "temperature for each day"
    )

    arg_parser.add_argument(
        '-single_line_chart',
        type=validate_year_month,
        metavar="year/mm",
        help="Display one line charts of high and low "
             "temperature for each day"
    )

    args = arg_parser.parse_args()

    weather_data_folder_path = CURRENT_DIRECTORY + args.data_folder[0]
    check_directory_path_exists(weather_data_folder_path)

    if args.display_report:
        data_provider = ReportDataProvider(
            args.display_report, weather_data_folder_path
        )
        report_data = data_provider.get_high_low_temp_high_humidity_data()

        report = HighLowTemperatureAndHumidityReport(report_data)
        report.print_report()

    if args.average_stats_report:
        data_provider = ReportDataProvider(
            args.average_stats_report, weather_data_folder_path
        )
        report_data = data_provider.get_average_temp_and_humidity()

        report = AverageTemperatureAndHumidityReport(report_data)
        report.print_report()

    chart_arguments = {'c': args.charts, 'cs': args.single_line_chart}
    for arg, value in chart_arguments.items():

        if value:
            data_provider = ReportDataProvider(value, weather_data_folder_path)
            report_data = data_provider.get_chart_data()

            report = TemperatureChartsReport(
                report_data, single_line_chart=(arg == 'cs')
            )
            report.print_report()
