from tkinter import * 
from tkinter import messagebox
import random 
import pyperclip

WIDGET_FONT = ("Courier",18,"normal")
THEME_COLOUR = "#ebcfb2"
CHARS_LIST = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%^&*")
LABEL_BG = "#C7C9CB"
password = ""
# ------------------------------ BUTTON FUNCTIONALITIES -------------------------------

def generate_password():
    global password
    try:
        chars_num = int(password_length_entry.get())
        password_length_entry.delete(0,END)

    except ValueError:
        messagebox.showerror(title="Error",message="Please enter the number of characters for the password.")

    else:   
        if chars_num == 0:
            messagebox.showerror("Please enter the number of characters for the password.")
        else:
            chars = []
            for i in range(chars_num):
                chars.append(random.choice(CHARS_LIST))
            random.shuffle(chars)
            password = "".join(chars)
            password_label.config(text=f"The password is: {password}")
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")


def save_password():
    global password
    email = email_entry.get()
    website = website_entry.get()
    pwd = password

    if len(email) == 0 or len(website) == 0:
        messagebox.showerror(title="Oops",message="Please complete all of the required fields.")
    
    else:
        try:
            with open("Tkinter\Password Generator\passwords.txt","a") as file:
                file.write(f"{email} | {website} | {pwd}\n")

        except FileNotFoundError:
            with open("Tkinter\Password Generator\passwords.txt","w") as file:
                file.write(f"{email} | {website} | {pwd}\n")

        finally:
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_label.config(text="")
            messagebox.showinfo(title="Success!",message="Password successfully saved.")

# ------------------------------------- UI -----------------------------------------

window = Tk()
window.config(bg=THEME_COLOUR,pady=30,padx=30)
window.minsize(width=300,height=300)
window.title("Password Generator")

text = "The number of uppercase letters, lowercase letters, numbers and symbols are randomized."
intro_text = Text(
                  wrap="word",
                  font=WIDGET_FONT,
                  padx=20,
                  pady=20,
                  highlightthickness=0,
                  bg=LABEL_BG,
                  height=1,
                  width=90)
intro_text.insert(END,text)
intro_text.grid(row=0,column=0,columnspan=2)

password_length_label = Label(text="How many characters should the password contain? ------------------->",
                              font=WIDGET_FONT,
                              padx=20,
                              bg=THEME_COLOUR,
                              pady=20,
                              anchor="e")
password_length_label.grid(row=1,column=0,sticky="e")

password_length_entry = Entry(font=WIDGET_FONT,width=5)
password_length_entry.focus()
password_length_entry.grid(row=1,column=1,padx=10)

generate_password_button = Button(text="Generate Password",
                                  font=WIDGET_FONT,
                                  padx=10,
                                  command=generate_password,
                                  highlightthickness=0,
                                  relief=RAISED)
generate_password_button.grid(row=2,column=0,columnspan=2)

password_label = Label(font=WIDGET_FONT,bg=THEME_COLOUR,pady=30,padx=20,anchor='w')
password_label.grid(row=3,column=0)

save_password_label = Label(text="Complete the following fields to save your password: ",
                            font=WIDGET_FONT,
                            pady=20,
                            padx=15,
                            bg=THEME_COLOUR)
save_password_label.grid(row=4,column=0)

email_label = Label(text="Email/Username -------------------------->",font=WIDGET_FONT,pady=20,padx=10,bg=THEME_COLOUR)
email_label.grid(row=5,column=0)

email_entry = Entry(font=WIDGET_FONT,width=21)
email_entry.grid(row=5,column=1,columnspan=2,sticky="e")

website_label = Label(text="Website --------------------------------->",font=WIDGET_FONT,pady=20,padx=10,bg=THEME_COLOUR)
website_label.grid(row=6,column=0)

website_entry = Entry(font=WIDGET_FONT,width=21)
website_entry.grid(row=6,column=1,sticky="e")

save_password_button = Button(text="Save",
                              font=WIDGET_FONT,
                              highlightthickness=0,
                              command=save_password,
                              padx=10,
                              relief=RAISED)
save_password_button.grid(row=7,column=0,columnspan=2)
window.mainloop()