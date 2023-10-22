import requests
from datetime import datetime, timedelta

TEQUILA_FLIGHT_ENDPOINT = 'https://api.tequila.kiwi.com/v2'
API_TEQUILA = "API"
CITY = "KRK"
CURRENCY = "PLN"

time_tomorrow = (datetime.now() + timedelta(days=1))
six_month = (time_tomorrow + timedelta(days=180))

time_tomorrow = time_tomorrow.strftime("%d/%m/%Y")
six_month = six_month.strftime("%d/%m/%Y")


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.ENDPOINT = TEQUILA_FLIGHT_ENDPOINT
        self.header_tequila = {
            "apikey": API_TEQUILA,
        }

    def search_flights(self, iataCode: str):
        params = {
            "fly_from": CITY,
            "fly_to": iataCode,
            "date_from": time_tomorrow,
            "date_to": six_month,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "flight_type": "round",
            "curr": CURRENCY
        }

        response = requests.get(url=f"{self.ENDPOINT}/search", params=params, headers=self.header_tequila)
        response.raise_for_status()
        return response.json()
