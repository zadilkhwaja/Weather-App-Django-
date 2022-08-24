from django.shortcuts import render
import json
import urllib.request  #to make request to api

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        source = urllib.request.urlopen(
             'https://api.openweathermap.org/data/2.5/weather?q='
                    + city + '&appid=c94f9a8e774eb330e946d1ac1648f220').read()

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
