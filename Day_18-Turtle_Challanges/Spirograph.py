from turtle import Turtle, Screen
import random

# Changing Franklin's appearance
franklin = Turtle()
franklin.shape("turtle")
franklin.speed("fastest")

chars = ['a', 'b', 'c', 'd', 'e', 'f', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def random_color(char_list):
    """Function returns HEX color in a format of #______ """
    rand_color = [str(random.choice(char_list)) for char in range(6)]
    return ("#" + "".join(rand_color)).upper()


def draw_spirograph(size):
    for circle in range(size):
        franklin.color(random_color(chars))
        franklin.circle(100)
        franklin.right(360/size)


draw_spirograph(85)

screen = Screen()
screen.exitonclick()
