import requests
import json
import datetime
from decouple import config

#FUNCS
def getName(host):
    name = host['name']
    return name

def getTemperature(host):
    temp = host['main']['temp']
    return temp

def getPressure(host):
    pressure = host['main']['pressure']
    return pressure

def getWeather(host):
    weathero = host['weather'][0]['main']
    return weathero


def main():
    date = datetime.datetime.now()
    name = getName(weather)
    weathero = getWeather(weather)
    temp = getTemperature(weather)
    pressure = getPressure(weather)
    print(str(date) + "\n" + str(name) + "\n"+ str(weathero) + "\n"+ str(temp) + " C\n" + str(pressure) + "hPa")

    return 0

#API

KEY = config('KEY')

url = "https://community-open-weather-map.p.rapidapi.com/weather"
querystring = {"q":"Cracow","units":"metric","mode":"XML"}
headers = {
    'x-rapidapi-key': KEY,
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params=querystring)


if response.status_code == 200:
    weather = response.json()
    main()

else:
    print("Error")