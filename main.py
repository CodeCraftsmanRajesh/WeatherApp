from tkinter import *
import requests
import json
from datetime import datetime

BUTTON = 'roboto 10'
FONT = 'roboto 12 bold'
SKY_COLOR = '#87CEEB'
YELLOW = '#FFFF00'

app = Tk()
app.geometry("400x400")  # size of the window by default
app.resizable(False, False)  # to make the window size fixed

app.config(bg=SKY_COLOR)
# title of our window
app.title("Weather App")

city_value = StringVar()


def showWeather():
    api_key = "5039329773942e3e521f5e93093301b0"  # sample API
    city_name = city_value.get()

    # API url
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    # Get the response from fetched url
    response = requests.get(weather_url)

    # changing response from json to python readable
    weather_info = response.json()

    tfield.delete("1.0", "end")  # to clear the text field for every new output

    # as per API documentation, if the cod is 200, it means that weather data was successfully fetched

    if weather_info['cod'] == 200:
        kelvin = 273  # value of kelvin

        # -----------Storing the fetched values of weather of a city

        temp = int(weather_info['main']['temp'] - kelvin)  # converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        # assigning Values to our weather variable, to display as output

        weather = (f"\nWeather of: {city_name}"
                   f"\nTemperature (Celsius): {temp}°"
                   f"\nFeels like in (Celsius): {feels_like_temp}°"
                   f"\nPressure: {pressure} hPa"
                   f"\nHumidity: {humidity}%"
                   f"\nSunrise at: {sunrise_time}"
                   f"\nSunset at: {sunset_time}"
                   f"\nWind speed: {wind_speed}"
                   f"\nCloud: {cloudy}%"
                   f"\nInfo: {description}")
    else:
        weather = (f"\n\tWeather for '{city_name}' not found!"
                   f"\n\tKindly Enter valid City Name !!")

    tfield.insert(INSERT, weather)  # to insert or send value in our Text Field to display output


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


# to generate label heading
Label(app, text='Enter City Name',
      font=FONT, bg=SKY_COLOR).pack(pady=10)

# entry field
Entry(app, textvariable=city_value, width=24, font=FONT, justify="center").pack()

Button(app, command=showWeather, text="Check Weather", font=BUTTON, bg='Green', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

Label(app, text="The Weather is: ", font=FONT, bg=SKY_COLOR).pack(pady=10)

tfield = Text(app, width=50, height=12, bg=YELLOW, font='roboto 9')
tfield.pack()

app.mainloop()
