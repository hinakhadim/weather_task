
from file_path_matcher_with_date import FilePathsProviderMatchedWithDate
from report_template import ReportTemplate
from weather_statistics_calculator import WeatherStatisticsCalculator


class ReportGenerator:

    def generate_report_for(self, flag, value, data_folder):
        match flag:
            case '-e':
                self.generateReportHighLowTempHumidity(value, data_folder)
            case '-a':
                self.generateReportAverageTempHumidity(value, data_folder)
            case '-c':
                self.generateTemperatureChartReport(value, data_folder)
            case '-cs':
                self.generateTemperatureChartReport(
                    value, data_folder, single_chart=True)
            case _:
                print("No flag sent")

    def get_statistics_calculator_instance(self, date, data_folder):

        file_paths = FilePathsProviderMatchedWithDate(data_folder)
        file_paths.matchWith(date)
        matched_file_paths_with_date = file_paths.get_matched_files_path()

        statistics_calculator = WeatherStatisticsCalculator(
            matched_file_paths_with_date)
        return statistics_calculator

    def generateReportHighLowTempHumidity(self, year, data_folder):

        statistics_calculator = self.get_statistics_calculator_instance(
            year, data_folder)
        report_data = statistics_calculator.calc_low_and_high_temp_and_humid()

        report_template_of = ReportTemplate()
        report_template_of.highest_lowest_temp_and_humidity(report_data)

    # date = year/month
    def generateReportAverageTempHumidity(self, date, data_folder):
        # date = yyyy/m
        if self.is_not_month_given(date):
            print("Error: Month is required to perform calculations")
            return

        statistics_calculator = self.get_statistics_calculator_instance(
            date, data_folder)
        report_data = statistics_calculator.calc_average_temp_and_humidity()

        report_template_of = ReportTemplate()
        report_template_of.average_max_min_temp_and_mean_humidity(report_data)

    # date = year/month

    def generateTemperatureChartReport(self, date, data_folder,
                                       single_chart=False):

        if self.is_not_month_given(date):
            print("Error: Month is required to perform calculations")
            return

        statistics_calculator = self.get_statistics_calculator_instance(
            date, data_folder)
        report_data = statistics_calculator.get_charts_data()

        report_template_of = ReportTemplate()
        if single_chart:
            report_template_of.high_low_temperature_single_chart(report_data)
        else:
            report_template_of.high_low_temperature_charts(report_data)

    def is_not_month_given(self, date):
        splitted_date = date.split("/")
        return len(splitted_date) <= 1
