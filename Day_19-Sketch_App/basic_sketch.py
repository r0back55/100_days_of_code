from turtle import Turtle, Screen


franklin = Turtle()
screen = Screen()


def move_forwards():
    franklin.forward(10)


def move_back():
    franklin.backward(10)


def turn_right():
    franklin.right(10)


def turn_left():
    franklin.left(10)


def clear_screen():
    franklin.clear()
    franklin.penup()
    franklin.home()
    franklin.pendown()


screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_back, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")

screen.onkey(clear_screen, "c")

screen.exitonclick()
