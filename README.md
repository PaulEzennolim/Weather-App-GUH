# Weather App GUH

## Overview:

Weather App GUH is a weather application built using Python, the Django framework, the OpenWeather API, and the Google Custom Search API. The app provides current weather information and an image of a city specified by the user.

## Requirements:

* Python

* Django

## Setup and Installation

1. Open a command prompt/terminal.

2. Navigate to the desired directory where you want to place the project.

3. Create a Django project and start a new app:

django-admin startproject yourprojectname

cd yourprojectname

django-admin startproject yourprojectoperationname

4. Configure settings:
In settings.py, add yourprojectoperationname to the INSTALLED_APPS list.

5. Run the development server:
python manage.py runserver

6. Access the application:
Click on the URL provided in the terminal (usually http://127.0.0.1:8000/) to open the application in your web browser.

## APIs Used

### OpenWeather API:

OpenWeather API provides global weather data, including current conditions, forecasts, and historical data. This project utilizes the "Current Weather Data" API to fetch weather details for a specified city. To use the API, sign up at OpenWeather, create an account, and generate an API key. Use the following URL format for requests:

https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

## Google Custom Search API:

The Google Custom Search API allows for searching and retrieving images related to a specific city. To set up the API, follow these steps:

1. Obtain an API key from Google Developers (https://developers.google.com/custom-search/v1/introduction).

2. Create a custom search engine at Programmable Search Engine (https://programmablesearchengine.google.com/)

3. Configure the search engine to "Search the entire web" to get relevant images. Copy the unique identifier (17 characters) from the search engine URL after the cx= parameter.

## Usage:

1. Install the required dependencies (Python and Django).

2. Set up your OpenWeather and Google Custom Search API keys in the project.

3. Run the Django server and access the app to enter a city name and get weather information and an image.

Thank you for taking the time to check out this project!
