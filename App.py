from helper import *
from MainPage import MainPage
from Graph import Graph


class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        tkinter.Tk.wm_title(self, 'Scheduling')
        tkinter.Tk.geometry(self, '1000x500')

        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frames[MainPage] = MainPage(container, self)
        self.frames[MainPage].grid(row=0, column=0, sticky='nsew')

        self.frames[Graph] = Graph(container, self)
        self.frames[Graph].grid(row=0, column=0, sticky='nsew')

        self.frames[MainPage].tkraise()
