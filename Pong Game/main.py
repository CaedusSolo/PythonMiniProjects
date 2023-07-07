from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="w",fun=left_paddle.move_up)
screen.onkey(key="Up",fun=right_paddle.move_up)
screen.onkey(key="s",fun=left_paddle.move_down)
screen.onkey(key="Down",fun=right_paddle.move_down)


game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle 

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        print("made contact")
        ball.bounce_x()
        ball.move_speed *= 0.95
    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score() 
        ball.move_speed = 0.1

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()
        ball.move_speed = 0.1


screen.exitonclick()