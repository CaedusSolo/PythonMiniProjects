import tkinter 
from tkinter import ttk
from tkinter import messagebox

BG_COLOUR = "#333333" 
FG_COLOUR = "#FF1D8E"
FONT = ("Arial",14,"normal")

def save_data():

    accepted = accept_var.get()
    if accepted == "Accepted":

    # User data
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:

            age = age_spinbox.get()
            title = title_combobox.get()
            nationality = nationality_combobox.get()

            # Courses data
            course_num = course_num_spinbox.get()   
            semester_num = semester_num_spinbox.get()
            registration_status = reg_status_var.get()

            entry = f"Name: {title} {firstname} {lastname} | Age: {age} | Nationality: {nationality} | Number of Courses: {course_num} | Number of Semesters: {semester_num} | Registration Status: {registration_status}\n"
            
            try:
                with open("Tkinter\\Registration GUI\\user_data.txt","a") as file:
                    file.write(entry)
                    
            except FileNotFoundError:
                with open("Tkinter\\Registration GUI\\user_data.txt","w") as file:
                    file.write(entry)

            finally:
                first_name_entry.delete(0,tkinter.END)
                last_name_entry.delete(0,tkinter.END)
                title_combobox.delete(0,tkinter.END)
                age_spinbox.delete(0,tkinter.END)
                nationality_combobox.delete(0,tkinter.END)
                course_num_spinbox.delete(0,tkinter.END)
                semester_num_spinbox.delete(0,tkinter.END)
                reg_status_var.set("Not Registered")
                accept_var.set("Not Accepted")

                messagebox.showinfo(title="Nice!",message="Data was saved successfully.")
                
        else:
            messagebox.showerror(title="Error",message="Please enter your first name and last name.")

    else:
        messagebox.showerror(title='Error',message="You have not accepted the terms and conditions.")

# -------------------------------------UI----------------------------------------------

window = tkinter.Tk()
window.title("Data Entry Form")
window.config(bg=BG_COLOUR,padx=20,pady=20)

frame = tkinter.Frame(window,bg=BG_COLOUR)
frame.pack()

# Saving user information
user_info_frame = tkinter.LabelFrame(frame,text="User Information",font=("Arial",18,"bold"),
                                     padx=20,pady=10,bg=BG_COLOUR,fg=FG_COLOUR)
user_info_frame.grid(row=0,column=0)

first_name_label = tkinter.Label(user_info_frame,text="First Name",font=FONT,bg=BG_COLOUR,fg="white")
first_name_label.grid(row=0,column=0)
last_name_label = tkinter.Label(user_info_frame,text="Last Name",font=FONT,bg=BG_COLOUR,fg="white")
last_name_label.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_info_frame,font=FONT)
first_name_entry.focus()
first_name_entry.grid(row=1,column=0)
last_name_entry = tkinter.Entry(user_info_frame,font=FONT)
last_name_entry.grid(row=1,column=1)

title_label = tkinter.Label(user_info_frame,text="Title",font=FONT,bg=BG_COLOUR,fg="white")
title_label.grid(row=0,column=2)
title_combobox = ttk.Combobox(user_info_frame,values=["None","Ms.","Mr.","Dr."],font=FONT)
title_combobox.grid(row=1,column=2)

age_label = tkinter.Label(user_info_frame,text="Age",font=FONT,bg=BG_COLOUR,fg="white")
age_label.grid(row=2,column=0)
age_spinbox = tkinter.Spinbox(user_info_frame,from_=18,to=100,font=FONT)
age_spinbox.grid(row=3,column=0)

nationality_label = tkinter.Label(user_info_frame,text="Nationality",bg=BG_COLOUR,fg="white",font=FONT)
nationality_combobox = ttk.Combobox(user_info_frame, font=FONT,
                                    values=["Malaysia","Singapore","Brunei","Thailand","Myanmar","Vietnam"])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

courses_frame = tkinter.LabelFrame(frame,font=("Arial",18,"bold"),text="Course Information",
                                   bg=BG_COLOUR,fg=FG_COLOUR)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

registered_label = tkinter.Label(courses_frame,text="Registration Status",font=FONT,bg=BG_COLOUR,fg='white')
registered_label.grid(row=0,column=0) 

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", 
                                       offvalue="Not registered",font=FONT,bg=BG_COLOUR,fg='#FC4C4E')

registered_check.grid(row=1,column=0)

course_num_label = tkinter.Label(courses_frame,font=FONT,bg=BG_COLOUR,fg="white",text="Number of Courses Registered")
course_num_label.grid(row=0,column=1)
course_num_spinbox = tkinter.Spinbox(courses_frame,font=FONT,from_=0,to="infinity")
course_num_spinbox.grid(row=1,column=1)
semester_num_label = tkinter.Label(courses_frame,font=FONT,bg=BG_COLOUR,fg="white",text="Number of Semesters Completed")
semester_num_label.grid(row=0,column=2)
semester_num_spinbox = tkinter.Spinbox(courses_frame,font=FONT,from_=0,to=20)
semester_num_spinbox.grid(row=1,column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

terms_frame = tkinter.LabelFrame(frame,text="Terms and Conditions",bg=BG_COLOUR,fg=FG_COLOUR,font=("Arial",18,"bold"))
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame,text="I accept the terms and conditions.",
                                  font=FONT,bg=BG_COLOUR,fg='#FC4C4E',variable=accept_var,
                                  onvalue="Accepted",offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

save_data_button = tkinter.Button(frame,text="Save Data",font=FONT,bg=BG_COLOUR,fg="white",padx=20,pady=10,command=save_data)
save_data_button.grid(row=3,column=0,sticky="news")

window.mainloop()