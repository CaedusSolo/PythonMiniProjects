# project to find out the flights headed to KLIA (KUL) 

import requests
import tkinter as tk

ENDPOINT = "http://api.aviationstack.com/v1/flights"
KEY = "74b94ac2b21d42257005c32ed3efbsf24"


class FlightData:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Flight Data of Flights to KUL")
        self.root.config(bg="#00CCFF",padx=10,pady=10)
        self.root.geometry("700x600")
        self.root.resizable(False,False)

        self.title_label = tk.Label(self.root,bg="#00CCFF",fg="white",padx=10,pady=10,
                                    highlightthickness=0,text="Flights Headed to KLIA (KUL)",
                                    anchor="center",
                                    font=("Tahoma",22,"bold"))
        self.title_label.grid(row=0,column=0,columnspan=2,sticky="ew")
        self.root.columnconfigure((0,1),weight=1)

        self.active_flight_frame = tk.Frame(self.root,bg="white",highlightthickness=0,
                                            padx=10,pady=10)
        self.active_flight_frame.grid(row=1,column=0,sticky="ew")

        self.active_flight_label = tk.Label(self.active_flight_frame,text="Current active flights: ",bg="white",
                                            fg="black",font=("Tahoma",20,"normal"),padx=10,pady=3,
                                            highlightthickness=0)
        self.active_flight_label.grid(row=0,column=0)
        self.active_flight_info = tk.Label(self.active_flight_frame,bg="white",fg="black",
                                           text="test",font=("Tahoma",20,"normal"),wraplength=650,anchor="center")
        self.active_flight_info.grid(row=1,column=0,columnspan=2,sticky="news")
        
        self.weather_info_label = tk.Label(self.root,font=("Tahoma",20,"normal"),bg="#00CCFF",fg="white",
                                     highlightthickness=0,padx=10,pady=20,wraplength=600)
        self.weather_info_label.grid(row=2,column=0,columnspan=2)

        self.get_active_flight_info()
        self.get_weather()
        
        self.root.mainloop()

    
    def get_active_flight_info(self):
        parameters = {
            "access_key" : KEY,
            "flight_status" : "active",
            "arr_iata" : "KUL"
        }
        flight_info_text = ""
        response = requests.get(ENDPOINT,params=parameters)
        response.raise_for_status()

        data = response.json()["data"]

        flights_displayed = data[:10]
        for index,flight in enumerate(flights_displayed):

            departure_airport = flight["departure"]["airport"]
            flight_num = flight["flight"]["number"]
            
            flight_info = f"Flight {flight_num} from {departure_airport}\n" 
            flight_info_text += flight_info

        flights_not_displayed = len(data) - len(flights_displayed)
        self.active_flight_info.config(text=f"{flight_info_text} and {flights_not_displayed} more")

        self.root.after(1000,self.get_active_flight_info)


    def get_weather(self):
        end_point = "https://api.openweathermap.org/data/2.5/weather"
        api_key = "2225842deafe192468d897cb2a7f58a8" 

        parameters = {
            "q" : "Kuala Lumpur",
            "appid" : api_key
        }

        response = requests.get(end_point,params=parameters)
        response.raise_for_status()
        weather_data = response.json() 

        weather_condition = weather_data["weather"][0]["main"]
        description = weather_data["weather"][0]["description"]
        
        self.weather_info_label.config(text=f"Weather in Kuala Lumpur: {weather_condition}\n Condition: {description}")


flight_data = FlightData()