from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.level = 1
        self.goto(x=-290, y=270)
        self.hideturtle()
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def counter(self):
        self.level += 1
        self.increase_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
