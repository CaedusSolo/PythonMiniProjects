from turtle import Turtle 
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.display_score()


    def increment_score(self):
        self.score += 1 
        self.clear()
        self.display_score()
    

    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=FONT) 

    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)