import numpy
from pyowm import OWM

from rest_framework.decorators import api_view
from rest_framework.response import Response

from settings import WEATHER_API_KEY


location = 'London,uk'


def temperature(temperature_data):
    print temperature_data
    min_temp = temperature_data['min']
    max_temp = temperature_data['max']
    avg_temp = numpy.mean([min_temp, max_temp])
    avg_round = round(avg_temp, 2)
    temperature = {'min': min_temp, 'max': max_temp, 'avg': avg_round}
    return temperature


def get_weather(location, days=7):
    owm = OWM(WEATHER_API_KEY)
    forecast = owm.daily_forecast(location, limit=days)
    get_forecast = forecast.get_forecast()

    weather = []
    for info in get_forecast:
        day = info.get_reference_time('iso')
        humidity = info.get_humidity()
        temp_info = info.get_temperature('celsius')
        temp = temperature(temp_info)
        weather.append({
            'day': day,
            'humidity': humidity,
            'temperature': temp,
        })

    return weather


@api_view(['GET'])
def weather(request):
    return Response(get_weather(location, 7))
