# Weather

## Description

### User story:
As an API user I want to get min, max, average and median temperature and humidity
for given city and period of time.

### Requirements:
- Use git for version control
- Publish on GitHub or send us a compressed repo
- Functionality
  - Create locally running RESTful web API
    - django-rest-framework recommended, though not necessary
  - that accepts a request with 'city' and 'period' args
  - fetches weather data for that location and period of time from some public API
    - e.g. Yahoo! Weather
  - computes min, max, average and median temperature and humidity
    for that location and period and returns that to the user.

### Extra goals:
- Provide a view which renders a bar chart for the requested data.
- Deploy it somewhere.


## Local development

### Installation

1. Download the project 
  - `$ git clone https://github.com/BibianaC/weather.git`
2. Install dependencies
  - `pip install -r requirements.txt`
  - `pip install -r requirements.test`
3. Set up external weather api
  - Signup for a free API key [on the OWM website](https://home.openweathermap.org/users/sign_up)
    - Create `settings.py` with the `API key`
      - `$ echo "WEATHER_API_KEY = 'your OWM key'" > settings.py`

### Run

- Server `$ python manage.py runserver`
  - url `localhost/api/v0/weather/City,country/days/`
    - Example: `localhost:8000/api/v0/weather/London,uk/7/`
    - Maximum quantity of days is 7.
- Tests `$ py.test`
