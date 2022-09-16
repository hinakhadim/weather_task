import sys
import os
from report_generator import ReportGenerator
from file_path_matcher_with_date import FilePathsProviderMatchedWithDate
from weather_statistics_calculator import WeatherStatisticsCalculator

CURRENT_DIRECTORY = os.getcwd()
MIN_REQUIRED_ARGS = 4


def isNotValidLengthOfARGS(arguments):
    return len(arguments) < MIN_REQUIRED_ARGS


def isNotValidDirectoryPath(folder_path):
    print(folder_path)
    return not os.path.isdir(folder_path)


def isOdd(args):
    return len(args) % 2 != 0


def generate_report(flag, value, data_folder):
    match flag:
        case '-e':
            generateReportHighLowTempHumidity(value, data_folder)
        case '-a':
            generateReportAverageTempHumidity(value, data_folder)
        case '-c':
            generateTemperatureChartReport(value, data_folder)
        case '-cs':
            generateTemperatureChartReport(
                value, data_folder, single_chart=True)
        case _:
            print("No flag sent")


def get_statistics_calculator_instance(date, data_folder):

    file_paths_provider = FilePathsProviderMatchedWithDate(data_folder)
    file_paths_provider.setDate(date)
    matched_file_paths_with_year = file_paths_provider.get_matched_files_path()

    statistics_calculator = WeatherStatisticsCalculator(
        matched_file_paths_with_year)
    return statistics_calculator


def generateReportHighLowTempHumidity(year, data_folder):

    statistics_calculator = get_statistics_calculator_instance(
        year, data_folder)
    report_data = statistics_calculator.calc_low_and_high_temp_and_humidity()

    generate_report = ReportGenerator()
    generate_report.highest_lowest_temp_and_humidity(report_data)


def generateReportAverageTempHumidity(date, data_folder):   # date = year/month

    statistics_calculator = get_statistics_calculator_instance(
        date, data_folder)
    report_data = statistics_calculator.calc_average_temp_and_humidity()

    generate_report = ReportGenerator()
    generate_report.average_max_min_temp_and_mean_humidity(report_data)


# date = year/month
def generateTemperatureChartReport(date, data_folder, single_chart=False):

    statistics_calculator = get_statistics_calculator_instance(
        date, data_folder)
    report_data = statistics_calculator.get_charts_data()

    generate_report = ReportGenerator()
    if single_chart:
        generate_report.high_low_temperature_single_chart(report_data)
    else:
        generate_report.high_low_temperature_charts(report_data)


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

    for i in range(0, (len(arg_flags_with_values) // 2) + 1, 2):
        flag, value = arg_flags_with_values[i], arg_flags_with_values[i + 1]
        generate_report(flag, value, weather_data_folder_path)
