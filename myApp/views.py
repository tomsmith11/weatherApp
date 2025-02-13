from django.shortcuts import render
import requests
import logging
from .models import City
from .forms import CityForm

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=480dc4bb43512f39def7b2db34d39522'

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    
    for city in cities:
        city_weather = requests.get(url.format(city.name)).json()  # request the API data and convert the JSON to Python data types
        weather = {
            'city': city.name,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }
        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'home.html', context)

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=480dc4bb43512f39def7b2db34d39522'
    form = CityForm()
    cities = City.objects.all()  # return all the cities in the database

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate

    form = CityForm()

    weather_data = []
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'home.html', context)