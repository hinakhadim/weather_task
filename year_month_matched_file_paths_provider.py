import os

from validations import check_month_is_valid_number, is_month_exists
from utils import get_month_year_from

Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class YearMonthMatchedFilePathsProvider:
    """ Provides the file paths having year_month in their names """

    def __init__(self, year_month, data_folder_path) -> None:
        self.year = None
        self.month = None
        self.matched_file_paths_with_year_month = []
        self.data_folder_path = data_folder_path

        self.validate(year_month)
        self.store_matched_file_paths_to_list()

    def validate(self, year_month):
        """
        Validate whether the given year_month contains valid month and year
        :param year_month:
        """

        split_year_month = year_month.split("/")

        if is_month_exists(split_year_month):
            month = split_year_month[1]

            check_month_is_valid_number(month)
            self.month = Months[int(month) - 1]

        self.year = split_year_month[0]

    def store_matched_file_paths_to_list(self):
        """
        Call the corresponding functions of storing the matched filepaths
        based on year and month
        """

        if self.month and self.year:
            self.store_file_paths_matched_with_year_and_month()
        elif self.year:
            self.store_file_paths_matched_with_year()
        else:
            raise Exception("Year/Month must be Required")

    def store_file_paths_matched_with_year(self):
        """
        Add the filepaths in the list if filename contains the given year
        """

        for file_name in os.listdir(self.data_folder_path):
            file_year = get_month_year_from(file_name).year

            if self.year == file_year:
                self.matched_file_paths_with_year_month.append(
                    os.path.join(self.data_folder_path, file_name)
                )

    def store_file_paths_matched_with_year_and_month(self):
        """
        Add the filepaths in the list if filename contains the given month and
        year
        """

        for file_name in os.listdir(self.data_folder_path):
            file_month_year = get_month_year_from(file_name)
            file_month, file_year = file_month_year.month, file_month_year.year

            if self.month == file_month and self.year == file_year:
                self.matched_file_paths_with_year_month.append(
                    os.path.join(self.data_folder_path, file_name)
                )
                break

    def get_matched_file_paths(self):
        """
        Returns the filepaths matched with the user given year_month

        :return: List[FilePath]
        """
        return self.matched_file_paths_with_year_month
