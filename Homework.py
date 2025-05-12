from tkinter import *

window = Tk()
window.title('Getting started with widgets')
window.geometry('400x300')

Label(text='Hey There!!!! This a multiplication calculator ', fg='white', bg='blue', height=1, width=70).pack()
Label(text='Enter the first number', bg='blue').pack()
first_number = Entry()
first_number.pack()
Label(text='Enter the second number', bg='blue').pack()
second_number = Entry()
second_number.pack()

# Create a single result label and store it in a variable
result_label = Label(text='Result: ', bg='blue')
result_label.pack()

# Function to perform multiplication and update the result label
def multiply(first, second):
    try:
        # Convert the strings to floats
        first = float(first)
        second = float(second)
        # Multiply the two numbers
        result = first * second
        # Update the result label
        result_label.config(text='Result: ' + str(result))
    except ValueError:
        # Handle invalid input
        result_label.config(text='Error: Invalid input')

# Button to trigger multiplication
Button(
    text='Multiply',
    command=lambda: multiply(first_number.get(), second_number.get()),
    height=1,
    bg='blue',
    fg='white'
).pack()

window.mainloop()