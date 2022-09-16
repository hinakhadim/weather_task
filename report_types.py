from collections import namedtuple

HighLowTempHumidityReportType = namedtuple(
    "HighestLowestTemperatureHumidityReport", [
        'highest_temperature',
        'lowest_temperature',
        'high_humidity'],
    defaults=['', '', ''])
