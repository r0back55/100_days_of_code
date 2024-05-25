# General Method Call
# import turtle
# timmy1 = turtle.Turtle()


# More detailed way
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

timmy.shape("turtle")
timmy.color("DarkGreen")
timmy.width(2)

timmy.left(90)
timmy.forward(100)

timmy.right(30)
timmy.forward(40)
timmy.right(30)
timmy.forward(40)
timmy.right(30)
timmy.forward(40)

timmy.right(120)
timmy.forward(40)
timmy.right(30)
timmy.forward(40)
timmy.right(30)
timmy.forward(40)

timmy.right(90)
timmy.forward(140)


for step in range(50):
    for c in ('red', 'green', 'yellow'):
        timmy.color(c)
        timmy.forward(step)
        timmy.right(30)


my_screen = Screen()
print(my_screen.canvheight)  # canvheight is an attribute of Screen()
my_screen.exitonclick()
