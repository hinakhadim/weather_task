

from typing import Optional
from report_types import HighLowTempHumidityReportType


Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class ReportGenerator:

    def highest_lowest_temp_and_humidity(self, report_data:
                                         Optional[
                                             HighLowTempHumidityReportType
                                         ]):

        print("\n================== Report =================")

        if not report_data:
            print("There is no data for generating a report")

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
            f"Highest Humidity: {high_humid.max_humidity}°C on "
            f"{self.format_date_from(high_humid.date)}\n")

    def format_date_from(self, date):
        year, month, day = date.split("-")
        return f"{Months[int(month) - 1]} {day}, {year}"
