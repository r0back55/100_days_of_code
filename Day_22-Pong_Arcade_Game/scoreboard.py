from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score_left = 0
        self.score_right = 0
        self.goto(x=0, y=240)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write("SCORE" + '\n', align=ALIGNMENT, font=FONT)
        self.write(f"{self.score_left}  vs. {self.score_right}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Courier', 24, 'normal'))

    def counter_left(self):
        self.score_left += 1
        self.update_score()

    def counter_right(self):
        self.score_right += 1
        self.update_score()
