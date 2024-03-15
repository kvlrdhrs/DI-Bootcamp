import pyowm
from pyowm.owm import OWM
import datetime

owm = pyowm.OWM('d35ad205557efdb73e6cd4a2319da30b')  # You MUST provide a valid API key

def get_weather(city):
    obs = owm.weather_at_place(city)
    w = obs.get_weather()

    print(f"Weather in {city}:")
    print(f"  Status: {w.get_status()}")
    print(f"  Temperature: {w.get_temperature('celsius')['temp']}°C")
    print(f"  Wind Speed: {w.get_wind()['speed']} m/s")

def get_sunrise_sunset(city):
    obs = owm.weather_at_place(city)
    w = obs.get_weather()

    sunrise_time = datetime.datetime.fromtimestamp(w.get_sunrise_time())
    sunset_time = datetime.datetime.fromtimestamp(w.get_sunset_time())

    print(f"Sunrise and sunset in {city}:")
    print(f"  Sunrise: {sunrise_time}")
    print(f"  Sunset: {sunset_time}")

def get_forecast(city):
    fc = owm.three_hours_forecast(city)
    f = fc.get_forecast()

    print(f"Forecast for {city}:")
    for weather in f:
        print(f"  {weather.get_reference_time('iso')} - {weather.get_status()}")

def get_pollution(city):
    obs = owm.weather_at_place(city)
    l = obs.get_location()
    co = owm.coindex_around_coords(l.get_lat(), l.get_lon())
    print(f"Air pollution in {city}: {co.get_co_samples()}")

city = input("Enter a city: ")
get_weather(city)
get_sunrise_sunset(city)
get_forecast(city)
get_pollution(city)



