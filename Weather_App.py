import requests
from tkinter import *
from tkinter import messagebox


MY_API_KEY = '7952acfed7b17c38eaa5acec0288b647'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def app_weather(my_city):
    url = f"{BASE_URL}appid={MY_API_KEY}&q={my_city}"
    response = requests.get(url)
    return response.json()

def search():
    my_city = the_city_text.get()
    weather_is = app_weather(my_city)
    if weather_is and weather_is.get('cod') != '404':
        lbl_location['text'] = f"{weather_is['name']}, {weather_is['sys']['country']}"
        temp_celsius = weather_is['main']['temp'] - 273.15
        temperature_lbl['text'] = f"{temp_celsius:.2f} °C"
        weather_lbl['text'] = weather_is['weather'][0]['description'].capitalize()
    else:
        messagebox.showerror('Error!!', f"Sorry, can't find city '{my_city}'")

application_weather = Tk()
application_weather.title("Weather App")
application_weather.geometry("400x300")

the_city_text = StringVar()
a_city_entry = Entry(application_weather, textvariable=the_city_text)
a_city_entry.pack()

search_button = Button(application_weather, text="Search to know Weather for a perticular city", command=search)
search_button.pack()

lbl_location = Label(application_weather, text="Valid Location", font=('bold', 20))
lbl_location.pack()

temperature_lbl = Label(application_weather, text="")
temperature_lbl.pack()

weather_lbl = Label(application_weather, text="")
weather_lbl.pack()

application_weather.mainloop()