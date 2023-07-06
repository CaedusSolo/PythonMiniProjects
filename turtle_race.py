from turtle import Turtle, Screen 
import random 

screen = Screen()
screen.setup(width=500,height=500)
user_input = screen.textinput(title="Make your bet: ",
                 prompt="Which turtle will win the race? Enter a colour: ")
print(f"User bet: {user_input}")

turtle_colours = ["red","orange","yellow","green","blue","indigo","purple"]
y_coords = [190,130,70,10,-50,-110,-170]
all_turtles = []
race_still_on = False


for i in range(0,7):
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(turtle_colours[i])
    new_turtle.goto(x=-230, y=y_coords[i])


if user_input:
    race_still_on = True 


while race_still_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_still_on = False
            winner = turtle.color()
            if user_input == winner[0]:
                print(f"You are right! The winner was {winner[0]}")
            else:
                print(f"You lost! The winner was {winner[0]}")
            break
        random_distance = random.randint(1,20)
        turtle.forward(random_distance)
    


screen.exitonclick()