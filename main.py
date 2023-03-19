import requests
import os
from datetime import datetime

GENDER    = "female"
WEIGHT_KG = "60"
HEIGHT_CM = "170"
AGE       = "22"
TOKEN     = os.environ.get("TOKEN")

NUTRITION_APP_ID  = os.environ.get("NUTRITION_APP_ID")
NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint    = "https://api.sheety.co/32f67aa8343d6984c3f94fba5340b51e/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

nutrition_headers = {
      "x-app-id": NUTRITION_APP_ID,
      "x-app-key": NUTRITION_API_KEY,
      "Content-Type": "application/json",
}

nutrition_params = {
      "query": exercise_text,
      "gender": GENDER,
      "weight_kg": WEIGHT_KG,
      "height_cm": HEIGHT_CM,
      "age": AGE,
}

exercise_response = requests.post(exercise_endpoint, json=nutrition_params, headers=nutrition_headers)
result            = exercise_response.json()


for exercise in result["exercises"]:
   sheet_inputs = {
         "workout": {
      "date": datetime.today().strftime("%d/%m/%Y"),
      "time": datetime.today().strftime("%X"),
      "exercise": exercise["name"].title(),
      "duration": exercise["duration_min"],
      "calories": exercise["nf_calories"],
         }
   }

bearer_headers = {
"Authorization": "Bearer " + TOKEN
}

sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)

print(sheet_response.json())