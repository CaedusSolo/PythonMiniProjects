from tkinter import * 
import tkinter as tk
from geopy.geocoders import Nominatim 
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime 
import requests 
import pytz 


def get_weather():
    try:
        city = city_textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        time_now = local_time.strftime("%I:%M %p")
        clock_label.config(text=time_now)
        name.config(text="CURRENT WEATHER")

        # weather settings
        end_point = "https://api.openweathermap.org/data/2.5/weather"
        api_key = "2225842deafe192468d897cb2a7f58a8"
        parameters = {
            "q" : city,
            "appid" : api_key
        }

        response = requests.get(end_point, params=parameters)
        response.raise_for_status()
        data = response.json()

        condition = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = int(data["main"]["temp"]-273)
        feels_like_temperature = int(data["main"]["feels_like"]-273)
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        t.config(text=f"{temperature}°C")
        c.config(text=f"{condition} | FEELS LIKE: {feels_like_temperature}°C")
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as error:
        messagebox.showerror(title="Error",message="Invalid entry")


window = Tk()
window.title("Weather App")
window.geometry("900x500+300+200")
window.resizable(False,False)

# Search bar 
search_image = PhotoImage(file="Tkinter\\Weather App\\images\\search.png")
my_image = Label(image=search_image)
my_image.place(x=20,y=20)

city_textfield = tk.Entry(window,
                     justify="center",
                     width=17,
                     font=("poppins",25,"bold"),
                     bg="#404040",
                     border=0,
                     fg="white")
city_textfield.place(x=50,y=40)
city_textfield.focus()

search_icon = PhotoImage(file="Tkinter\\Weather App\\images\\search_icon.png")
my_image_icon = Button(image=search_icon,
                       borderwidth=0,
                       cursor="hand2",
                       bg="#404040",
                       command=get_weather)
my_image_icon.place(x=400,y=33)

# logo 
logo_image = PhotoImage(file="Tkinter\\Weather App\\images\\logo.png")
logo_label = Label(image=logo_image)
logo_label.place(x=150,y=100)

# button box
frame_image = PhotoImage(file="Tkinter\\Weather App\\images\\box.png")
frame_my_image = Label(image=frame_image)
frame_my_image.pack(padx=5,pady=5,side=BOTTOM)

# time 
name = Label(window,font=("Arial",15,"bold"))
name.place(x=30,y=100)
clock_label = Label(window,font=("Helvetica",20))
clock_label.place(x=30,y=130)


# labels
wind_label = Label(window,text="WIND",font=("Helvetica",15,"bold"),
                fg="white",bg="#1ab5ef")
wind_label.place(x=120,y=400)

humidity_label = Label(window,text="HUMIDITY",font=("Helvetica",15,"bold"),
                fg="white",bg="#1ab5ef")
humidity_label.place(x=225,y=400)

description_label = Label(window,text="DESCRIPTION",font=("Helvetica",15,"bold"),
                fg="white",bg="#1ab5ef")
description_label.place(x=450,y=400)

pressure_label = Label(window,text="PRESSURE",font=("Helvetica",15,"bold"),
                fg="white",bg="#1ab5ef")
pressure_label.place(x=650,y=400)

t = Label(window,font=("Arial",70,"bold"),
          fg="#ee666d")
t.place(x=400,y=150)
c = Label(font=("Arial",15,"bold"))
c.place(x=400,y=250)

w = Label(text="...",
          font=("Arial",20,"bold"),
          bg="#1ab5ef")
w.place(x=120,y=430)

h = Label(text="...",
          font=("Arial",20,"bold"),
          bg="#1ab5ef")
h.place(x=280,y=430)

d = Label(text="...",
          font=("Arial",20,"bold"),
          bg="#1ab5ef")
d.place(x=445,y=430)

p = Label(text="...",
          font=("Arial",20,"bold"),
          bg="#1ab5ef")
p.place(x=670,y=430)


window.mainloop()