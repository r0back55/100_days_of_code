import colorgram
import random
from turtle import Turtle, Screen


# Extract 10 colors from an image
# colors = colorgram.extract('image.jpg', 30)


def extract_colors(image):
    color_list = []
    for i in range(len(image) - 1):
        rgb = image[i].rgb
        color = (rgb[0], rgb[1], rgb[2])
        color_list.append(color)
    return color_list


# extracted_colors = extract_colors(colors)
# print(extracted_colors)


extracted_colors = [(242, 242, 240), (46, 116, 78), (150, 70, 48), (22, 26, 38), (153, 23, 17),
                    (60, 28, 22), (24, 50, 37), (224, 229, 235), (135, 23, 30), (68, 21, 29),
                    (21, 93, 59), (200, 171, 87), (224, 213, 97), (166, 165, 52), (142, 65, 77),
                    (128, 179, 143), (206, 230, 220), (208, 129, 141), (191, 91, 103), (68, 89, 125),
                    (211, 75, 63), (80, 156, 110), (237, 217, 224), (144, 162, 182), (35, 50, 121),
                    (154, 214, 182), (71, 79, 35), (231, 166, 179), (90, 117, 182)]

# ------------------------------------------------------------------
# 100 dots painting
# 10 rows, 10 columns
# dot size = 20, space between = 50
screen = Screen()
screen.colormode(255)

franklin = Turtle()
franklin.penup()
franklin.hideturtle()


# setting Franklin's start position
franklin.setheading(180)
franklin.forward(250)
franklin.left(90)
franklin.forward(250)
franklin.setheading(0)

# Drawing the painting
for row in range(1, 11):
    for row_dot in range(10):
        franklin.dot(20, random.choice(extracted_colors))
        franklin.forward(50)
    franklin.teleport(-250, -250 + (50 * row))


screen.exitonclick()
