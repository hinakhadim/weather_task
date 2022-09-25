import os

from custom_types import DateObj
from utils import get_month_year_from_filename

Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class YearMonthMatchedFilePathsProvider:
    """ Provides the file paths having year_month in their names """

    def __init__(self, year_month: DateObj, data_folder_path) -> None:
        self.year = year_month.year
        self.month = year_month.month

        self.matched_file_paths_with_year_month = []
        self.data_folder_path = data_folder_path

        self.store_matched_file_paths_to_list()

    def store_matched_file_paths_to_list(self):
        """
        Call the corresponding functions of storing the matched filepaths
        based on year and month
        """

        if self.month and self.year:
            self.store_file_paths_matched_with_year_and_month()
        elif self.year:
            self.store_file_paths_matched_with_year()

    def store_file_paths_matched_with_year(self):
        """
        Add the filepaths in the list if filename contains the given year
        """

        for file_name in os.listdir(self.data_folder_path):
            file_year = get_month_year_from_filename(file_name).year

            if self.year == file_year:
                self.matched_file_paths_with_year_month.append(
                    os.path.join(self.data_folder_path, file_name)
                )

    def store_file_paths_matched_with_year_and_month(self):
        """
        Add the filepaths in the list if filename contains the given month and
        year
        """
        user_given_month = Months[int(self.month) - 1]
        for file_name in os.listdir(self.data_folder_path):
            file_month_year = get_month_year_from_filename(file_name)
            file_month, file_year = file_month_year.month, file_month_year.year

            if user_given_month == file_month and self.year == file_year:
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
