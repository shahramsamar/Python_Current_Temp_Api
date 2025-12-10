
# this file contains inheritance, polymorphism, abstraction without encapsulation
 

import pprint
from abc import ABC, abstractmethod

import requests


class WeatherAbstract(ABC):
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    @abstractmethod
    def get_forecast_temp_hum(self):
        pass
    
    @abstractmethod
    def get_current_temp_hum(self):
        pass
   

class OpenMeteoStation(WeatherAbstract):
        
    def get_forecast_temp_hum(self):
        url = 'https://api.open-meteo.com/v1/forecast'
        params ={
            'latitude':  self.latitude ,
            'longitude': self.longitude ,
            'hourly':['temperature_2m','relative_humidity_2m']
        }
        data = requests.get(url, params=params)
        response = data.json()
        return response
    
    def get_current_temp_hum(self):
        url = 'https://api.open-meteo.com/v1/forecast'
        params ={
            'latitude':  self.latitude ,
            'longitude': self.longitude ,
            'current':['temperature_2m','relative_humidity_2m'] 
        }
        data = requests.get(url, params=params)
        response = data.json()
        return response
    

    
 
    def display_forecast(client):
            print('OpenMeteoStation forecast_temp_hum .....')
            time = client.get_forecast_temp_hum()['hourly']['time']
            temperature = client.get_forecast_temp_hum()['hourly']['temperature_2m']
            relative_humidity = client.get_forecast_temp_hum()['hourly']['relative_humidity_2m']

            for index, Weather in enumerate(time):
                print(index,'time: ',time[index],"_",'temperature: ',temperature[index],"_",'relative_humidity: ',relative_humidity[index])
    
    
    def display_current(client):
        print('OpenMeteoStation current_temp_hum .....')
        temperature = client.get_current_temp_hum()['current']['temperature_2m']
        relative_humidity = client.get_current_temp_hum()['current']['relative_humidity_2m']
        return f"temperature: {temperature} , relative_humidity: {relative_humidity}"


    
class OpenWeatherStation(WeatherAbstract):
    
    def get_forecast_temp_hum(self):
        url = 'https://api.openweathermap.org/data/2.5/forecast'
        API_key ="00e7ad1f702afa36c308e10a55cba3ef"
        cnt = 16 # 1 ot 16
        units = 'metric' # Celsius - # imperial - Fahrenheit # standard
        params ={
            'lat':  self.latitude ,
            'lon': self.longitude ,
            'cnt': cnt ,
            'appid': API_key ,
            'units': units 
        }
        data = requests.get(url, params=params)
        response = data.json()
        return response

    def get_current_temp_hum(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?'
        API_key ="00e7ad1f702afa36c308e10a55cba3ef"
        units = 'metric'
        params ={
            'lat':  self.latitude ,
            'lon': self.longitude ,
            'appid': API_key ,
            'units': units
        }
        data = requests.get(url, params=params)
        response = data.json()
        return response

    def display_forecast(client):
            print('OpenWeatherStation forecast_temp_hum .....')
            # data = Weather_OpenWeatherStation.get_forecast_temp_hum()['list'][0]
            data = client.get_forecast_temp_hum()['list']
            # print(data)
            for item, day in enumerate(data):
                print(item,"-",'forecast_time:',data[item]['dt_txt'],"-",'forecast_temp:',
                    data[item]['main']['temp'],"-",'forecast_humidity:',data[item]['main']['humidity'])
                
    def display_current(client):
        print('OpenWeatherStation current_temp_hum .....')
        temperature = client.get_current_temp_hum()['main']['temp']
        humidity = client.get_current_temp_hum()['main']['humidity']
        return f"current_temp: {temperature} , current_humidity: {humidity}"

        
latitude = 52.52
longitude = 13.41
client = OpenMeteoStation(latitude,longitude)
for   client.display_current()in client :
    client.display_current()
