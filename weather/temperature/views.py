from django.shortcuts import render
import json, random
import urllib.request  
from urllib.request import Request, urlopen
from datetime import datetime

def index(request):
    if request.method == 'POST':
        city = request.POST['searchQueryInput']
    else:
        # generate a random city to display its info, if it's a get request
        req = Request(
        url='https://countriesnow.space/api/v0.1/countries', headers={'User-Agent': 'Mozilla/5.0'})
        country_cities_api = urlopen(req).read()
        all_data = json.loads(country_cities_api)
        cities = []
        for i in all_data['data']:
            for a,b in i.items():
                if a == 'cities':
                    for y in b:
                        cities.append(y)
        city = random.choice(cities)

    weather_api = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q='
                + city + '&appid=make_sure_to_add_your_unique_api_key_here').read()
    data = {}
    temp_data = json.loads(weather_api)
    temp_in_kelvin = str(temp_data['main']['temp']) + ' K'
    temp_in_celcius = str(round((temp_data['main']['temp'] -  273.15),2))
    temp_in_fahrenheit = str(round((((temp_data['main']['temp'] -  273.15) * 9/5) + 32),2))
    data['temp_in_celcius'] = temp_in_celcius  
    data['temp_in_fahrenheit'] = temp_in_fahrenheit 
    city_country_code = temp_data['sys']['country']
    for i in temp_data['weather']:
        atmosphere = i.get('main')
    atm_pressure = str(temp_data['main']['pressure']) + 'Pa'
    humidity = str(temp_data['main']['humidity'])  + '%' 
    wind_speed = str(temp_data['wind']['speed']) + 'm/s'
    data['atmosphere'] = atmosphere 
    data['atm_pressure'] = atm_pressure 
    data['humidity'] = humidity 
    data['wind_speed'] = wind_speed 
    req = Request(
    url='https://countriesnow.space/api/v0.1/countries/iso', headers={'User-Agent': 'Mozilla/5.0'})
    country_codes_api = urlopen(req).read()
    country_data = json.loads(country_codes_api)
    for i in country_data['data']:
        for a,b in i.items():
            if b == city_country_code:
                city_country = i.get('name')
    now = datetime.now()
    today_date = datetime.now().strftime("%d/%m/%Y")
    today_time = now.strftime("%H:%M:%S")
    weekday = now.strftime('%A')
    data['today_date'] = today_date
    data['today_time'] = today_time
    data['weekday'] = weekday
    data['country'] = city_country
    data['city'] = city.capitalize()

    return render(request, "index.html", data)