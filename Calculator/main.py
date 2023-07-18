from tkinter import *

WIDGET_FONT = ("Times New Roman", 20, "bold")
buttons = [
    "AC", "DEL", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "+",
    "1", "2", "3", "-",
    ".", "0", "="
]

# --------------------------- CLEAR/DELETE FUNCTIONALITY -----------------------------

def clear():
    display_entry.delete(0,END)


def delete():
    current_value = display_entry.get() 
    updated_value = current_value[:-1]
    display_entry.delete(0,END)
    display_entry.insert(END,updated_value)

# ----------------------------- OPERATION BUTTONS ----------------------------------

def button_click(value):
    current_value = display_entry.get()
    display_entry.delete(0,END)
    display_entry.insert(END,current_value + value)


def calculate():
    operation = display_entry.get()

    try:
        result = eval(operation)
        display_entry.delete(0,END)
        display_entry.insert(END,str(result))

    except:
        display_entry.delete(0,END)
        display_entry.insert(END,"ERROR")

# -------------------------------- UI ----------------------------------------------

window = Tk()
window.title("Calculator Program")
window.minsize(height=450, width=500)
window.config(padx=25, pady=25)

display_entry = Entry(window, font=WIDGET_FONT, bg="black", fg="white")
display_entry.focus()
display_entry.configure(insertbackground="blue",width=35,)
display_entry.grid(column=0, row=0, columnspan=4,)

row = 1
col = 0

for button in buttons:

    if button == "AC":
        button = Button(window, text=button, font=WIDGET_FONT,width=10,padx=5,pady=5,command=clear)
        button.grid(row=row,column=col,sticky="EW")
        col += 1

    elif button == "DEL":
        button = Button(window, text=button, font=WIDGET_FONT,width=10,padx=5,pady=5,command=delete)
        button.grid(row=row, column=col, columnspan=2,sticky="EW")
        col += 2

    elif button == "=":
        button = Button(window, text=button, font=WIDGET_FONT,width=10,padx=5,pady=5,command=calculate)
        button.grid(row=row, column=col, columnspan=2,sticky="EW")
        col += 2

    else:
        button = Button(window, 
                        text=button, 
                        font=WIDGET_FONT,
                        width=5,
                        padx=5,
                        pady=5,
                        command=lambda value=button: button_click(value))
        button.grid(row=row, column=col,sticky="EW")
        col += 1

    if col > 3:
        col = 0
        row += 1

window.mainloop()
