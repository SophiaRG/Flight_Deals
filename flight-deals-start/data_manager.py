SHEET_ENDPOINT = 'https://api.sheety.co/a61d7f72d3d5c3dba26921192d6e886d/myWorkouts/workouts'
import requests
TOKEN = 'FlightInfo'

class DataManager:

    def __init__(self):
        self.SHEET_ENDPOINT = 'https://api.sheety.co/a61d7f72d3d5c3dba26921192d6e886d/flightDeals/prices'
        self.headers = {
            "Authorization": f"Bearer {TOKEN}"
        }

    def sheety_get_response(self):
        response = requests.get(url=self.SHEET_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def sheety_put_request(self, iataCode: str, row: int):
        params = {
            "price": {
                "iataCode": iataCode,
            }
        }
        url = f"{self.SHEET_ENDPOINT}/{row}"
        response = requests.put(url=url, json=params, headers=self.headers)
        response.raise_for_status()
