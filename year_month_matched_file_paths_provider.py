import os

from validations import check_month_is_valid_number, is_month_exists
from utils import get_month_year_from

Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class YearMonthMatchedFilePathsProvider:

    def __init__(self, year_month, data_folder_path) -> None:
        self.year = None
        self.month = None
        self.matched_file_paths_with_year_month = []
        self.data_folder_path = data_folder_path

        self.validate(year_month)
        self.store_matched_file_paths_to_list()

    def validate(self, year_month):
        split_year_month = year_month.split("/")

        if is_month_exists(split_year_month):
            month = split_year_month[1]

            check_month_is_valid_number(month)
            self.month = Months[int(month) - 1]

        self.year = split_year_month[0]

    def store_matched_file_paths_to_list(self):

        if self.month and self.year:
            self.store_file_paths_matched_with_year_and_month()
        elif self.year:
            self.store_file_paths_matched_with_year()
        else:
            raise Exception("Year/Month must be Required")

    def store_file_paths_matched_with_year(self):

        for file_name in os.listdir(self.data_folder_path):
            file_year = get_month_year_from(file_name).year

            if self.year == file_year:
                self.matched_file_paths_with_year_month.append(
                    os.path.join(self.data_folder_path, file_name)
                )

    def store_file_paths_matched_with_year_and_month(self):

        for file_name in os.listdir(self.data_folder_path):
            file_month_year = get_month_year_from(file_name)
            file_month, file_year = file_month_year.month, file_month_year.year

            if self.month == file_month and self.year == file_year:
                self.matched_file_paths_with_year_month.append(
                    os.path.join(self.data_folder_path, file_name)
                )
                break
                # since the given month of the given year has only 1 file

    def get_matched_file_paths(self):
        return self.matched_file_paths_with_year_month
