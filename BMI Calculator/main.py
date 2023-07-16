from tkinter import * 
import math

THEME_COLOUR = "#cc9933"
TITLE_FONT = ("Ink Free",30,"italic")
WIDGET_FONT = ("Ink Free",24,"normal")
ENTRY_FONT = ("Arial",22,"normal")

window = Tk()
window.minsize(width=600,height=550)
window.config(bg=THEME_COLOUR,pady=30,padx=30)
window.title("BMI CALCULATOR")

title_label = Label(text="YT'S BMI CALCULATOR PROGRAM",font=TITLE_FONT,bg=THEME_COLOUR,fg="white",padx=200)
title_label.grid(row=0,column=0,columnspan=2)

enter_weight_label = Label(text="Enter your weight in kilograms (kg):",
                           font=WIDGET_FONT,
                           bg=THEME_COLOUR,
                           fg="white",
                           padx=20,
                           pady=30)
enter_weight_label.grid(row=1,column=0)

weight_entry = Entry(width=20,font=ENTRY_FONT)
weight_entry.focus()
weight_entry.grid(row=1,column=1)

enter_height_label = Label(text="Enter your height in metres (m): ",
                           font=WIDGET_FONT,
                           bg=THEME_COLOUR,
                           fg='white',
                           pady=50)
enter_height_label.grid(row=2,column=0)

height_entry = Entry(width=20,font=ENTRY_FONT)
height_entry.focus()
height_entry.grid(row=2,column=1)

def update_bmi():
    try:
        user_height = float(height_entry.get()) 
        user_weight = float(weight_entry.get())
        user_bmi = user_weight / math.pow(user_height,2)
        bmi_label.config(text=f"Your BMI is:  {user_bmi:.2f}")

        if user_bmi < 18.5:
            info_label.config(text="You are underweight.")
        
        elif user_bmi >= 18.5 and user_bmi <= 25:
            info_label.config(text="You have a normal BMI.")

        elif user_bmi > 25 and user_bmi < 30:
            info_label.config(text="You are overweight.")
        
        else:
            info_label.config(text="You are obese.")

    except ValueError:
        info_label.config("Invalid input. Please enter numeric values only.")


calculate_button = Button(text="Calculate",font=WIDGET_FONT,width=15,command=update_bmi)
calculate_button.grid(row=3,column=0,columnspan=2)

bmi_label = Label(text="Your BMI is: ",font=WIDGET_FONT,bg=THEME_COLOUR,fg="white",pady=50,)
bmi_label.grid(row=4,column=0,columnspan=2)

info_label = Label(text="",font=WIDGET_FONT,bg=THEME_COLOUR,fg='white')
info_label.grid(row=5,column=0,columnspan=2)

window.mainloop()