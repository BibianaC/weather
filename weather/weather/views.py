import numpy
from pyowm import OWM

from rest_framework.decorators import api_view
from rest_framework.response import Response

from settings import WEATHER_API_KEY


location = 'London,uk'


def get_weather(location, days=7):
    owm = OWM(WEATHER_API_KEY)
    forecast = owm.daily_forecast(location, limit=days)
    get_forecast = forecast.get_forecast()

    weather = []
    for info in get_forecast:
        day = info.get_reference_time('iso')
        humidity = info.get_humidity()
        temperature = info.get_temperature('celsius')
        min_temp = temperature['min']
        max_temp = temperature['max']
        avg_temp = numpy.mean([min_temp, max_temp])
        avg_round = round(avg_temp, 2)
        weather.append({
            'day': day,
            'humidity': humidity,
            'temperature': {'min': min_temp, 'max': max_temp, 'avg': avg_round},
        })

    return weather


@api_view(['GET'])
def weather(request):
    return Response(get_weather(location, 7))
