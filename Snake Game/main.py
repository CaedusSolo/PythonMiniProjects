from turtle import Screen
import time 
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("J's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(key="Up",fun=snake.move_up)
screen.onkey(key="Down",fun=snake.move_down)
screen.onkey(key="Left",fun=snake.move_left)
screen.onkey(key="Right",fun=snake.move_right)


game_is_on = True 
while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Calculate if snake has collided with food 

    if snake.head.distance(food) < 15:
        print("Nom nom nom")
        food.refresh()
        snake.extend()
        score.increment_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    for square in snake.squares[1:]:
        if snake.head.distance(square) < 15:
            game_is_on = False 
            score.game_over()


screen.exitonclick()