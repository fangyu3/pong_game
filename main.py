from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)

# Setup paddle
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

# Setup ball
ball = Ball()

# Setup scoreboard
scoreboard = Scoreboard()

screen.listen()

screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down,"Down")

screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Check collision against upper && lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check collision against right wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score_left()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score_right()

    # Check collision right paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 330)  or (ball.distance(left_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

screen.exitonclick()