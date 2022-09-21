from typing import List, Optional
from report_types import AverageTempHumidReportType
from report_types import HighLowTempHumidityReportType
from weather_record import WeatherRecord
from constants import COLORS

Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class ReportGenerator:

    def gen_report_highest_lowest_temp_and_humidity(
            self, report_data:
            Optional[HighLowTempHumidityReportType]
            ):

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
            f"Highest Temperature: {highest_temp.max_temp}°C on "
            f"{self.format_date_from(highest_temp.date)}"
        )
        print(
            f"Lowest Temperature: {lowest_temp.min_temp}°C on "
            f"{self.format_date_from(lowest_temp.date)}"
        )
        print(
            f"Highest Humidity: {high_humid.max_humidity}% on "
            f"{self.format_date_from(high_humid.date)}\n"
        )

    def format_date_from(self, date):
        year, month, day = date.split("-")
        return f"{Months[int(month) - 1]} {day}, {year}"

    def gen_report_average_max_min_temp_and_mean_humidity(
            self, report_data:
            Optional[
                AverageTempHumidReportType
            ]
            ):
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
            f"Highest Average Temperature: {average_highest_temp}°C"
        )
        print(
            f"Lowest Average Temperature: {average_low_temp}°C"
        )
        print(
            f"Average Mean Humidity: {average_humid}%\n"
        )

    def gen_report_high_low_temperature_charts(
            self, report_data: List[WeatherRecord]
            ):

        print("\n================== Report =================")

        if not report_data:
            print("\nThere are no data to draw the charts\n")
            return

        date = self.get_date_from(report_data[0].date)
        print(
            "================= Temperature Charts"
            f" {Months[int(date['month']) - 1]}, {date['year']} ==============="
            )

        for record in report_data:
            self.draw_2_charts_of_high_low_temp_for_1_day(record)

    def draw_2_charts_of_high_low_temp_for_1_day(self, record: WeatherRecord):
        day = self.get_date_from(record.date)['day']
        formatted_day = self.append_zero_to_start_in_day(day)

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

        print("\n================== Report =================")

        if not report_data:
            print("\nThere are no data to draw the charts\n")
            return

        date = self.get_date_from(report_data[0].date)
        print(
            "================== Temperature Charts"
            f" {Months[int(date['month']) - 1]}, {date['year']} ================="
            )

        for record in report_data:
            self.draw_1_chart_of_high_low_temp_for_1_day(record)

    def draw_1_chart_of_high_low_temp_for_1_day(self, record: WeatherRecord):
        day = self.get_date_from(record.date)['day']
        formatted_day = self.append_zero_to_start_in_day(day)

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
        year, month, day = date_string.split("-")
        return {'day': day, 'month': month, 'year': year}


