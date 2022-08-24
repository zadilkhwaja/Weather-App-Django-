from django.shortcuts import render
import json
import urllib.request  #to make request to api

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen(
             'https://api.openweathermap.org/data/2.5/weather?q='
                    + city + '&appid=e8a821ce2c56f63bb0dad3efddb93dba').read()

        temp_data = json.loads(source)

        data = {
            "temp": str(temp_data['main']['temp']) + ' K',
        }
        print(data)
    else:
        data={ }
    return render(request, "index.html", data)