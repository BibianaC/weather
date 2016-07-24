from weather.weather.views import temperature


def test_temperature():
    temp_info = {
        u'min': 18.89, u'max': 27.48, u'eve': 26.03,
        u'morn': 18.89, u'night': 20.27, u'day': 25.95}
    temp = temperature(temp_info)
    result = {'min': 18.89, 'max': 27.48, 'avg': 23.19}
    assert(temp) == result
