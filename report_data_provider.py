from year_month_matched_file_paths_provider import (
    YearMonthMatchedFilePathsProvider
)
from weather_data_analyzer import WeatherDataAnalyzer


class ReportDataProvider:
    """
        Provide report data of different reports
    """

    def __init__(self, year_month, data_folder):
        self.year_month = year_month

        self.data_analyzer = None
        self.set_data_analyzer(year_month, data_folder)

    def set_data_analyzer(self, year_month, data_folder):
        """
        Get file paths matched with the given year_month and pass them into
        weather analyzer

        :param year_month: DateObj
        :param data_folder:
        """

        file_paths = YearMonthMatchedFilePathsProvider(year_month, data_folder)
        matched_file_paths_with_year_month = file_paths.get_matched_file_paths()

        self.data_analyzer = WeatherDataAnalyzer(
            matched_file_paths_with_year_month
        )

    def get_high_low_temp_high_humidity_data(self):
        """
        Returns the high temperature, low temperature and high humidity data
        calculated from weatherAnalyzer

        :return: HighLowTempHumidityReportType
        """

        report_data = self.data_analyzer.calc_low_and_high_temp_and_humid()
        return report_data

    def get_average_temp_and_humidity(self):
        """
        Returns the average high temperature, average low temperature and
        average high humidity data calculated from weatherAnalyzer

        :return: AverageTempHumidReportType
        """

        report_data = self.data_analyzer.calc_average_temp_and_humidity()
        return report_data

    def get_chart_data(self):
        """
        Returns chart data for a month calculated from weatherAnalyzer

        :return: List[WeatherRecords]
        """

        report_data = self.data_analyzer.get_charts_data()
        return report_data
