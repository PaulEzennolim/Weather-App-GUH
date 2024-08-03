"""
views.py handles HTTP requests and returns HTTP responses, such as HTML documents. 
All application-specific view functions are defined here.
"""

from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Home view function
def home(request):
    # Get the city from POST request; default to 'Manchester' if not provided
    if 'city' in request.POST:
        city = request.POST['city']
    else:  # Default city
        city = 'Manchester'
    
    # APIs to fetch weather and city image information
    # OpenWeatherMap API
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=' # Weather API 

    # Google Custom Search API
    API_KEY = '' # Your API key
    SEARCH_ENGINE_ID = '' # Your search engine ID
    query = f"{city} 1920x1080"
    start = 1  # Start index for results
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    # Get city image URL from Google Custom Search API
    data = requests.get(city_url).json()
    search_items = data.get("items")
    image_url = search_items[1]['link'] if search_items and len(search_items) > 1 else None

    # Parameters to fetch weather data in metric units (Celsius)
    PARAMS = {'units': 'metric'}  

    try:
        data = requests.get(weather_url, params=PARAMS).json() # Fetch weather data
        description = data['weather'][0]['description'] # Weather description
        icon = data['weather'][0]['icon'] # Weather icon
        temp = data['main']['temp'] # Temperature
        day = datetime.date.today() # Today's date

        # Render the template with the weather and city data
        return render(request, 'index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url
        })
    
    except KeyError:
        """
        Handle the case where the city data is not available (KeyError).
        Display an error message and default weather data.
        """
        exception_occurred = True
        messages.error(request, 'The entered data is not available to the API')
        day = datetime.date.today()
        return render(request, 'index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'Manchester',
            'exception_occurred': exception_occurred
        })
