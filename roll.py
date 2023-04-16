from logging import root
import tkinter
from PIL import Image, ImageTk
import random

# Creating front end of the widget
root = tkinter.Tk()
root.geometry('600x400')
root.title("Rolling Dice")

# label of the form
Roll = tkinter.Label(root, text="")
Roll.pack()

# label woth different front formatting
Roll1 = tkinter.Label(root, text="Press the Button to ROLL", fg="black",
                      bg="Grey",
                      font="Helvetica 16 bold italic")
Roll1.pack()

# img
roller = ['d1.jpg', 'd2.jpg', 'd3.jpg', 'd4.jpg', 'd5.jpg', 'd6.jpg']
# simulating the dice with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(roller)))


tag1 = tkinter.Label(root, image=image1)
tag1.image = image1


tag1.pack(expand=True)


def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(roller)))
    # update image
    tag1.configure(image=image1)
    # keep a reference
    tag1.image = image1


btn = tkinter.Button(root, text='ROLL',
                     fg='green', bg="white", command=rolling_dice)


btn.pack(expand=True)


root.mainloop()
