from tkinter import *


def button_clicked():
    new_text = input_field.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label
my_label = Label(text="I am a label", font=("Arial", 18, "italic"))
my_label.config(text="New Text")
# my_label.pack()  # it packs a label on the screen, in a center, and next object right after the preceding one
# my_label.place(x=200, y=50)  # this allows to place object with a specific coordinates (x,y)
my_label.grid(column=0, row=0)  # if we use grid() all other object has to use it as well!!


# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

"""
button.grid(row=0, column=0, padx=10, pady=5)
This adds 10 pixels of horizontal padding and 5 pixels of vertical padding around the button in its grid cell.

button.config(padx=10, pady=5)
This adds 10 pixels of horizontal padding and 5 pixels of vertical padding inside the button, between its borders 
and its content.
"""

# Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)


# Entry component (input field)
input_field = Entry(width=10)
print(input_field.get())
input_field.grid(column=3, row=2)


# always at the wary end
window.mainloop()
