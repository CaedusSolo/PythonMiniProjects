import tkinter as tk 
from tkinter import messagebox

# Note for myself: To change cursor colour in Entry, use insertbackground kwarg


class EmailSlicer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Email Slicer")
        self.window.geometry("700x500")
        self.window.resizable(False,False)
        self.window.config(bg="black",padx=20,pady=20)

        self.email_slicer_label = tk.Label(self.window,bg="white",fg="black",padx=5,pady=5,
                                           font=("Ink Free",22,"bold"),highlightthickness=0,
                                           text="Welcome To This Email Slicer Program!")
        self.email_slicer_label.grid(row=0,column=0)
        self.window.columnconfigure(0,weight=1)

        self.instructions_label = tk.Label(self.window,text="Just enter your email into the text entry below, then click on the \"Slice\" button. The program will then determine your email username and email domain.",
                                           highlightthickness=0,bg="black",fg="white",padx=5,pady=20,
                                           font=("Ink Free",20,"bold"),wraplength=600)
        self.instructions_label.grid(row=1,column=0) 

        self.email_field = tk.Entry(self.window,insertbackground="black",bg="white",fg="black",
                                    width=20,font=("Arial",20,"normal"))
        self.email_field.focus()
        self.email_field.grid(row=2,column=0,sticky="we",padx=20,pady=5)

        self.slice_button = tk.Button(self.window,bg="white",fg="black",font=("Ink Free",22,"bold"),
                                      relief="ridge",text="Slice",anchor="center",width=10,padx=10,pady=5,
                                      cursor="hand2",command=self.slice_email)
        self.slice_button.grid(row=3,column=0)

        self.email_username_label = tk.Label(self.window,bg="black",fg="white",font=("Ink Free",22,"bold"),
                                             text="Email Username:     ",padx=10,pady=10,
                                             anchor="center")
        self.email_username_label.grid(row=4,column=0) 

        self.email_domain_label = tk.Label(self.window,bg="black",fg="white",font=("Ink Free",22,"bold"),
                                             text="Email Domain:     ",padx=10,pady=10,
                                             anchor="center")
        self.email_domain_label.grid(row=5,column=0)

        self.window.mainloop() 


    def slice_email(self):
        try:
            email = self.email_field.get()
            index_of_at_symbol = email.index("@")

            username = email[:index_of_at_symbol]
            domain = email[index_of_at_symbol+1:]

        except ValueError:
            messagebox.showerror(title="Error",message="Please enter a valid email address.")

        else:
            self.email_username_label.config(text=f"Email Username:      {username}")
            self.email_domain_label.config(text=f"Email Domain:      {domain}")
        
        finally:
            self.email_field.delete(0,tk.END)


email_slicer = EmailSlicer()