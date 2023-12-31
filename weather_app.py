import requests

api_key = '77ef3634493c5783a105857309f0e4f8'

user_input = input("Enter city: ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
print(weather_data.json())