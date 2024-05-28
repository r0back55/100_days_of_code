from turtle import Turtle, Screen
import random

# changing Franklin's appearance
franklin = Turtle()
franklin.shape("turtle")


# --------------------------------------------------------------
# Hi Franklin - lets go for a random walk, very fast one:
franklin.pensize(15)
franklin.speed(10)

direction = [0, 90, 180, 270]
chars = ['a', 'b', 'c', 'd', 'e', 'f', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def random_color(characters):
    """Function returns HEX color in a format of #______ """
    rand_color = [str(random.choice(characters)) for char in range(6)]
    return ("#" + "".join(rand_color)).upper()


def random_move(number_of_steps, characters):
    for step in range(number_of_steps):
        color = random_color(characters)
        franklin.color(color)
        franklin.forward(30)
        angle = random.choice(direction)
        franklin.right(angle)


random_move(200, chars)

screen = Screen()
screen.exitonclick()
