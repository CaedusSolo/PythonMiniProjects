from tkinter import * 
from tkinter import messagebox
# ------------------------------- CONSTANTS ------------------------------

THEME_COLOUR = "#cc9933"
TITLE_FONT = ("Ink Free",30,"bold")
WIDGET_FONT = ("Ink Free",24,"normal")

# ------------------------------- ADD TASK BUTTON ------------------------------

def add_task():
    task = entrybox.get()
    if len(task) > 0: 
        task_listbox.insert(END,task)
        entrybox.delete(0,END)
    else:
        messagebox.showerror(title="Error",message="No task entered. Please try again.")

# ------------------------------- DELETE TASK BUTTON ------------------------------

def delete_task():
    try:
        index = task_listbox.curselection()
        if messagebox.askyesno("Confirm Deletion","Do you want to delete this task?"):
            task_listbox.delete(index)
    except:
        messagebox.showerror(title="Oops",message="No task has been selected. Please try again.") 

# ------------------------------- DELETE TASK BUTTON ------------------------------

def search_task():
    query = search_task_entry.get().lower()
    search_task_entry.delete(0,END)
    # task_listbox.delete(0,END)
    for task in tasks:
        if query == task.lower():
            task_listbox.insert(END,query)


# ------------------------------- UI ------------------------------

window = Tk()
window.title("To Do List")
window.config(bg=THEME_COLOUR,padx=30)
window.minsize(width=1000,height=1000)


title_label = Label(text="TO DO LIST",
                    fg="white",
                    bg=THEME_COLOUR,
                    font=TITLE_FONT,
                    anchor="center",
                    padx=300,
                    pady=10)
title_label.grid(row=0,column=0,columnspan=2)

entrybox = Entry(font=WIDGET_FONT,bg="silver",fg="black",width=30)
entrybox.focus()
entrybox.grid(row=1,column=0,pady=20,padx=20)

add_task_button = Button(text="Add Task",
                         font=WIDGET_FONT,
                         command=add_task,
                         highlightthickness=0,
                         padx=10,
                         width=20)
add_task_button.grid(row=1,column=1)

search_task_entry = Entry(font=WIDGET_FONT,bg="silver",fg="black",width=30)
search_task_entry.grid(row=2,column=0,pady=20,padx=20)

search_button = Button(text="Search Tasks",
                       font=WIDGET_FONT,
                       command=search_task,
                       highlightthickness=0,
                       padx=10,
                       width=20)
search_button.grid(row=2,column=1)


task_listbox = Listbox(font=WIDGET_FONT,width=30,height=5)
task_listbox.grid(row=3,column=0,padx=10,pady=30,columnspan=2)

delete_button = Button(text="Delete Task",font=WIDGET_FONT,highlightthickness=0,command=delete_task)
delete_button.grid(row=4,column=0,columnspan=2)


tasks = ["Walk the dog","Read a book"]
for task in tasks:
    task_listbox.insert(END,task)


scrollbar = Scrollbar(master=window)
scrollbar.grid(row=3, column=1, sticky="ns",pady=30)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)


window.mainloop()