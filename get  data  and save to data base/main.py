# added module
import pprint
import sqlite3

import requests

# create database connection and table
conn = sqlite3.connect("./mydatabase.db")
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS forecast(id INTEGER PRIMARY KEY AUTOINCREMENT, latitude REAL, longitude REAL , datetime TEXT, temperature REAL, humidity INTEGER)"
)
conn.commit()


def insert_into_db(latitude, longitude, datetime, temperature, humidity):
    entity = [
        latitude,
        longitude,
        timeseries_list[index],
        temperature_list[index],
        humidity_list[index],
    ]
    cur.execute(
        "INSERT INTO forecast(latitude, longitude, datetime, temperature, humidity)VALUES(?,?,?,?,?)",
        entity,
    )
    conn.commit()


def insert_into_db_bulk(entities):
    cur.executemany(
        "INSERT INTO forecast(latitude, longitude, datetime, temperature, humidity)VALUES(?,?,?,?,?)",
        entities,
    )
    conn.commit()


# function to get forecast data from open meteo for 7 days in hourly time
def get_forecast_state(latitude, longitude):
    # url and fetch data
    url = "https://api.open-meteo.com/v1/forecast"

    # variable
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m",
    }

    # results query
    response = requests.get(url, params=params)
    return response.json()


# code variables
latitude = 52.52
longitude = 13.41

if __name__ == "__main__":
    # fetching data   and separating to each value as list
    data = get_forecast_state(52.52, 13.41)
    # testing print how to show data
    # pprint.pprint(data,width=4)
    timeseries_list = data["hourly"]["time"]
    temperature_list = data["hourly"]["temperature_2m"]
    humidity_list = data["hourly"]["relative_humidity_2m"]

    result_data = []
    # iterating over data to insert into database
    for index, item in enumerate(timeseries_list):
        # print(item,timeseries_list[index],temperature_list[index],humidity_list[index])
        # for fetch one
        # insert_into_db(latitude,longitude,timeseries_list[index],temperature_list[index],humidity_list[index])
        # for fetch all
        result_data.append(
            [
                latitude,
                longitude,
                timeseries_list[index],
                temperature_list[index],
                humidity_list[index],
            ]
        )
    insert_into_db_bulk(result_data)
