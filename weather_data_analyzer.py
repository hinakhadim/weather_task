import csv
import sys
from weather_record import WeatherRecord
from custom_types import (AverageTempHumidReportType,
                          HighLowTempHumidityReportType)

dummy_record_for_comparison = {
    'PKT': "2022-08-16",
    'Mean TemperatureC': None,
    'Max TemperatureC': -sys.maxsize,
    'Min TemperatureC': sys.maxsize,
    ' Min Humidity': sys.maxsize,
    'Max Humidity': -sys.maxsize,
    ' Mean Humidity': None
}


class WeatherDataAnalyzer:
    """
    Receives the file paths and store their record in the list. Then perform
    different calculations on that list
    """

    def __init__(self, filepaths) -> None:

        self.file_records = []

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

        max_high_temp = WeatherRecord(dummy_record_for_comparison)
        min_low_temp = WeatherRecord(dummy_record_for_comparison)
        max_high_humidity = WeatherRecord(dummy_record_for_comparison)

        for record in self.file_records:

            if self.high_temp_less_than_record(max_high_temp, record):
                max_high_temp = record

            if self.low_temp_greater_than_record(min_low_temp, record):
                min_low_temp = record

            if self.high_humid_less_than_record(max_high_humidity, record):
                max_high_humidity = record

        return HighLowTempHumidityReportType(
            highest_temperature=max_high_temp,
            lowest_temperature=min_low_temp,
            high_humidity=max_high_humidity
        )

    def high_temp_less_than_record(self, max_high_temp, record):
        """
        Returns true if given record has max_temp greater than the
        max_temp of max_high_temp

        :param max_high_temp:
        :param record:
        :return: bool
        """

        if record.max_temp:
            if int(max_high_temp.max_temp) < int(record.max_temp):
                return True
        return False

    def low_temp_greater_than_record(self, min_low_temp, record):
        """
        Returns true if the given record has min_temp minimum than the already
        min_temp of min_low_temp

        :param min_low_temp:
        :param record:
        :return: bool
        """

        if record.min_temp:
            if int(min_low_temp.min_temp) > int(record.min_temp):
                return True
        return False

    def high_humid_less_than_record(self, max_high_humid, record):
        """
        Returns true if the given record has max_humidity greater than the
        already max_humidity of max_high_humid

        :param max_high_humid:
        :param record:
        :return: bool
        """

        if record.max_humidity:
            if int(max_high_humid.max_humidity) < int(record.max_humidity):
                return True
        return False

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

        valid_max_temps = [
            int(rec.max_temp) for rec in self.file_records if rec.max_temp
        ]
        total = sum(valid_max_temps)
        return total / len(self.file_records)

    def get_average_min_temperature(self):
        """
        Calculates the average of min_temperature from the file_records list

        :return: average - float
        """

        valid_min_temps = [
            int(rec.min_temp) for rec in self.file_records if rec.min_temp
        ]
        total = sum(valid_min_temps)
        return total / len(self.file_records)

    def get_average_mean_humidity(self):
        """
        Calculates the average of mean_humidity from the file_records list

        :return: average - float
        """

        valid_mean_humidity = [
            int(rec.mean_humidity) for rec in self.file_records
            if rec.mean_humidity
        ]
        total = sum(valid_mean_humidity)
        return total / len(self.file_records)

    def get_charts_data(self):
        """
        Returns the data of files

        :return: file_records - List[WeatherRecord]
        """

        return self.file_records
