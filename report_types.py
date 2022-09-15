from collections import namedtuple

HighLowTempHumidityReportType = namedtuple(
    "HighestLowestTemperatureHumidityReport", [
        'highest_temperature',
        'lowest_temperature',
        'high_humidity'],
    defaults=['', '', ''])


AverageTempHumidReportType = namedtuple(
    "AverageTempHumidityReportType", [
        'average_max_temperature',
        'average_min_temperature',
        'average_mean_humidity'],
    defaults=['', '', ''])
