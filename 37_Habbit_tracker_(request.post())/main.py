import requests
from datetime import datetime
USERNAME = 'viktorsito'
TOKEN = "kjsdfiwei93245o1"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

# Creating graph
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Min",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Add value to the tracker
new_pixel_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# today = datetime(year=2021, month=5, day=18)
today = datetime.now()
today = today.strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": input("How long did you code today: "),
}

response2 = requests.post(url=new_pixel_end_point, json=pixel_config, headers=headers)

new_config = {
    "quantity": "60",
}
print(response2.text)
# Update value
# update_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response3 = requests.put(url=update_end_point, json=new_config, headers=headers)

# Delete value
# delete_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response4 = requests.delete(delete_end_point, headers=headers)
# print(response4.text)
