import requests
from flight_data import FlightData
from data_manager import DataManager
from pprint import pprint
API_key = "API_key"
CITY = "Krakow"

class FlightSearch:

    def __init__(self, city: str):
        self.ENDPOINT = 'https://api.tequila.kiwi.com'
        self.HEADER = {
            'apikey': API_key,
        }
        self.city = city
        self.sheet_data_manager = DataManager()
        self.sheet_data = self.sheet_data_manager.sheety_get_response()
        self.dict = {}

    def get_location(self):
        url = f"{self.ENDPOINT}/locations/query"
        params = {
            "term": self.city,
            "location_type": "city"
        }
        response = requests.get(url=url, params=params, headers=self.HEADER)
        response.raise_for_status()
        return response.json()

    def get_flights(self):
        for row in self.sheet_data['prices']:
            # print(row)
            flight_data = FlightData()
            iataCode = row['iataCode']
            response = flight_data.search_flights(iataCode=iataCode)
            try:
                arrival = (response['data'][0]['route'][0]['local_arrival']).split('T')[0]
                departure = (response['data'][0]['route'][1]['local_departure']).split('T')[0]
                price = response['data'][0]['price']
                to_city = response['data'][0]['cityTo']
                iata_from = response['data'][0]['cityCodeFrom']
                iata_to = response['data'][0]['cityCodeTo']
            except IndexError:
                print(f"There is no flight for {row['city']}.")
            else:
                print(f"Only {price} pln to fly from {CITY}-{iata_from} to {to_city}-{iata_to}, "
                      f"from {arrival} to {departure}")
