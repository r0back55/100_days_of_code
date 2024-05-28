from turtle import Turtle, Screen
import random

# changing Franklin's appearance
franklin = Turtle()
franklin.shape("turtle")
franklin.color("#00FFFF")


# --------------------------------------------------------------
# Focus now Franklin - I need yo to draw me:
# 'triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon', all in one shot
color_list = [
    "#00FFFF", "#7FFF00", "#B8860B", "#FF0000", "#87CEFA",
    "#8A2BE2", "#FFD700", "#800000", "#DCDCDC", "#228B22",
    "#000000", "#0000FF", "#FFDEAD", "#FF4500", "#00FF00"]


def draw_the_shape(shape):
    angle = 360 / shape
    for wall in range(shape):
        franklin.forward(100)
        franklin.right(angle)


for shape_size in range(3, 11):
    franklin.color(random.choice(color_list))
    draw_the_shape(shape_size)
