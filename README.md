# Weather App GUH

Overview:

Weather App GUH is a weather application built using Python, the Django framework, the OpenWeather API, and the Google Custom Search API. The app provides current weather information and an image of a city specified by the user.

Requirements:

Python

Django

APIs Used

OpenWeather API:

OpenWeather API provides global weather data, including current conditions, forecasts, and historical data. This project utilizes the "Current Weather Data" API to fetch weather details for a specified city. To use the API, sign up at OpenWeather, create an account, and generate an API key. Use the following URL format for requests:

https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

Google Custom Search API:

The Google Custom Search API allows for searching and retrieving images related to a specific city. To set up the API, follow these steps:

1. Obtain an API key from Google Developers (https://developers.google.com/custom-search/v1/introduction).

2. Create a custom search engine at Programmable Search Engine (https://programmablesearchengine.google.com/)

3. Configure the search engine to "Search the entire web" to get relevant images. Copy the unique identifier (17 characters) from the search engine URL after the cx= parameter.

Usage:

1. Install the required dependencies (Python and Django).

2. Set up your OpenWeather and Google Custom Search API keys in the project.

3. Run the Django server and access the app to enter a city name and get weather information and an image.

Thank you for checking out this project! Your interest and support are greatly appreciated.
