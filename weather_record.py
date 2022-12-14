class WeatherRecord:

    def __init__(self, record_item) -> None:

        self.date = record_item['PKT']
        self.min_temp = record_item['Mean TemperatureC']
        self.max_temp = record_item['Max TemperatureC']
        self.avg_temp = record_item['Min Temperature']
        self.min_humidity = record_item[' Min Humidity']
        self.max_humidity = record_item['Max Humidity']
        self.avg_humidity = record_item[' Mean Humidity']

    def __lt__(self, nxt):
        return self.avg_temp < nxt.avg_temp
