import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import Font
import ttkbootstrap as ttk
import requests


# find the weather

def getWeather():

    api_key = "e9d5bddb146b4ffc760ed7763e14d08c"

    user_input = entry.get()

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        update_text_weather("City name invalid")
        update_text_temperature(" ")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])

        update_text_weather(f"The weather in {user_input} is: {weather}")
        update_text_temperature(f"The temperature in {user_input} is: {temp}ºF")

        weather_temp_string = f"The weather in {user_input} is: {weather}"

        update_planet_text(temp, weather)

    return

def update_text_weather(text):
    result_labelw.config(text = text)

def update_text_temperature(text):
    result_labelt.config(text = text)

def update_planet_text(temperature, weather):
    if temperature <= 32 and "snow" in weather.lower():
        planet_label.config(text = "Your current weather is most similiar to the planet Hoth. \n Learn More: https://starwars.fandom.com/wiki/Hoth?so=search")
    elif temperature >= 80 and "clear" in weather.lower():
        planet_label.config(text = "Your current weather is most similiar to the planet Tatooine. \n Learn More: https://starwars.fandom.com/wiki/Tatooine")
    elif temperature > 32 and ("shower rain" in weather.lower() or "rain" in weather.lower() or "thunderstorm" in weather.lower()):
        planet_label.config(text = "Your current weather is most similiar to the planet Kamino. \n Learn More: https://starwars.fandom.com/wiki/Kamino")
    elif temperature >=55 and temperature < 80 and "clear" in weather.lower():
        planet_label.config(text = "Your current weather is most similiar to the planet Coruscant. \n Learn More: https://starwars.fandom.com/wiki/Coruscant")
    elif "clouds" in weather.lower():
        planet_label.config(text = "Your current weather is most similiar to the planet Kamino. \n Learn More: https://starwars.fandom.com/wiki/Bespin")
    elif temperature >= 90:
        planet_label.config(text = "Your current weather is most similiar to the planet Mustafar. \n Learn More: https://starwars.fandom.com/wiki/Mustafar")
    elif "mist" in weather.lower():
        planet_label.config(text = "Your current weather is most similiar to the planet Endor. \n Learn More: https://starwars.fandom.com/wiki/Endor")


#window 
window = ttk.Window(themename = "darkly")
window.title("Skywalker Weather")
window.geometry("800x500")
window.iconbitmap("skywalkerlogoico.ico")


# title
title_label = ttk.Label(master = window, text = "Skywalker Weather", font = "Comfortaa 24 bold")
title_label.pack()


#input field
input_frame = ttk.Frame(master = window)
entry_string = StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_string)
button = ttk.Button(master = input_frame, text = "Search 🔍", command = getWeather,)
input_frame.pack()
entry.pack(side = "left", pady = 15)
button.pack(side = "left", padx = 10, pady = 15)


planet_label = ttk.Label(master = window, text = "", font = "Comfortaa 15")
planet_label.pack()


result_labelw = ttk.Label(master = window, text = "", font = "Comfortaa 10")
result_labelw.pack()

result_labelt = ttk.Label(master = window, text = "", font = "Comfortaa 10")
result_labelt.pack()

name_label = ttk.Label(master = window, text = "Created by MegadudeCC", font = "Comfortaa 10")
name_label.pack(pady = 15)

#run
window.mainloop()