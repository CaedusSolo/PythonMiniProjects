import tkinter as tk 
import requests

class AdviceGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x250")
        self.root.title("Advice Generator")
        self.root.config(bg="black",padx=10,pady=10)
        self.root.resizable(False,False)

        self.advice_label = tk.Label(self.root,text="A random advice is generated every minute.",bg="black",fg="white",
                                     font=("Tahoma",22,"bold"),padx=10,pady=10,highlightthickness=0,anchor="center")
        self.advice_label.grid(row=0,column=0,columnspan=2)

        self.advice_text_label = tk.Label(self.root,font=("Ink Free",24,"bold"),padx=10,pady=10,
                                          highlightthickness=0,bg="white",fg="black",anchor="center",
                                          wraplength=640)
        self.advice_text_label.grid(row=1,column=0,columnspan=2)

        self.get_advice()
        self.root.mainloop() 

    def get_advice(self):
        end_point = "https://api.adviceslip.com/advice"

        response = requests.get(end_point)
        response.raise_for_status()

        advice = response.json()["slip"]["advice"]
        self.advice_text_label.config(text=advice)

        self.root.after(60000,self.get_advice)


advice_generator = AdviceGenerator()