from django.shortcuts import render
from django.conf import settings
import requests
# Create your views here.

def weather_home(request):
    weather_data = None
    city = request.GET.get('city', 'New York')  # Default city
    if city:
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHER_API_KEY}&units=metric"
        response = requests.get(api_url)
        if response.status_code == 200:
            weather_data = response.json()
    return render(request, 'forecast/home.html', {'weather_data': weather_data, 'city': city})



from django.http import JsonResponse


def get_weather_data(request):
    country = request.GET.get('country')
    api_key = settings.WEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return JsonResponse({
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        })
    else:
        return JsonResponse({'error': 'Unable to fetch weather data'}, status=400)


def weather_search(request):
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = settings.WEATHER_API_KEY
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
        else:
            weather = None
        return render(request, 'forecast/home.html', {'weather': weather})
    return render(request, 'forecast/home.html')
