# Weather Data Generator Application
# Author Kiana Gonzalez-Rodholm
# 11/19/2020
# This program is meant to open a weather webservice and will display weather results depending on the user input.
# The user is asked to input a city or zip code and the appropriate weather information will display.

import requests
import json

# The following is my unique API key from the website and the country code variable is set to US.
api_key = '584f7926af16e44b0d6d567e6ab3ebff'
country_code = 'us'


# This function reads the user inputted zip code, calls the API with a get request and retrieves weather data.
def read_zip(zip_code):
    # This is the API call from the website which is specific to zip codes.
    url1 = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&units=imperial&appid={api_key}'

    # This try/except statement will catch any exceptions or issues with retrieving the data.
    try:
        response = requests.get(url1)   # get request using the requests library
        data1 = response.text
        json_data1 = json.loads(data1)  # processes the data into json data in order to print the results properly

        # The following if statement will run the display function as long as the error code is not 404.
        if json_data1['cod'] != '404':
            display_info(json_data1)
            print("Data request processed successfully.\n")
        # If the error code is 404 then the location is not in the database and the print statement will display.
        else:
            print('Location not found. Please try again.\n')

    except:
        print('Data requested processed incorrectly. HTTP error.\n')


# This function reads the user inputted city and state, calls the API with a get request and retrieves weather data.
def read_city(city, state):
    # This is the API call from the website which is specific to city name.
    url2 = f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country_code}&units=imperial&appid={api_key}'

    # The following if statement will run the display function as long as the error code is not 404.
    try:
        response = requests.get(url2)       # get request using the requests library
        data2 = response.text
        json_data2 = json.loads(data2)      # processes the data into json data in order to print the results properly

        # The following if statement will run the display function as long as the error code is not 404.
        if json_data2['cod'] != '404':
            display_info(json_data2)
            print("Data request processed successfully.\n")
        # If the error code is 404 then the location is not in the database and the print statement will display.
        else:
            print('Location not found. Please try again.\n')

    except:
        print('Data requested processed incorrectly. HTTP error.')


# The following function sets variables for each element of wanted data, and then prints each result.
def display_info(data):
    weather = data['main']
    current_temp = weather['temp']
    temp_max = weather['temp_max']
    temp_min = weather['temp_min']
    pressure = weather['pressure']
    humidity = weather['humidity']
    report = data['weather']
    # An index is needed here since the 'weather' dictionary key has a value which is a list.
    description = report[0]['description']
    city_name = data['name']
    clouds = data['clouds']
    cloud_percentage = clouds['all']
    print(f'{city_name:-^30}')              # special formatting which centers city name and adds dashes
    print(f'Current temperature: {current_temp}\u00b0 fahrenheit')    # \u00b0 is a code to display the degrees symbol
    print(f'Maximum temperature: {temp_max}\u00b0 fahrenheit')
    print(f'Minimum temperature: {temp_min}\u00b0 fahrenheit')
    print(f'Pressure: {pressure} hPa')
    print(f'Humidity: {humidity}%')
    print(f'Weather Report: {description}')
    print(f'Cloudiness: {cloud_percentage}%')


# The following is the main function which asks for the user to input a zip code or city and calls the read functions.
def main():
    print('Hello and welcome to the weather app!')

    # This while loop will keep giving the user weather data until the user types 'done' and ends the program.
    while True:
        zip_city = input("Please enter a zip code or city name. Type 'zip' or 'city'.\n"
                         "When you are done type 'done'.\n").lower()       # defaults input to all lowercase regardless

        # If the user types 'done' then the loop breaks and the program ends.
        if zip_city == 'done':
            print('Have a nice day!')
            break
        # If the user types 'zip' then the program retrieves the zip code and calls the read_zip function.
        elif zip_city == 'zip':
            user_input = input('Please enter the zip code (US only).\n')
            read_zip(user_input)
        # If the user types 'city' then the program retrieves the city and state code and calls the read_city function.
        elif zip_city == 'city':
            user_input = input('Please enter the city name.\n').lower()                 # defaults input to lowercase
            state_input = input('Please enter the state code (US only).\n').upper()     # defaults input to uppercase
            read_city(user_input, state_input)
        # If the user doesn't type 'zip' or 'city' a print statement is displayed and the loop starts over.
        else:
            print("Please enter 'zip' or 'city'.\n")
            continue


# This is the standard call statement that will run the program as long as this is the original (non-imported) file.
if __name__ == "__main__":
    main()
