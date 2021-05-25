import requests
import datetime


APP_ID = "162ecb6a"
API_KEY = "a6c75c50a7bc905b7f7c52bcac347122"

GENDER = "male"
WEIGHT_KG = "85"
HEIGHT_CM = "201"
AGE = "31"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("What exercises have you done: ")

parameters = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

response = requests.post(exercise_end_point, json=parameters, headers=headers)
data = response.json()
print(data)

ADD_ROW_API = "https://api.sheety.co/fb47302bc410dd77ba48c369e6881ced/workout/лист1"
today = datetime.datetime.now()
today_date = today.strftime("%d/%m/%Y")

time = today.strftime("%H:%M:%S")


duration = data["exercises"][0]["duration_min"]
print(duration)
calories = data["exercises"][0]["nf_calories"]
print(calories)

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(ADD_ROW_API, json=sheet_inputs)

    print(sheet_response.text)