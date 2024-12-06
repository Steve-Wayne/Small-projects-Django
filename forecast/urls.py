# forecast/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_home, name='weather_home'),
    path('search/', views.weather_search, name='weather_search'),
    path('get_weather_data/', views.get_weather_data, name='get_weather_data'),
]
