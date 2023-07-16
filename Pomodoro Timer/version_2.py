from tkinter import *
from datetime import datetime, timedelta

THEME_COLOR = "#FFFFE0"
TITLE_FONT = ("Ink Free", 25, "bold")
WORK_MINS = 25
SHORT_BREAK_MINS = 5
LONG_BREAK_MINS = 20

class Timer:
    def __init__(self):
        self.total_reps = 0
        self.timer = None

    def start(self):
        self.start_button.config(state="disabled")
        self.total_reps += 1
        work_seconds = WORK_MINS * 60
        short_break_seconds = SHORT_BREAK_MINS * 60
        long_break_seconds = LONG_BREAK_MINS * 60

        if self.total_reps % 8 == 0:
            self.title_label.config(text="LONG BREAK")
            self.countdown(long_break_seconds)
        elif self.total_reps % 2 == 0:
            self.title_label.config(text="SHORT BREAK")
            self.countdown(short_break_seconds)
        else:
            self.title_label.config(text="WORK")
            self.countdown(work_seconds)

    def countdown(self, seconds):
        mins, secs = divmod(seconds, 60)
        time_str = "{:02d}:{:02d}".format(mins, secs)
        self.canvas.itemconfig(self.timer_clock, text=time_str)

        if seconds > 0:
            self.timer = self.window.after(1000, self.countdown, seconds - 1)
        else:
            self.start()
            mark = "✔" * (self.total_reps // 2)
            self.checkmarks_label.config(text=mark)

    def reset(self):
        self.start_button.config(state="active")
        self.window.after_cancel(self.timer)
        self.total_reps = 0
        self.title_label.config(text="TIMER")
        self.checkmarks_label.config(text="")
        self.canvas.itemconfig(self.timer_clock, text="00:00")

    def create_ui(self):
        self.window = Tk()
        self.window.minsize(width=600, height=550)
        self.window.config(bg=THEME_COLOR, padx=40)
        self.window.title('Pomodoro Timer')

        intro_label = Label(text="Increase your productivity using the Pomodoro method!",
                            font=TITLE_FONT,
                            bg=THEME_COLOR,
                            fg="black",
                            pady=30)
        intro_label.grid(row=0, column=0, columnspan=2)

        self.title_label = Label(text="",
                                 font=("Ink Free", 30, "bold"),
                                 bg=THEME_COLOR,
                                 fg="black")
        self.title_label.grid(row=1, column=0, columnspan=2)

        tomato_img = PhotoImage(file="Tkinter\\Pomodoro\\tomato.png")

        self.canvas = Canvas(bg=THEME_COLOR, width=200, height=224, highlightthickness=0)
        self.canvas.create_image(100, 112, image=tomato_img)
        self.timer_clock = self.canvas.create_text(105, 130, text="00:00", fill="black",
                                                   font=("Ink Free", 20, "bold"))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)

        self.start_button = Button(text="Start",
                                   font=TITLE_FONT,
                                   width=15,
                                   highlightthickness=0,
                                   pady=10,
                                   command=self.start)
        self.start_button.grid(row=3, column=0)

        self.reset_button = Button(text="Reset",
                                   font=TITLE_FONT,
                                   width=15,
                                   highlightthickness=0,
                                   pady=10,
                                   command=self.reset)
        self.reset_button.grid(row=3, column=1)

        self.checkmarks_label = Label(bg=THEME_COLOR,
                                      fg="black",
                                      font=TITLE_FONT,
                                      pady=30)
        self.checkmarks_label.grid(row=4, column=0, columnspan=2)

        self.window.protocol("WM_DELETE_WINDOW", self.quit)
        self.window.mainloop()

    def quit(self):
        self.window.quit()

timer = Timer()
timer.create_ui()     