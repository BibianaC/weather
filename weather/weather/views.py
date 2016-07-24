import numpy
from pyowm import OWM

from rest_framework.decorators import api_view
from rest_framework.response import Response

from settings import WEATHER_API_KEY


def temperature(day_temp):
    min_temp = day_temp['min']
    max_temp = day_temp['max']
    avg_temp = numpy.mean([min_temp, max_temp])
    avg_round = round(avg_temp, 2)
    temperature = {'min': min_temp, 'max': max_temp, 'avg': avg_round}
    return temperature


def forecast(forecast_data):
    forecast = []
    for day_weather in forecast_data:
        day = day_weather.get_reference_time('iso')
        humidity = day_weather.get_humidity()
        day_temp = day_weather.get_temperature('celsius')
        temp = temperature(day_temp)
        forecast.append({
            'day': day,
            'humidity': humidity,
            'temperature': temp,
        })

    return forecast


def get_forecast(location, days):
    owm = OWM(WEATHER_API_KEY)
    daily_forecast = owm.daily_forecast(location, limit=days)
    forecast_data = daily_forecast.get_forecast()
    return forecast(forecast_data)


def weather_info(location, days):
    forecast = get_forecast(location, days)
    return forecast


@api_view(['GET'])
def weather(request, location, days_str):
    days = int(days_str)
    return Response(weather_info(location, days))
