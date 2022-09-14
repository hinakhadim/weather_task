
import os
import re
from collections import namedtuple


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class FilePathMatcherWithDate:

    def __init__(self, data_folder_path) -> None:
        self.month = None
        self.year = None
        self.data_folder_path = data_folder_path

    def setDate(self, date):
        splitted_date = date.split("/")         # date = yyyy/m

        if len(splitted_date) > 1:
            self.month = splitted_date[1]
        self.year = splitted_date[0]

    def get_files_path(self):

        if self.month and self.year:
            return ""
        elif self.year:
            return self.get_specific_year_file_paths()
        else:
            print("Date must be Required")

    def get_specific_year_file_paths(self):
        file_paths_of_a_year = []

        for file_name in os.listdir(self.data_folder_path):
            file_year = self.get_file_month_year(file_name).year

            if self.year == file_year:
                file_paths_of_a_year.append(
                    os.path.join(self.data_folder_path, file_name))

        return file_paths_of_a_year

    def get_file_month_year(self, filename):
        matched_result = list(re.finditer(
            r'(?P<year>\d+)_(?P<month>\w+)', filename))

        DateObj = namedtuple("DateObj", ['month', 'year'], defaults=['', ''])

        if len(matched_result) > 0:
            matched_object = matched_result[0].groupdict()
            date_object = DateObj(
                matched_object['month'], matched_object['year'])
            return date_object

        return DateObj()
