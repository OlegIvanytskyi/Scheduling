from params import *
from MainPage import MainPage
from Test import Test
from ResearchOneDueDate import ResearchOneDueDate
from ResearchTwoDueDates import ResearchTwoDueDates


class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        tkinter.Tk.wm_title(self, 'Scheduling')
        tkinter.Tk.geometry(self, '740x600')

        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        self.frames[MainPage] = MainPage(container, self)
        self.frames[MainPage].grid(row=0, column=0, sticky='nsew')

        self.frames[Test] = Test(container, self)
        self.frames[Test].grid(row=0, column=0, sticky='nsew')

        self.frames[ResearchOneDueDate] = ResearchOneDueDate(container, self)
        self.frames[ResearchOneDueDate].grid(row=0, column=0, sticky='nsew')

        self.frames[ResearchTwoDueDates] = ResearchTwoDueDates(container, self)
        self.frames[ResearchTwoDueDates].grid(row=0, column=0, sticky='nsew')

        for _, frame in self.frames.items():
            frame.configure(bg='white')

        self.frames[MainPage].tkraise()
