
"""
widgets = GUI elements: buttons, text-boxes, labels, images
windows = serves as a container to hold or contain these widgets`

"""

from tkinter import *
from PIL import ImageTk, Image

window= Tk() #instantiate an instance of a window

# window.geometry("720x720")
#if not specified, it will create with the exact size of label & image

window.title("GUI Panel")

icon = ImageTk.PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#56fcff")

image = ImageTk.PhotoImage(file="logo.png")
image2 = ImageTk.PhotoImage(file='click.png')

label = Label(window,
                text="Hello Python GUI", 
                font=("Arial", 40, 'bold'), 
                fg='#00FF00', 
                bg='#000000', 
                relief=RAISED, #SUNKEN
                bd=10,
                padx=20,
                pady=20,
                image=image,
                compound='bottom')
label.pack()
# label.place(x=100, y=100)

#function click

count = 0

def click():
    global count
    count +=1
    print("You clicked the button!")
    print(count)


#button
button = Button(window, 
                    text="Click Here",
                    command=click,
                    font=('Comic Sans', 20),
                    fg="#00FF00",
                    bg="#000000",
                    activeforeground="blue",
                    activebackground="red",
                    state=ACTIVE, #byDefault = Active, Disabled)
                    image=image2,
                    compound='bottom') 
button.pack()


window.mainloop() #place window on computer screen, listen for events


#test