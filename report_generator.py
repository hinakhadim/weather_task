from typing import List, Optional
from custom_types import AverageTempHumidReportType
from custom_types import HighLowTempHumidityReportType
from weather_record import WeatherRecord
from constants import COLORS

from collections import namedtuple
from abc import ABCMeta, abstractmethod

Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class ReportGenerator(metaclass=ABCMeta):

    def __init__(self, report_data):
        self.report_data = report_data

    def print_report_header(self, header_title):
        """ Print the header of the report"""

        print("\n================== Report =================")
        print("========== {title} =========".format(title=header_title))

    @abstractmethod
    def print_report(self):
        """ Print the header and report """

        pass

    def print_temperature_chart(self, temperature_string):
        """ Print the chart -> print + signs (temperature) number of times """
        print("+" * self.convert_to_number(temperature_string), end="")

    def add_leading_zero(self, day):
        return day.zfill(2)

    def convert_to_number(self, string):
        return int(string) if string else 0

    def get_date_from(self, date_string):
        """ Get date object from given string """

        Date = namedtuple("Date", ['day', 'month', 'year'])

        year, month, day = date_string.split("-")
        return Date(self.add_leading_zero(day), Months[int(month) - 1], year)

    def get_formatted_date(self, date_string):
        """Get formatted date in string"""

        day, month, year = self.get_date_from(date_string)
        return f"{year} {month}, {day}"


class HighLowTemperatureAndHumidityReport(ReportGenerator):

    def __init__(self, report_data: Optional[HighLowTempHumidityReportType]):
        super().__init__(report_data)

    def print_report(self):
        self.print_report_header(
            "Highest and Lowest Temperature and Maximum Humidity"
        )

        if not self.report_data:
            print("\nThere is no data for generating a report\n")
            return

        highest_temp = self.report_data.highest_temperature
        lowest_temp = self.report_data.lowest_temperature
        high_humid = self.report_data.high_humidity

        print(
            "Highest Temperature: {temp}°C on {date}".format(
                temp=highest_temp.max_temp,
                date=self.get_formatted_date(highest_temp.date)
            )
        )

        print(
            "Lowest Temperature: {temp}°C on {date}".format(
                temp=lowest_temp.min_temp,
                date=self.get_formatted_date(lowest_temp.date)
            )
        )

        print(
            "Highest Temperature: {temp}°C on {date}\n".format(
                temp=high_humid.max_humidity,
                date=self.get_formatted_date(high_humid.date)
            )
        )


class AverageTemperatureAndHumidityReport(ReportGenerator):

    def __init__(self, report_data: Optional[AverageTempHumidReportType]):
        super().__init__(report_data)

    def print_report(self):
        self.print_report_header(
            "Average Highest and Lowest Temperature and Mean Humidity"
        )

        if not self.report_data:
            print("\nThere is no data for generating a report\n")
            return

        average_highest_temp = self.report_data.average_max_temperature
        average_low_temp = self.report_data.average_min_temperature
        average_humid = self.report_data.average_mean_humidity

        print(
            "Highest Average Temperature: {:.2f}°C".format(average_highest_temp)
        )
        print(
            "Lowest Average Temperature: {:.2f}°C".format(average_low_temp)
        )
        print(
            "Average Mean Humidity: {:.2f}%\n".format(average_humid)
        )


class TemperatureChartsReport(ReportGenerator):
    def __init__(
            self, report_data: List[WeatherRecord], single_line_chart=False
    ):
        super().__init__(report_data)
        self.single_line_chart = single_line_chart

    def print_report(self):

        if not self.report_data:
            print("\nThere are no data to draw the charts\n")
            return

        date = self.get_date_from(self.report_data[0].date)
        self.print_report_header(
            "Temperature Charts {month} {date}".format(
                month=date.month,
                date=date.year
            )
        )

        if self.single_line_chart:
            self.draw_single_line_chart()
        else:
            self.draw_double_line_charts()

    def draw_double_line_charts(self):
        """
        Draws 2 charts - One in red color for high temperature and other in
        Blue color for low temperature on different lines
        """

        for record in self.report_data:
            date = self.get_date_from(record.date)

            print(COLORS.RED + date.day, end=" ")
            self.print_temperature_chart(record.max_temp)
            print(f" {record.max_temp}°C")

            print(COLORS.BLUE + date.day, end=" ")
            self.print_temperature_chart(record.min_temp)
            print(f" {record.min_temp}°C")

    def draw_single_line_chart(self):
        """
        Draws 1 chart - Draw both high temperature and low temperature chart
        in one single line containing Red and blue color respectively
        """

        for record in self.report_data:
            date = self.get_date_from(record.date)

            print(date.day, end=" ")
            print(COLORS.BLUE, end="")
            self.print_temperature_chart(record.min_temp)
            print(COLORS.RED, end="")
            self.print_temperature_chart(record.max_temp)
            print(COLORS.ENDC, end="")
            print(f" {record.min_temp}°C - {record.max_temp}°C")
