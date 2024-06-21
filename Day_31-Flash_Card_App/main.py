from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = {}

try:
    data_frame = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data_frame.to_dict(orient="records")


# -------------------------- WORDS RANDOMIZER -------------------------- #
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


# -------------------------- CARD FLIP -------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    words_to_learn.remove(current_card)
    data = pd.DataFrame(words_to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# -------------------------- BUILDING UI -------------------------- #
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Canvas object allows to lay a tol of things on top of each other
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="", font=('Ariel', 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=('Ariel', 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_icon = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_icon, highlightthickness=0, background='white', command=next_card)
wrong_button.grid(column=0, row=1)

right_icon = PhotoImage(file="./images/right.png")
right_button = Button(image=right_icon, highlightthickness=0, background='white', command=is_known)
right_button.grid(column=1, row=1)

next_card()

# Mainloop to keep the window open
window.mainloop()
