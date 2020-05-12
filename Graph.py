import MainPage
from helper import *
#from MainPage import MainPage


class Graph(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        self.button = tkinter.Button(self, text='Назад', font=font, command=lambda: self.reset_frame()).place(x=0, y=0)

    def reset_frame(self):
        from Test import Test
        self.controller.frames[Test].tkraise()

    def set(self, kek):
        print(kek.get())
