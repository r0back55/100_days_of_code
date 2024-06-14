import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Importing list of states from .csv file
data = pd.read_csv("./50_states.csv")
all_states = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States",
                                    prompt="What's another state's name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item())

screen.exitonclick()
