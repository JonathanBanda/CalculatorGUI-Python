# import the gui module tkinter
from tkinter import *

# Color for BUTTONS Hex: #D4D4D2
# Color for LABLE Hex: #1C1C1C
# Color for AC, +/-, % Hex: #505050
# Color for OPERATORS Hex: #FF9500

# we want to create the window first
window = Tk()
window.title('Python Calculator')


# If we want the buttons to do things we need to create a function
def button_clicked(number):
    start = result_field.get()
    result_field.delete(0, END)
    result_field.insert(0, start + number)


def button_multiply_clicked(number):
    currentNumber = result_field.get()
    result_field.delete(0, END)

def button_divide_clicked(number):
    return


def button_add_clicked(number):
    return


def button_subtract_clicked(number):
    return


def button_equal_clicked(number):
    return


def button_clear_clicked(number):
    result_field.delete(0, END)


# creating a label widget
result_field = Entry(text='0', fg='black', width=25, )

result_field.grid(row=0, column=0, columnspan=5)

# creating the button widgets
# the parameter for Button(where we want it = window, text = "what will be displayed")
# first parameter is where we want the button
# second is the text for the button
# we can use padx and pady to set dimensions of button
# command=myFunction will then trigger the function we defined
button_1 = Button(window, text="1", padx=21, pady=20, command=lambda: button_clicked("1"))
button_2 = Button(window, text="2", padx=21, pady=20, command=lambda: button_clicked("2"))
button_3 = Button(window, text="3", padx=21, pady=20, command=lambda: button_clicked("3"))
button_4 = Button(window, text="4", padx=21, pady=20, command=lambda: button_clicked("4"))
button_5 = Button(window, text="5", padx=21, pady=20, command=lambda: button_clicked("5"))
button_6 = Button(window, text="6", padx=21, pady=20, command=lambda: button_clicked("6"))
button_7 = Button(window, text="7", padx=21, pady=20, command=lambda: button_clicked("7"))
button_8 = Button(window, text="8", padx=21, pady=20, command=lambda: button_clicked("8"))
button_9 = Button(window, text="9", padx=21, pady=20, command=lambda: button_clicked("9"))
button_0 = Button(window, text="0", padx=21, pady=20, command=lambda: button_clicked("0"))

button_multipy = Button(window, text=" * ", padx=18, pady=20, command=lambda: button_multiply_clicked())
button_divide = Button(window, text="/", padx=23, pady=20, command=lambda: button_divide_clicked())
button_add = Button(window, text="+", padx=21, pady=20, command=lambda: button_add_clicked())
button_subtract = Button(window, text="-", padx=21, pady=20, command=lambda: button_subtract_clicked())

button_equal = Button(window, text="=", padx=21, pady=20, command=lambda: button_equal_clicked())
button_clear = Button(window, text="Clear", padx=39, pady=20, command=lambda: button_clear_clicked())
# positioning the buttons on the screen

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_multipy.grid(row=1, column=4)
button_divide.grid(row=2, column=4)
button_add.grid(row=3, column=4)
button_subtract.grid(row=4, column=4)

button_equal.grid(row=4, column=4)
button_clear.grid(row=4, column=1, columnspan=2)

window.mainloop()
