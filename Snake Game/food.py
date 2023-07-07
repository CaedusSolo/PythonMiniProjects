from turtle import Turtle
import random 

class Food(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("brown")
        self.speed("fastest")

        self.refresh()
        
    def refresh(self):
        random_x_coord = random.randint(-270,270) 
        random_y_coord = random.randint(-270, 270)
        self.goto(random_x_coord,random_y_coord)
