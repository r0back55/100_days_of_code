from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("Snake Game")


# -------------------------------------------------
# Create a snake body

frank = Turtle()
frank.shape("square")
frank.shapesize(stretch_wid=1, stretch_len=1)
frank.color("white")
frank.goto(x=(0.00, 0.00))

frank1 = Turtle()
frank1.shape("square")
frank1.shapesize(stretch_wid=1, stretch_len=1)
frank1.color("white")
frank1.goto(x=(-20.00, 0.00))

frank2 = Turtle()
frank2.shape("square")
frank2.shapesize(stretch_wid=1, stretch_len=1)
frank2.color("white")
frank2.goto(x=(-40.00, 0.00))




screen.exitonclick()
