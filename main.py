import requests

api_key = "you_api_goes_here"

parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": ['current', "minutely", "daily"]
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
data = weather_data['hourly'][0]["weather"][0]["id"]
all_id = []

for i in range(0, 13):
    ids = weather_data['hourly'][i]["weather"][0]["id"]
    all_id.append(ids)
print(data)
print(all_id)

is_rain = False
for _ in all_id:
    if _ > 700:
        is_rain = True
    else:
        is_rain = False

if is_rain:
    print("Bring Ambralla")
