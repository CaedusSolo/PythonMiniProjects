from tkinter import * 
import math 
# ---------------------------CONSTANTS---------------------------------

THEME_COLOUR = "#FFFFE0"
TITLE_FONT = ("Ink Free",25,"bold")
WORK_MINS = 25
SHORT_BREAK_MINS = 5
LONG_BREAK_MINS = 20
total_reps = 0
timer = None 
# ------------------------- FUNCTIONALITY ----------------------------

def start():
    start_button.config(state="disabled")
    global total_reps
    total_reps += 1
    work_seconds = WORK_MINS * 60
    short_break_seconds = SHORT_BREAK_MINS * 60
    long_break_seconds = LONG_BREAK_MINS * 60

    if total_reps % 8 == 0:
        title_label.config(text="LONG BREAK")
        countdown(long_break_seconds)
    elif total_reps % 2 == 0:
        title_label.config(text="SHORT BREAK") 
        countdown(short_break_seconds)
    else:
        title_label.config(text="WORK")
        countdown(work_seconds)


def countdown(seconds):
    global timer 
    mins = math.floor(seconds / 60)
    secs = seconds % 60 

    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_clock,text=f"{mins}:{secs}")

    if seconds > 0:
        timer = window.after(1000,countdown,seconds-1)
    
    else:
        start()
        mark = ""
        work_sessions = math.floor(total_reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmarks_label.config(text=mark)


def reset():
    start_button.config(state="active")
    global total_reps
    window.after_cancel(timer)
    total_reps = 0
    title_label.config(text="TIMER")
    checkmarks_label.config(text="")
    canvas.itemconfig(timer_clock,text="00:00")


# ------------------------------UI---------------------------------------

window = Tk()
window.minsize(width=600,height=550)
window.config(bg=THEME_COLOUR,padx=40)
window.title('Pomodoro Timer')

intro_label = Label(text="Increase your productivity using the Pomodoro method!",
                    font=TITLE_FONT,
                    bg=THEME_COLOUR, 
                    fg="black",
                    pady=30)
intro_label.grid(row=0,column=0,columnspan=2)

title_label = Label(text="",font=("Ink Free",30,"bold"),bg=THEME_COLOUR,fg="black")
title_label.grid(row=1,column=0,columnspan=2)

tomato_img = PhotoImage(file="Tkinter\\Pomodoro\\tomato.png")

canvas = Canvas(bg=THEME_COLOUR,width=200,height=224,highlightthickness=0)
canvas.create_image(100,112,image=tomato_img)
timer_clock = canvas.create_text(105,130,text="00:00",fill="black",font=("Ink Free",20,"bold"))
canvas.grid(row=2,column=0,columnspan=2,pady=50)

start_button = Button(text="Start",font=TITLE_FONT,width=15,highlightthickness=0,pady=10,command=start)
start_button.grid(row=3,column=0)

reset_button = Button(text="Reset",font=TITLE_FONT,width=15,highlightthickness=0,pady=10,command=reset)
reset_button.grid(row=3,column=1)

checkmarks_label = Label(bg=THEME_COLOUR,fg="black",font=TITLE_FONT,pady=30)
checkmarks_label.grid(row=4,column=0,columnspan=2)

window.mainloop()