from year_month_matched_file_paths_provider \
    import YearMonthMatchedFilePathsProvider
from weather_data_analyzer import WeatherDataAnalyzer
from validations import is_month_not_given


class ReportDataProvider:

    def __init__(self, year_month, data_folder):
        self.year_month = year_month

        self.data_analyzer = None
        self.set_data_analyzer(year_month, data_folder)

    def set_data_analyzer(self, year_month, data_folder):

        file_paths = YearMonthMatchedFilePathsProvider(year_month, data_folder)
        matched_file_paths_with_year_month = file_paths.get_matched_file_paths()

        self.data_analyzer = WeatherDataAnalyzer(
            matched_file_paths_with_year_month
        )

    def get_high_low_temp_high_humidity_data(self):

        report_data = self.data_analyzer.calc_low_and_high_temp_and_humid()
        return report_data

    def get_average_temp_and_humidity(self):
        if is_month_not_given(self.year_month):
            raise Exception("Error: Month is required to perform calculations")

        report_data = self.data_analyzer.calc_average_temp_and_humidity()
        return report_data

    def get_chart_data(self, single_line_chart=False):

        if is_month_not_given(self.year_month):
            raise Exception("Error: Month is required to perform calculations")

        report_data = self.data_analyzer.get_charts_data()
        return report_data
