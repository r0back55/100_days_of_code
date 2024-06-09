import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# -------------------------------------------------
# Create a screen
screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)


# -------------------------------------------------
# Initiating objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detecting collision with the car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detecting when player wins the round:
    if player.ycor() > 280:
        scoreboard.counter()
        scoreboard.increase_level()
        player.reset_position()
        car_manager.level_up()


screen.exitonclick()
