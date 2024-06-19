from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

BACKGROUND = '#ffffff'
FONT_NAME = "Tahoma"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = ([random.choice(letters) for _ in range(nr_letters)] +
                     [random.choice(symbols) for _ in range(nr_symbols)] +
                     [random.choice(numbers) for _ in range(nr_numbers)])
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = entry_website.get()
    user_email = entry_user_email.get()
    passw = entry_password.get()
    new_data = {
        website: {
            "email": user_email,
            "password": passw
        }
    }

    if len(website) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open('./passwords.json', mode='r') as data_file:
                # reading current data from JSON
                data = json.load(data_file)
        except FileNotFoundError:
            with open('./passwords.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating JSON with new entry
            data.update(new_data)

            with open('./passwords.json', mode='w') as data_file:
                # saving updated data to JSON
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)  # from index to index
            entry_password.delete(0, END)  # from index to index


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_website.get()

    try:
        with open('./passwords.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f'Email: {data[website]["email"]} \n '
                                                       f'Password: {data[website]["password"]}')
        else:
            messagebox.showinfo(title="Error", message="No password found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, background=BACKGROUND)


# Adding background image
canvas = Canvas(width=200, height=200, background=BACKGROUND, highlightthickness=0)
locker_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=locker_image)
canvas.grid(column=1, row=0)


# Text Labels
l_website = Label(text="Website:", background=BACKGROUND, font=(FONT_NAME, 10, "normal"))
l_website.grid(column=0, row=1)

l_email = Label(text="Email/Username:", background=BACKGROUND, font=(FONT_NAME, 10, "normal"))
l_email.grid(column=0, row=2)

l_password = Label(text="Password:", background=BACKGROUND, font=(FONT_NAME, 10, "normal"))
l_password.grid(column=0, row=3)


# Input/Entry fields
entry_website = Entry(width=20)
entry_website.focus()
entry_website.grid(column=1, row=1)

entry_user_email = Entry(width=40)
entry_user_email.insert(0, string="r0back55@gmail.com")
entry_user_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=20)
entry_password.insert(END, string="")
entry_password.grid(column=1, row=3)


# Buttons
b_search = Button(text="Search", width=18, command=find_password)
b_search.grid(column=2, row=1)

b_gen_pass = Button(text="Generate Password", width=18, command=gen_password)
b_gen_pass.grid(column=2, row=3)

b_add = Button(text="Add", width=38, command=add_password)
b_add.grid(column=1, row=4, columnspan=2)


# ------------------------------------------------------------------------------------
window.mainloop()
