# import the gui module tkinter
from tkinter import *

# Color for BUTTONS Hex: #D4D4D2
# Color for LABLE Hex: #1C1C1C
# Color for AC, +/-, % Hex: #505050
# Color for OPERATORS Hex: #FF9500

# we want to create the window first
window = Tk()

# If we want the buttons to do things we need to create a function
def button1_clicked():
	

	return 0


# creating a label widget
result_field = Label(text = '0',
					fg='white', width=25,
					height=4, 
					bg = '#505050', 
					justify = RIGHT)
result_field.grid(row = 0, column = 0, columnspan=3)

#creating the button widgets
# the parameter for Button(where we want it = window, text = "what will be displayed")
# first parameter is where we want the button
# second is the text for the button
# we can use padx and pady to set dimensions of button
# command=myFunction will then trigger the function we defined
button_1 = Button(window, text = "1", padx=30, pady=30, command= button1_clicked)
button_2 = Button(window, text = "2", padx=30, pady=30)
button_3 = Button(window, text = "3", padx=30, pady=30)
button_4 = Button(window, text = "4", padx=30, pady=30)
button_5 = Button(window, text = "5", padx=30, pady=30)
button_6 = Button(window, text = "6", padx=30, pady=30)
button_7 = Button(window, text = "7", padx=30, pady=30)
button_8 = Button(window, text = "8", padx=30, pady=30)
button_9 = Button(window, text = "9", padx=30, pady=30)
button_0 = Button(window, text = "0", padx=30, pady=30)

# positioning the buttons on the screen

button_1.grid(row = 1 , column = 0)
button_2.grid(row = 1 , column = 1)
button_3.grid(row = 1 , column = 2)

button_4.grid(row = 2 , column = 0)
button_5.grid(row = 2 , column = 1)
button_6.grid(row = 2 , column = 2)

button_7.grid(row = 3 , column = 0)
button_8.grid(row = 3 , column = 1)
button_9.grid(row = 3 , column = 2)

button_0.grid(row = 4 , column = 1)



window.mainloop()

