from django.shortcuts import render
import requests
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=480dc4bb43512f39def7b2db34d39522'
    city = 'Leeds'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types


    # city_weather.temp = (city_weather.temp - 32) * 5/9

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
    }


    temperature = city_weather['main']['temp']
    temperature = (temperature - 32) * 5/9
    print(temperature)

    context = {'weather' : weather}

    print(weather)



    return render(request, 'home.html')