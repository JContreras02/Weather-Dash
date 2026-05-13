import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather(city_id):
    url = f"https://api.openweathermap.org/data/2.5/weather?units=imperial&q={city_id}&appid={API_KEY}"
    response = (requests.get(url))
    data = response.json()
    temp = round(data["main"]["temp"])
    humid = round(data["main"]["humidity"])
    feels_like = round(data["main"]["feels_like"])

    print(f"The current weather in {city_id} is {temp} degrees.")

    if temp == feels_like:
        print(f"Feels like the actual temperature.")
    elif temp >= feels_like:
        print(f"Feels higher than actual temperature at {feels_like}.")
    elif temp <= feels_like:
        print(f"Feels lower than actual temperature at {feels_like}.")
    else:
        print(f"Failed to compare to actual temp.")

    print(f"The current humidity is {humid}%\n")

print("\nWelcome to Jonathan's Weather App!")
print("----------------------------------------------")
city_id = input("Input a city: ")
print("\n")

get_weather(city_id)
