import requests
from twilio.rest import Client


api_key = "5f1dff1338f7050a5c5ad1c7893101ac"
my_lat = "51.507351"
my_lon = "-0.127758"
account_sid = "ACfb14f346953d61ac3759ace3638dde53"
auth_token = "96d74541092d27e7f3c3952c4eb12f5c"
my_number = "+13519998463"

parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data['hourly'][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]['id'])
    print(condition_code)
    if int(condition_code) < 700:
        print("Bring an umbrella")
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Please bring an umbrella, is going to rain.",
        from_='+13519998463',
        to='+447472427254'
    )
    print(message.status)

