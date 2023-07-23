import tkinter as tk

button_font = ("poppins",20,"bold")


class Stopwatch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stopwatch")
        self.root.geometry("500x200")
        self.root.resizable(False,False)
        self.root.config(padx=10,pady=10,bg="white")
        self.timer = None

        self.hour = 0
        self.minute = 0
        self.second = 0
        
        self.clock_label = tk.Label(self.root,bg="black",fg="white",
                                    font=("poppins",35,"bold"),text=f"0{self.hour}:0{self.minute}:0{self.second}",
                                    padx=10,pady=10,anchor="center")
        self.clock_label.grid(row=0,column=0,columnspan=3,sticky="news")
        
        self.root.rowconfigure(0,weight=1)
        self.root.columnconfigure((0,1,2),weight=1)
        

        self.start_button = tk.Button(self.root,text="Start",bg="silver",fg="black",
                                      font=button_font,anchor="center",command=self.start)
        self.start_button.grid(row=1,column=0,sticky="ew")

        self.stop_button = tk.Button(self.root,text="Stop",bg="silver",fg="black",
                                      font=button_font,anchor="center",command=self.stop)
        self.stop_button.grid(row=1,column=1,sticky="ew")

        self.reset_button = tk.Button(self.root,text="Reset",bg="silver",fg="black",
                                      font=button_font,anchor="center",command=self.reset)
        self.reset_button.grid(row=1,column=2,sticky="ew")


        self.root.mainloop()


    def start(self):
        self.start_button.config(state="disabled")
        self.increment_time()


    def increment_time(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1

        time = f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        self.clock_label.config(text=time)
        self.timer = self.root.after(1000,self.increment_time)


    def reset(self):
        self.second = 0
        self.minute = 0
        self.hour = 0
        self.root.after_cancel(self.timer)
        self.start_button.config(state="normal")
        self.clock_label.config(text="00:00:00")

    
    def stop(self):
        self.root.after_cancel(self.timer)
        self.start_button.config(state="normal")


stopwatch = Stopwatch()