class WeatherRecord:

    def __init__(self, record_item) -> None:

        self.date = record_item['PKT']
        self.min_temp = record_item['Mean TemperatureC']
        self.max_temp = record_item['Max TemperatureC']
        self.mean_temp = record_item['Min TemperatureC']
        self.min_humidity = record_item[' Min Humidity']
        self.max_humidity = record_item['Max Humidity']
        self.mean_humidity = record_item[' Mean Humidity']
