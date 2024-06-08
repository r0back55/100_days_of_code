from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# -------------------------------------------------
# Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Arcade Game")
screen.tracer(0)

# -------------------------------------------------
# Create a paddle
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collision with the wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detecting collision with the paddle:
    if ball.xcor() > 350 or ball.xcor() < -350:
        if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
            ball.paddle_bounce()

    # Counting score:
    if ball.xcor() > 390:
        ball.reset_position()
        score.counter_left()
        score.update_score()
    elif ball.xcor() < -390:
        ball.reset_position()
        score.counter_right()
        score.update_score()


screen.exitonclick()
