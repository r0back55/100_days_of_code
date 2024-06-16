from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()


# Buttons
def action():
    print("Do something")


# calls action when pressed
button = Button(text="Click me", command=action)
button.pack()

# Entries
entry_field = Entry(width=30)
# ad some text to begin with
entry_field.insert(END, string="Some text to begin with")
# gets text in entry
print(entry_field.get())
entry_field.pack()

# Text
text = Text(height=5, width=30)
# puts cursor in textbox
text.focus()
# adds some text to begin with
text.insert(END, "Example of multi-line text entry")
# gets the current value in textbox at line 1, character 0 (index)
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=5, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# called with current scale value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # prints 1 if button checked, otherwise 0
    print(checked_state.get())


# "checked_state" is variable to hold on checked state, 0 for off, 1 for on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option_1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option_2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


# always at the wary end
window.mainloop()
