from django.shortcuts import render
import json
import urllib.request  #to make request to api

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        source = urllib.request.urlopen(
             'https://api.openweathermap.org/data/2.5/weather?q='
                    + city + '&appid=make_sure_to_add_your_unique_api_key_here').read()

        temp_data = json.loads(source)
        temp_in_kelvin = str(temp_data['main']['temp']) + ' K'
        temp_in_celcius = str(round((temp_data['main']['temp'] -  273.15),2)) + ' C'
        data = {
            "temp": temp_in_kelvin + ' / ' + temp_in_celcius
        }
        print(data)
    else:
        data={ }
    return render(request, "index.html", data)
