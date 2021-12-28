import requests
import datetime
import keys

keys = keys.Keys()

weather_params = {
    "lat": -33.918861,
    "lon": 18.423300,
    "appid": keys.api_key,
    "exclude": "current,minutely,daily"
}
endpoint = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
hourly_weather = weather_data["hourly"]
bring_umbrella = False
weather = [hour["weather"][0]["id"] for hour in hourly_weather]
for hour in range(8):
    if weather[hour] < 700:
        bring_umbrella = True

print(bring_umbrella)
print(weather)
time_hour = f"{datetime.datetime.now()}".split(" ")[1].split(":")[0]
print(time_hour)