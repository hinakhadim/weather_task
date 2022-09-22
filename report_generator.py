from typing import List, Optional
from report_types import AverageTempHumidReportType
from report_types import HighLowTempHumidityReportType
from weather_record import WeatherRecord
from constants import COLORS

from collections import namedtuple

Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class ReportGenerator:

    def gen_report_highest_lowest_temp_and_humidity(
            self, report_data:
            Optional[HighLowTempHumidityReportType]
    ):
        """ Generate Report of highest, lowest temperature and highest 
        humidity from the given report_data"""

        print("\n================== Report =================")
        print(
            "================== Highest and Lowest Temperature and Maximum"
            " Humidity ================="
        )

        if not report_data:
            print("\nThere is no data for generating a report\n")
            return

        highest_temp = report_data.highest_temperature
        lowest_temp = report_data.lowest_temperature
        high_humid = report_data.high_humidity

        print(
            "Highest Temperature: {temp}°C on {date}".format(
                temp=highest_temp.max_temp,
                date=self.format_date_from(highest_temp.date)
            )
        )

        print(
            "Lowest Temperature: {temp}°C on {date}".format(
                temp=lowest_temp.min_temp,
                date=self.format_date_from(lowest_temp.date)
            )
        )

        print(
            "Highest Temperature: {temp}°C on {date}\n".format(
                temp=high_humid.max_humidity,
                date=self.format_date_from(high_humid.date)
            )
        )

    def format_date_from(self, date):
        year, month, day = date.split("-")
        return f"{Months[int(month) - 1]} {day}, {year}"

    def gen_report_average_max_min_temp_and_mean_humidity(
            self, report_data:
            Optional[AverageTempHumidReportType]
    ):
        """ Generate Report of average highest, lowest temperature and mean 
            humidity from the given report_data"""

        print("\n================== Report =================")
        print(
            "================== Average Highest and Lowest Temperature and"
            " Mean Humidity ================="
        )

        if not report_data:
            print("\nThere is no data for generating a report\n")
            return

        average_highest_temp = report_data.average_max_temperature
        average_low_temp = report_data.average_min_temperature
        average_humid = report_data.average_mean_humidity

        print(
            "Highest Average Temperature: {}°C".format(average_highest_temp)
        )
        print(
            "Lowest Average Temperature: {}°C".format(average_low_temp)
        )
        print(
            "Average Mean Humidity: {}%\n".format(average_humid)
        )

    def gen_report_high_low_temperature_charts(
            self, report_data: List[WeatherRecord]
    ):
        """ Generate Report of highest and lowest temperature charts-
        It draws one chart for highest temperature and one for
        lowest temperature for each day"""

        print("\n================== Report =================")

        if not report_data:
            print("\nThere are no data to draw the charts\n")
            return

        date = self.get_date_from(report_data[0].date)
        print(
            "=========== Temperature Charts {month} {date} ===========".format(
                month=Months[int(date.month) - 1],
                date=date.year
            )
        )

        for record in report_data:
            self.draw_2_charts_of_high_low_temp_for_1_day(record)

    def draw_2_charts_of_high_low_temp_for_1_day(self, record: WeatherRecord):
        """
        Draws 2 charts - One in red color for high temperature and other in
        Blue color for low temperature

        :param record: WeatherRecord
        """

        date = self.get_date_from(record.date)
        formatted_day = self.append_zero_to_start_in_day(date.day)

        print(COLORS.RED + formatted_day, end=" ")
        self.draw_temperature_chart(record.max_temp)
        print(f" {record.max_temp}°C")

        print(COLORS.BLUE + formatted_day, end=" ")
        self.draw_temperature_chart(record.min_temp)
        print(f" {record.min_temp}°C")

    def gen_report_high_low_temperature_single_line_chart(
            self, report_data:
            List[WeatherRecord]
    ):
        """ Generate Report of highest and lowest temperature charts-
            It draws one chart for highest temperature lowest temperature 
            for each day"""

        print("\n================== Report =================")

        if not report_data:
            print("\nThere are no data to draw the charts\n")
            return

        date = self.get_date_from(report_data[0].date)
        print(
            "=========== Temperature Charts {month} {date} ===========".format(
                month=Months[int(date.month) - 1], date=date.day
                )
        )

        for record in report_data:
            self.draw_1_chart_of_high_low_temp_for_1_day(record)

    def draw_1_chart_of_high_low_temp_for_1_day(self, record: WeatherRecord):
        """
        Draws 1 chart - Draw both high temperature and low temperature chart
        in one single line containing Red and blue color respectively

        :param record: WeatherRecord
        """

        date = self.get_date_from(record.date)
        formatted_day = self.append_zero_to_start_in_day(date.day)

        print(formatted_day, end=" ")
        print(COLORS.BLUE, end="")
        self.draw_temperature_chart(record.min_temp)
        print(COLORS.RED, end="")
        self.draw_temperature_chart(record.max_temp)
        print(COLORS.ENDC, end="")
        print(f" {record.min_temp}°C - {record.max_temp}°C")

    def draw_temperature_chart(self, temperature_string):
        print("+" * self.get_integer_value_from(temperature_string), end="")

    def append_zero_to_start_in_day(self, day):
        return '0' + day if int(day) < 10 else day

    def get_integer_value_from(self, string):
        return int(string) if string else 0

    def get_date_from(self, date_string):
        Date = namedtuple("Date", ['day', 'month', 'year'])

        year, month, day = date_string.split("-")
        return Date(day, month, year)
