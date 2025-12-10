from current_temp_api.api import OpenMeteo, Openweather

open_meteo_obj = OpenMeteo(35.69, 51.42)
temp = open_meteo_obj.get_current_temperature()
print(temp)

open_weather_obj = Openweather(
    35.69, 51.42, api_token="2a80acae8fbb29d9da2ea5962c852b15"
)
temp = open_weather_obj.get_current_temperature()
print(temp)
