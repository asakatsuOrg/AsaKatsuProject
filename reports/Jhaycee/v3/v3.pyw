# from dataUpdate import *


# qwe = input()
# s = select_item(f"{qwe}%")
# print(s)

from tkinter import Tk, Frame, Label
from PIL import ImageTk, Image
from time import sleep
from dambalasik import main_window

flash = Tk()

width_of_window = 700
height_of_window = 350
screen_width = flash.winfo_screenwidth()
screen_height = flash.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
flash.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

flash.overrideredirect(1)

def new_win():
    main_window()

Frame(flash, width=700, height=350, bg='#272727').place(x=0, y=0)
label1 = Label(flash, text='Dambalasik', fg='white', bg='#272727', font=("Dream MMA", 45, 'bold')).place(x=38,y=80)
label1 = Label(flash, text='Loading...', fg='white', bg='#272727', font=("Calibri", 25, 'bold')).place(x=260,y=150)


image_a = ImageTk.PhotoImage(Image.open('p1.jpg'))
image_b = ImageTk.PhotoImage(Image.open('p2.jpg'))


for i in range(3):
    l1 = Label(flash, image=image_b, border=0, relief='sunken').place(x=190, y=220)
    l2 = Label(flash, image=image_a, border=0, relief='sunken').place(x=260, y=220)
    l3 = Label(flash, image=image_a, border=0, relief='sunken').place(x=330, y=220)
    l4 = Label(flash, image=image_a, border=0, relief='sunken').place(x=400, y=220)
    flash.update_idletasks()
    sleep(0.5)

    l1 = Label(flash, image=image_a, border=0, relief='sunken').place(x=190, y=220)
    l2 = Label(flash, image=image_b, border=0, relief='sunken').place(x=260, y=220)
    l3 = Label(flash, image=image_a, border=0, relief='sunken').place(x=330, y=220)
    l4 = Label(flash, image=image_a, border=0, relief='sunken').place(x=400, y=220)
    flash.update_idletasks()
    sleep(0.5)

    l1 = Label(flash, image=image_a, border=0, relief='sunken').place(x=190, y=220)
    l2 = Label(flash, image=image_a, border=0, relief='sunken').place(x=260, y=220)
    l3 = Label(flash, image=image_b, border=0, relief='sunken').place(x=330, y=220)
    l4 = Label(flash, image=image_a, border=0, relief='sunken').place(x=400, y=220)
    flash.update_idletasks()
    sleep(0.5)

    l1 = Label(flash, image=image_a, border=0, relief='sunken').place(x=190, y=220)
    l2 = Label(flash, image=image_a, border=0, relief='sunken').place(x=260, y=220)
    l3 = Label(flash, image=image_a, border=0, relief='sunken').place(x=330, y=220)
    l4 = Label(flash, image=image_b, border=0, relief='sunken').place(x=400, y=220)
    flash.update_idletasks()
    sleep(0.5)

flash.destroy()
new_win()
flash.mainloop()