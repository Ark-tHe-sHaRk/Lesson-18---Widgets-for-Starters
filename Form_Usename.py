#Importing nessasary modules
from tkinter import *
from datetime import date

#Create Window
screen = Tk()
screen.title = ('Ark Forms')
screen.geometry = ('400x300')

#Add widgets:
#Adding a Label
lbl = Label(text = 'Hey There!!!!', fg = 'white', bg = '#072F5F', height = 1, width = 300)

#Add label for getting name as input from the user
#Use entry widget to create a text box for the user to enter details
name_lbl = Label(text = 'Full Name', bg = '#3895D3')
name_entry = Entry()

#Function to display message
def display():

    #Read the input given by the user
    name = name_entry.get()

    #Declaring a global variable to make acsessable anywhere in the program 
    global message 
    message = "Welcome to the application! \nToday's date is: "
    greet = "Hello " +name+ '\n'

    #Displaying details in a text box
    #Specify where to add the detail inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

#Add a text widget to display information/messages
text_box = Text(height = 3)

#Add button and give value of command as the naem of the function 
#Press button, display function will be called automatically
btn = Button(text = "Begin", command = display, height = 1, bg = "#1261A0", fg  = "white")

#Organise all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
screen.mainloop()