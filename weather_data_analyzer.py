import csv
import sys
from typing import List

from weather_record import WeatherRecord
from custom_types import (AverageTempHumidReportType,
                          HighLowTempHumidityReportType)


class WeatherDataAnalyzer:
    """
    Receives the file paths and store their record in the list. Then perform
    different calculations on that list
    """

    def __init__(self, filepaths) -> None:

        self.file_records: List[WeatherRecord] = []

        self.file_data_reader_and_add_to_file_records(filepaths)

    def file_data_reader_and_add_to_file_records(self, filepaths):
        """
        Read the data of all files given in filepaths and append it to the list

        :param filepaths:
        """

        for filepath in filepaths:
            with open(filepath, 'r') as file:
                records_list = csv.DictReader(file)

                for row in records_list:
                    record = WeatherRecord(row)
                    self.file_records.append(record)

    def calc_low_and_high_temp_and_humid(self):

        if len(self.file_records) == 0:
            return None

        return self.get_low_high_temp_and_max_humidity()

    def get_low_high_temp_and_max_humidity(self):
        """
        From the file_records list, it returns the max of high temperature, min
        of low temperature and max of high humidity

        :return: HighLowTempHumidityReportType
        """

        valid_high_temp_records = self.remove_none_values_of_max_temp()
        valid_low_temp_records = self.remove_none_values_of_min_temp()
        valid_high_humidity_records = self.remove_none_values_of_max_humidity()

        max_high_temp = max(
            valid_high_temp_records, key=lambda x: int(x.max_temp)
        )
        min_low_temp = min(
            valid_low_temp_records, key=lambda x: int(x.min_temp)
        )
        max_high_humidity = max(
            valid_high_humidity_records, key=lambda x: int(x.max_humidity)
        )

        return HighLowTempHumidityReportType(
            highest_temperature=max_high_temp,
            lowest_temperature=min_low_temp,
            high_humidity=max_high_humidity
        )

    def remove_none_values_of_max_temp(self):
        """
        Removes the records from file_records whose max_temperature value is None

        :return: List[WeatherRecords]
        """

        valid_max_temps = [
            rec for rec in self.file_records if rec.max_temp
        ]
        return valid_max_temps

    def remove_none_values_of_min_temp(self):
        """
        Removes the records from file_records whose min_temperature value is None

        :return: List[WeatherRecords]
        """

        valid_min_temps = [
            rec for rec in self.file_records if rec.min_temp
        ]
        return valid_min_temps

    def remove_none_values_of_max_humidity(self):
        """
        Removes the records from file_records whose max_humidity value is None

        :return: List[WeatherRecords]
        """

        valid_max_humidity = [
            rec for rec in self.file_records if rec.max_humidity
        ]
        return valid_max_humidity

    def remove_none_values_of_mean_humidity(self):
        """
        Removes the records from file_records whose mean_humidity value is None

        :return: List[WeatherRecords]
        """

        valid_mean_humidity = [
            rec for rec in self.file_records if rec.mean_humidity
        ]
        return valid_mean_humidity

    def calc_average_temp_and_humidity(self):
        """
        Returns the average of max_temperature, min_temperature and
        mean_humidity

        :return: AverageTempHumidReportType
        """

        if len(self.file_records) == 0:
            return None

        report = AverageTempHumidReportType(
            average_max_temperature=self.get_average_max_temperature(),
            average_min_temperature=self.get_average_min_temperature(),
            average_mean_humidity=self.get_average_mean_humidity()
        )

        return report

    def get_average_max_temperature(self):
        """
        Calculates the average of max_temperature from the file_records list

        :return: average - float
        """

        valid_max_temps = self.remove_none_values_of_max_temp()
        total = sum([int(rec.max_temp) for rec in valid_max_temps])
        return total / len(self.file_records)

    def get_average_min_temperature(self):
        """
        Calculates the average of min_temperature from the file_records list

        :return: average - float
        """

        valid_min_temps = self.remove_none_values_of_min_temp()
        total = sum([int(rec.min_temp) for rec in valid_min_temps])
        return total / len(self.file_records)

    def get_average_mean_humidity(self):
        """
        Calculates the average of mean_humidity from the file_records list

        :return: average - float
        """

        valid_mean_humidity = self.remove_none_values_of_mean_humidity()
        total = sum([int(rec.mean_humidity) for rec in valid_mean_humidity])
        return total / len(self.file_records)

    def get_charts_data(self):
        """
        Returns the data of files

        :return: file_records - List[WeatherRecord]
        """

        return self.file_records
