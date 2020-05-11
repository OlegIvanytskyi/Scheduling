from helper import *
from MainPage import MainPage
from Graph import Graph
from TestOneDueDate import TestOneDueDate
from TestTwoDueDates import TestTwoDueDates
from ResearchOneDueDate import ResearchOneDueDate
from ResearchTwoDueDates import ResearchTwoDueDates


class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        tkinter.Tk.wm_title(self, 'Scheduling')
        tkinter.Tk.geometry(self, '775x300')

        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frames[MainPage] = MainPage(container, self)
        self.frames[MainPage].grid(row=0, column=0, sticky='nsew')

        self.frames[TestOneDueDate] = TestOneDueDate(container, self)
        self.frames[TestOneDueDate].grid(row=0, column=0, sticky='nsew')

        self.frames[TestTwoDueDates] = TestTwoDueDates(container, self)
        self.frames[TestTwoDueDates].grid(row=0, column=0, sticky='nsew')

        self.frames[ResearchOneDueDate] = ResearchOneDueDate(container, self)
        self.frames[ResearchOneDueDate].grid(row=0, column=0, sticky='nsew')

        self.frames[ResearchTwoDueDates] = ResearchTwoDueDates(container, self)
        self.frames[ResearchTwoDueDates].grid(row=0, column=0, sticky='nsew')

        self.frames[Graph] = Graph(container, self)
        self.frames[Graph].grid(row=0, column=0, sticky='nsew')

        self.frames[MainPage].tkraise()
