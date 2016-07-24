from weather.weather.views import aggreagate, average, median, temperature


def test_average():
    data = [18.75, 20.50, 27.01, 24.5, 26.03]
    avg = average(data)
    assert(avg) == 23.36


def test_median():
    data = [18.75, 20.50, 27.01, 24.5, 26.03]
    med = median(data)
    assert(med) == 24.5


def test_temperature():
    temp_info = {
        u'min': 18.89, u'max': 27.48, u'eve': 26.03,
        u'morn': 18.89, u'night': 20.27, u'day': 25.95}
    temp = temperature(temp_info)
    result = {'min': 18.89, 'max': 27.48, 'avg': 23.19}
    assert(temp) == result


def test_aggreagate():
    forecast = [
        {
            'day': '2016-07-24 18:00:00+00',
            'temperature': {'max': 33.1, 'avg': 29.11, 'min': 25.12},
            'humidity': 86
        },
        {
            'day': '2016-07-25 18:00:00+00',
            'temperature': {'max': 32.46, 'avg': 29.28, 'min': 26.1},
            'humidity': 84
        },
        {
            'day': '2016-07-26 18:00:00+00',
            'temperature': {'max': 31.55, 'avg': 28.19, 'min': 24.83},
            'humidity': 0
        },
    ]
    aggreagated = aggreagate(forecast)
    result = {
        'min': 24.83,
        'max': 33.1,
        'min_avg': 25.35,
        'max_avg': 32.37,
        'avg': 28.86,
        'min_median': 25.12,
        'max_median': 32.46,
        'median': 29.11,
        'min_humidity': 0,
        'max_humidity': 86,
        'avg_humidity': 56.67,
        'median_humidity': 84,
    }

    assert(aggreagated) == result
