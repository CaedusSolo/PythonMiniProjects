from turtle import Turtle

STARTING_COORDS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
    

    def create_snake(self):
        for coordinates in STARTING_COORDS:
            self.add_square(coordinates)


    def move(self):
        for square_num in range(len(self.squares)-1, 0, -1):
            new_x = self.squares[square_num - 1].xcor() 
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x,new_y) 
        
        self.squares[0].forward(MOVE_DISTANCE)
    

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP) 
          

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN) 


    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 


    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
            
    def add_square(self,coordinates):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(coordinates)
        self.squares.append(new_square)


    def extend(self):
        self.add_square(self.squares[-1].position()) 