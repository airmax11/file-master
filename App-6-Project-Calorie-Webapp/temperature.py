import requests
from selectorlib import Extractor

THELINK = "https://www.timeanddate.com/weather/"


class Temperature:
    def __init__(self, country, city):
        self.city = city
        self.country = country

    def get(self):
        response = requests.get(f"{THELINK}{self.country}/{self.city}")

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

        extractor = Extractor.from_yaml_file('temperature.yaml')
        temp_value_raw = extractor.extract(response.text)
        temp_value_replaced = temp_value_raw["temp"].replace("\xa0°C", "")
        return float(temp_value_replaced)

