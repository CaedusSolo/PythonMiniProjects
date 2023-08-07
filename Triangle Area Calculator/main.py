    # Program to calculate the area of a triangle using Heron's Formula:
    #  A = sqrt(s(s-a)(s-b)(s-c)) , where a,b,c are the length of each side of the triangle respectively. 

import tkinter as tk 
import math 

class AreaOfTriangle:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Area Calculator")
        self.root.config(bg="white",padx=20,pady=20)
        self.root.geometry("650x650")
        self.root.resizable(False,False)

        diagram_img = tk.PhotoImage(file="Tkinter\\Triangle Area Calculator\\diagram.png")
        self.diagram_image = tk.Label(self.root,image=diagram_img,highlightthickness=0,border=0,
                                      borderwidth=0,anchor="center")
        self.diagram_image.grid(row=0,column=0,sticky="n",columnspan=2)

        self.a_length_label = tk.Label(self.root,font=("Ink Free",20,"bold"),highlightthickness=0,
                                       text="Enter the length of side \"a\" in cm: ",bg="white",fg="black",
                                       pady=10,padx=10,anchor="nw")
        self.a_length_label.grid(row=1,column=0,sticky="wn")
        self.a_length_entry = tk.Entry(self.root,bg="white",fg="black",font=("Ink Free",20,"bold"),
                                       insertbackground="black",width=10)
        self.a_length_entry.grid(row=1,column=1,sticky="ne",padx=10,pady=5)
        self.root.grid_columnconfigure((0,1),weight=1)

        self.b_length_label = tk.Label(self.root,font=("Ink Free",20,"bold"),bg="white",fg="black",
                                       highlightthickness=0,text="Enter the length of side \"b\" in cm: ",
                                       anchor="nw",padx=10,pady=10
                                       )
        self.b_length_label.grid(row=2,column=0,sticky="wn")
        self.b_length_entry = tk.Entry(self.root,width=10,bg="white",fg="black",insertbackground="black",
                                       font=("Ink Free",20,"bold"))
        self.b_length_entry.grid(row=2,column=1,sticky="ne",padx=10,pady=5)

        self.c_length_label = tk.Label(self.root,bg="white",fg="black",font=("Ink Free",22,"bold"),
                                       anchor="nw",highlightthickness=0,padx=10,pady=10,
                                       text="Enter the length of side \"c\" in cm: ")
        self.c_length_label.grid(row=3,column=0)
        self.c_length_entry = tk.Entry(self.root,width=10,bg="white",fg="black",insertbackground="black",
                                       font=("Ink Free",20,"bold"))
        self.c_length_entry.grid(row=3,column=1,sticky="ne",padx=10,pady=5)    

        self.a_length_entry.focus()
        self.b_length_entry.focus()
        self.c_length_entry.focus()

        self.calculate_area_button = tk.Button(self.root,bg="white",fg="black",highlightthickness=0,
                                               padx=10,pady=5,text="Calculate Area!",font=("Ink Free",20,"bold"),
                                               anchor="center",relief="ridge",cursor="hand2",
                                               command=self.calculate_area)
        self.calculate_area_button.grid(row=4,column=0,sticky="ns",columnspan=2)

        self.display_area_label = tk.Label(self.root,bg="white",fg="black",padx=10,pady=10,
                                           font=("Ink Free",18,"bold"),highlightthickness=0,
                                           anchor="center",
                                           text="Any feedback from the program will show up here, this includes the area of the triangle and any error messages.",
                                           wraplength=600)
        self.display_area_label.grid(row=5,column=0,columnspan=2)

        self.root.mainloop() 

    def calculate_area(self):
        try:
            a_length = float(int(self.a_length_entry.get()))
            b_length = float(int(self.b_length_entry.get()))
            c_length = float(int(self.c_length_entry.get()))

            if a_length <= 0 or b_length <= 0 or c_length <= 0:
                self.display_area_label.config(text="The length of all the sides must be greater than 0. Please try again.")
                return
            else:
                semiperimeter = (a_length + b_length + c_length) / 2 
                area = math.sqrt(semiperimeter * (semiperimeter - a_length) * (semiperimeter - b_length) * (semiperimeter - c_length))
            
        except ValueError:
            self.display_area_label.config(text="Invalid entry! Please try again.")

        else:
            self.display_area_label.config(text=f"The area of the triangle is: {area:.2f} cm^2.")

        finally:
            self.a_length_entry.delete(0,tk.END)
            self.b_length_entry.delete(0,tk.END)
            self.c_length_entry.delete(0,tk.END)


area = AreaOfTriangle()