import csv

from weather_record import WeatherRecord


class WeatherStatisticsCalculator:

    def __init__(self, filepaths) -> None:

        self.file_records = []

        for filepath in filepaths:
            self.file_data_reader(filepath)

    def file_data_reader(self, filepath):

        with open(filepath, 'r') as file:
            records_list = csv.DictReader(file)

            for row in records_list:
                record = WeatherRecord(row)
                self.file_records.push(record)

    def display_low_and_high_temp_and_humidity(self):

        low_temp_heap = []
        high_temp_heap = []
        high_humidity_heap = []
