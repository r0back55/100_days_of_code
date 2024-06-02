from turtle import Turtle, Screen
import random

# -------------------------------------------------
# basic setup
is_game_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Winner", prompt="Who will win the game? (color)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=(-100 + 40 * turtle_index))
    all_turtles.append(new_turtle)


if user_bet:
    is_game_on = True


while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_game_on = False

            if user_bet == turtle.pencolor():
                print(f"You've won! Turtle {turtle.pencolor()} fished the first!")
            else:
                print(f"You've lost! Turtle {turtle.pencolor()} fished the first!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
