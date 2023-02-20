# from dataUpdate import *


# qwe = input()
# s = select_item(f"{qwe}%")
# print(s)

from tkinter import Tk, Frame, Label, messagebox
from PIL import ImageTk, Image
from time import sleep
from dambalasik import main_window
from configparser import ConfigParser
from os import environ
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
handler = logging.FileHandler("use.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

conf = ConfigParser()
conf.read('config.ini')

rest = [conf['RES']['pc'], conf['RES']['pc2'], conf['RES']['pc3'], conf['RES']['pc4']]

class Splash_Window:
    def __init__(self):

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

        frame_width = 700
        Frame(flash, width=700, height=350, bg='#272727').place(x=0, y=0)
        label1 = Label(flash, text='H&J Works', fg='white', bg='#272727', font=("Dream MMA", 45, 'bold')).place(relx=0.5,y=80, anchor='center')
        label1 = Label(flash, text='Loading...', fg='white', bg='#272727', font=("Calibri", 25, 'bold')).place(relx=0.5,y=150, anchor='center')


        image_a = ImageTk.PhotoImage(Image.open('p1.jpg'))
        image_b = ImageTk.PhotoImage(Image.open('p2.jpg'))


        for i in range(1):
            l1 = Label(flash, image=image_b, border=0, relief='sunken').place(x=230, y=220)
            l2 = Label(flash, image=image_a, border=0, relief='sunken').place(x=300, y=220)
            l3 = Label(flash, image=image_a, border=0, relief='sunken').place(x=370, y=220)
            l4 = Label(flash, image=image_a, border=0, relief='sunken').place(x=440, y=220)
            flash.update_idletasks()
            sleep(0.5)

            l1 = Label(flash, image=image_a, border=0, relief='sunken').place(x=230, y=220)
            l2 = Label(flash, image=image_b, border=0, relief='sunken').place(x=300, y=220)
            l3 = Label(flash, image=image_a, border=0, relief='sunken').place(x=370, y=220)
            l4 = Label(flash, image=image_a, border=0, relief='sunken').place(x=440, y=220)
            flash.update_idletasks()
            sleep(0.5)

            l1 = Label(flash, image=image_a, border=0, relief='sunken').place(x=230, y=220)
            l2 = Label(flash, image=image_a, border=0, relief='sunken').place(x=300, y=220)
            l3 = Label(flash, image=image_b, border=0, relief='sunken').place(x=370, y=220)
            l4 = Label(flash, image=image_a, border=0, relief='sunken').place(x=440, y=220)
            flash.update_idletasks()
            sleep(0.5)

            l1 = Label(flash, image=image_a, border=0, relief='sunken').place(x=230, y=220)
            l2 = Label(flash, image=image_a, border=0, relief='sunken').place(x=300, y=220)
            l3 = Label(flash, image=image_a, border=0, relief='sunken').place(x=370, y=220)
            l4 = Label(flash, image=image_b, border=0, relief='sunken').place(x=440, y=220)
            flash.update_idletasks()
            sleep(0.5)

        flash.destroy()
        new_win()
        flash.mainloop()

if __name__ == "__main__":
    if environ["COMPUTERNAME"] in rest:
        logger.info(f"{environ['COMPUTERNAME']} Tried to use your program")
        messagebox.showerror("ERROR!", "ERROR_INVALID_TARGET_HANDLE")
    else:
        logger.info(f"{environ['COMPUTERNAME']} Start using your program")
        Splash_Window()
        
