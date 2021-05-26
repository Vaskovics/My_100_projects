import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/fb47302bc410dd77ba48c369e6881ced/flightDeals/лист1"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["лист1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode":["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)