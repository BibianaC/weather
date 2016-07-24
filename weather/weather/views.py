import numpy
from pyowm import OWM

from rest_framework.decorators import api_view
from rest_framework.response import Response

from settings import WEATHER_API_KEY


def average(list_num):
    avg = numpy.mean(list_num)
    return round(avg, 2)


def median(list_num):
    median = numpy.median(list_num)
    return round(median, 2)


def temperature(day_temp):
    min_temp = day_temp['min']
    max_temp = day_temp['max']
    avg_temp = average([min_temp, max_temp])
    temperature = {'min': min_temp, 'max': max_temp, 'avg': avg_temp}
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


def daily_fcst_data(forecast):
    daily_min = []
    daily_max = []
    daily_avg = []
    daily_humidity = []

    for info in forecast:
        temperature = info['temperature']
        daily_min.append(temperature['min'])
        daily_max.append(temperature['max'])
        daily_avg.append(temperature['avg'])
        daily_humidity.append(info['humidity'])

    return daily_min, daily_max, daily_avg, daily_humidity


def aggreagate(forecast):
    daily_min, daily_max, daily_avg, daily_humidity = daily_fcst_data(forecast)
    aggregated = {
        'min': min(daily_min),
        'max': max(daily_max),
        'min_avg': average(daily_min),
        'max_avg': average(daily_max),
        'avg': average(daily_avg),
        'min_median': median(daily_min),
        'max_median': median(daily_max),
        'median': median(daily_avg),
        'min_humidity': min(daily_humidity),
        'max_humidity': max(daily_humidity),
        'avg_humidity': average(daily_humidity),
        'median_humidity': median(daily_humidity),
    }

    return aggregated


def weather_info(location, days):
    forecast = get_forecast(location, days)
    aggregated = aggreagate(forecast)
    weather = {
        'daily_forecast': forecast,
        'aggregated': aggregated,
    }
    return weather


@api_view(['GET'])
def weather(request, location, days_str):
    days = int(days_str)
    return Response(weather_info(location, days))
