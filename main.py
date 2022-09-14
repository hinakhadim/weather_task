import sys
import os
from file_path_matcher_with_date import FilePathMatcherWithDate

CURRENT_DIRECTORY = os.getcwd()

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("You must specify files path and the command with proper flag")
        sys.exit(0)

    weather_data_files_path = CURRENT_DIRECTORY + sys.argv[1]
    if not os.path.isdir(weather_data_files_path):
        print("Invalid path to directory : ", weather_data_files_path)
        sys.exit(0)

    print(weather_data_files_path)

    system_args = sys.argv[2:]

    year = sys.argv[3]

    file_path_matcher = FilePathMatcherWithDate(weather_data_files_path)
    file_path_matcher.setDate(year)
    matched_file_paths_with_year = file_path_matcher.get_files_path()

    # for index, argument in enumerate(system_args):
    #     pass
