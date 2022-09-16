import csv
import sys
from weather_record import WeatherRecord
from report_types import AverageTempHumidReportType
from report_types import HighLowTempHumidityReportType


class WeatherStatisticsCalculator:

    def __init__(self, filepaths) -> None:

        self.file_records = []

        for filepath in filepaths:
            self.file_data_reader_and_add_to_file_records(filepath)

    def file_data_reader_and_add_to_file_records(self, filepath):
        print(filepath)
        with open(filepath, 'r') as file:
            records_list = csv.DictReader(file)

            for row in records_list:
                record = WeatherRecord(row)
                self.file_records.append(record)

    def calc_low_and_high_temp_and_humidity(self):

        if len(self.file_records) == 0:
            return None

        report = HighLowTempHumidityReportType(
            highest_temperature=self.get_highest_max_temperature(),
            lowest_temperature=self.get_lowest_min_temperature,
            high_humidity=self.get_highest_max_humidity()
        )

        return report

    def get_highest_max_temperature(self):
        return sorted(self.file_records,
                      key=self.max_temperature_sorter, reverse=True)[0]

    def max_temperature_sorter(self, record):
        if record.max_temp:
            return int(record.max_temp)
        return -sys.maxsize

    def get_lowest_min_temperature(self):
        return sorted(self.file_records, key=self.min_temperature_sorter)[0]

    def min_temperature_sorter(self, record):
        if record.min_temp:
            return int(record.min_temp)
        return sys.maxsize

    def get_highest_max_humidity(self):
        return sorted(self.file_records,
                      key=self.max_humidity_sorter, reverse=True)[0]

    def max_humidity_sorter(self, record):
        if record.max_humidity:
            return int(record.max_humidity)
        return -sys.maxsize

    def calc_average_temp_and_humidity(self):
        if len(self.file_records) == 0:
            return None

        report = AverageTempHumidReportType(
            average_max_temperature=self.get_average_max_temperature(),
            average_min_temperature=self.get_average_min_temperature(),
            average_mean_humidity=self.get_average_mean_humidity()
        )

        return report

    def get_average_max_temperature(self):
        total_sum_of_max_temp = 0
        for record in self.file_records:

            if record.max_temp:
                total_sum_of_max_temp += int(record.max_temp)
            # else : assume max_temp to zero

        return total_sum_of_max_temp / len(self.file_records)

    def get_average_min_temperature(self):
        total_sum_of_min_temp = 0
        for record in self.file_records:

            if record.min_temp:
                total_sum_of_min_temp += int(record.min_temp)
            # else : assume max_temp to zero

        return total_sum_of_min_temp / len(self.file_records)

    def get_average_mean_humidity(self):
        total_sum_of_mean_humid = 0

        for record in self.file_records:

            if record.mean_humidity:
                total_sum_of_mean_humid += int(record.mean_humidity)
            # else : assume max_temp to zero

        return total_sum_of_mean_humid / len(self.file_records)
