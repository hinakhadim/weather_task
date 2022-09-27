import pandas as pd
import os
import fileinput


def remove_spaces_from_header_files(folder):
    for filename in os.listdir(folder):
        file_name = os.path.join(folder, filename)
        df = pd.read_csv(file_name, nrows=0)  # read only the header row
        df.rename(
            columns={" Min Humidity": "Min Humidity",
                     " Mean Humidity": "Mean Humidity"}, inplace=True
            )
        header_row = ','.join(df.columns)

        # modify header in csv file
        f = fileinput.input(file_name, inplace=True)
        for line in f:
            if fileinput.isfirstline():
                print(header_row)
            else:
                print(line, end='')
        f.close()


if __name__ == '__main__':
    print("Files Data Cleaner")
    remove_spaces_from_header_files(
        '/Users/hinakhadim/Documents/Arbisoft/Python/weather_task/weatherfiles'
        )
    print("done")
