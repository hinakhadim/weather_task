import csv
import sys
from typing import List

from weather_record import WeatherRecord
from custom_types import (AverageTempHumidReportType,
                          HighLowTempHumidityReportType
                          )


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

        report_fields = {'max_temp': 0, 'min_temp': 0, 'max_humidity': 0}

        for field, value in report_fields.items():
            valid_records = self.remove_none_values_of(field)

            if 'min' in field:
                extreme_value = self.get_min_value(valid_records, field)
            else:
                extreme_value = self.get_max_value(valid_records, field)

            report_fields[field] = extreme_value

        return HighLowTempHumidityReportType(
            highest_temperature=report_fields['max_temp'],
            lowest_temperature=report_fields['min_temp'],
            high_humidity=report_fields['max_humidity']
        )

    def get_min_value(self, record_list, field):
        """ Returns min value of the given field from record list """

        return min(
            record_list, key=lambda x: self.get_attr_value(x, field)
        )

    def get_max_value(self, record_list, field):
        """ Returns max value of the given field from record list """

        return max(
            record_list, key=lambda x: self.get_attr_value(x, field)
        )

    def remove_none_values_of(self, field_name: str):
        """
        Removes the records from file_records whose given field value is
        empty string/None

        :return: List[WeatherRecords]
        """

        return list(
            filter(
                lambda rec: self.get_attr_value(rec, field_name),
                self.file_records
            )
        )

    def get_attr_value(self, record: WeatherRecord, field: str):
        record_dict = vars(record)
        return int(record_dict[field]) if record_dict[field] else None

    def calc_average_temp_and_humidity(self):
        """
        Returns the average of max_temperature, min_temperature and
        mean_humidity

        :return: AverageTempHumidReportType
        """

        if len(self.file_records) == 0:
            return None

        report = AverageTempHumidReportType(
            average_max_temperature=self.get_average_of("max_temp"),
            average_min_temperature=self.get_average_of("min_temp"),
            average_mean_humidity=self.get_average_of("mean_humidity")
        )

        return report

    def get_average_of(self, field):
        """ Returns Average of given field values """

        valid_attribute_records = self.remove_none_values_of(field)
        total = sum(
            [self.get_attr_value(rec, field) for rec in valid_attribute_records]
        )
        return total / len(self.file_records)

    def get_charts_data(self):
        """
        Returns the data of files

        :return: file_records - List[WeatherRecord]
        """

        return self.file_records
