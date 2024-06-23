import requests
from datetime import datetime


# ISS Tracker
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["latitude"]
# latitude = data["iss_position"]["longitude"]
# iss_position = (longitude, latitude)
# print(iss_position)


# Sunrise and Sunset check
MY_LAT = 52.229675
MY_LNG = 21.012230
MY_TZID = "Europe/Warsaw"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "tzid": MY_TZID,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
sunset = data["results"]["sunset"].split("T")[1].split("+")[0]

time_now = datetime.now()

print(sunrise)
print(sunset)
