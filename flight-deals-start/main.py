from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheet_data_manager = DataManager()
sheet_data = sheet_data_manager.sheety_get_response()
flight_data_manager = FlightData()
#
# pprint(sheet_data['prices'])

for row in sheet_data['prices']:
    if row['iataCode'] == '':
        flight_search = FlightSearch(city=row["city"])
        location = flight_search.get_location()
        row["iataCode"] = location["locations"][0]["code"]
        sheet_data_manager.sheety_put_request(row["iataCode"], row["id"])
    else:
        pass

    # pprint(flight_data_manager.search_flights(row["iataCode"]))
flight_search_manager = FlightSearch(city=row["city"])
print(flight_search_manager.get_flights())
