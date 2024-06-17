from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    if reps % 2 != 0:
        countdown(work_sec)
        title.config(text="Work", fg=GREEN)
    elif reps % 2 == 0 and reps % 8 != 0:
        countdown(short_break)
        title.config(text="Short break", fg=PINK)
    else:
        countdown(long_break)
        title.config(text="Long break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# we need Event Driven loop
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for session in range(work_sessions):
            marks += "✔"
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, background=YELLOW)


# Canvas to use image
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


# Title text = fg as foreground
title = Label(text="Timer", background=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Creating Text field with '✔' output
check_marks = Label(width=12, background=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
