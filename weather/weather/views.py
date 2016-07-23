from pyowm import OWM

from rest_framework.decorators import api_view
from rest_framework.response import Response

from settings import WEATHER_API_KEY


location = 'London,uk'


def get_weather(location):
    owm = OWM(WEATHER_API_KEY)
    forecast = owm.daily_forecast(location)
    get_forecast = forecast.get_forecast()

    weather = []
    for info in get_forecast:
        day = info.get_reference_time('iso')
        humidity = info.get_humidity()
        temperature = info.get_temperature('celsius')
        weather.append({
            'day': day,
            'humidity': humidity,
            'temperature': temperature,
        })

    return weather


@api_view(['GET'])
def weather(request):
    return Response(get_weather(location))
