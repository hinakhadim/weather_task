

from typing import Optional
from report_types import AverageTempHumidReportType
from report_types import HighLowTempHumidityReportType


Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class ReportGenerator:

    def highest_lowest_temp_and_humidity(self, report_data:
                                         Optional[
                                             HighLowTempHumidityReportType
                                         ]):

        print("\n================== Report =================")
        print("================== Highest and Lowest Temperature and Maximum"
              "Humidity =================")

        if not report_data:
            print("\nThere is no data for generating a report\n")
            return

        highest_temp = report_data.highest_temperature
        lowest_temp = report_data.lowest_temperature
        high_humid = report_data.high_humidity

        print(
            f"Highest Temperature: {highest_temp.max_temp}°C on "
            f"{self.format_date_from(highest_temp.date)}")
        print(
            f"Lowest Temperature: {lowest_temp.max_temp}°C on "
            f"{self.format_date_from(lowest_temp.date)}")
        print(
            f"Highest Humidity: {high_humid.max_humidity}% on "
            f"{self.format_date_from(high_humid.date)}\n")

    def format_date_from(self, date):
        year, month, day = date.split("-")
        return f"{Months[int(month) - 1]} {day}, {year}"

    def average_max_min_temp_and_mean_humidity(self, report_data:
                                               Optional[
                                                   AverageTempHumidReportType
                                               ]):
        print("\n================== Report =================")
        print("================== Average Highest and Lowest Temperature and"
              "Mean Humidity =================")

        if not report_data:
            print("\nThere is no data for generating a report\n")
            return

        average_highest_temp = report_data.average_max_temperature
        average_low_temp = report_data.average_min_temperature
        average_humid = report_data.average_mean_humidity

        print(
            f"Highest Average Temperature: {average_highest_temp}°C")
        print(
            f"Lowest Average Temperature: {average_low_temp}°C")
        print(
            f"Average Mean Humidity: {average_humid}%\n")
