from tkinter import *


def miles_to_km():
    value = float(entry_field.get())
    new_value = round(1.609 * value, 2)
    output.config(text=new_value)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)

# Creating labels
label_miles = Label(text="Miles")

label_miles.grid(column=2, row=0)
label_is_equal_to = Label(text="is equal to:")
label_is_equal_to.grid(column=0, row=1)

label_km = Label(text="Km")
label_km.grid(column=3, row=1)


# Creating Entry field
entry_field = Entry(width=10)
entry_field.insert(END, string="0")
entry_field.grid(column=1, row=0, padx=3, pady=3)


# Creating Text field with output
output = Label(text="0", width=8, borderwidth=1, relief="solid")
output.grid(column=1, row=1, padx=3, pady=3)


# Creating Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2, padx=3, pady=3)


# -------------------------------------------
# always at the wary end
window.mainloop()
