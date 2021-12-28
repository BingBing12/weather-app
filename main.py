import requests
import keys
import smtplib

keys = keys.Keys()

weather_params = {
    "lat": keys.lat,
    "lon": keys.lon,
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
for hour in range(12):
    if weather[hour] < 700:
        bring_umbrella = True

if bring_umbrella:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=keys.email, password=keys.password)
        connection.sendmail(
            from_addr=keys.email,
            to_addrs=keys.email,
            msg=f'Subject:RAIN ALERT\n\nIts going to rain, remember to bring an umbrella!'
        )
