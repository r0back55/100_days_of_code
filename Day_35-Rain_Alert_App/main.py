import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests

account_sid = ""
auth_token = ""


OpenWeatherEndpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_API_KEY = ""
MY_LAT = 52.229675
MY_LON = 21.012230


parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": MY_API_KEY,
    "cnt": 4,
}

response = requests.get(url=OpenWeatherEndpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain. Take an umbrella!",
        from_="+",
        to="+",
    )

    print(message.status)
