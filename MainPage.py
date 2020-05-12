from helper import *
from Graph import Graph
from Test import Test
from ResearchOneDueDate import ResearchOneDueDate
from ResearchTwoDueDates import ResearchTwoDueDates


class MainPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        tkinter.Label(self,
                      text='Вітаємо в системі з підтримки дослідження\nалгоритмів розв\'язання задач теорії розкладів',
                      font=font_header).grid(row=0, columnspan=2, pady=12)

        self.grid_rowconfigure(1, minsize=30)

        tkinter.Button(self, text='Тестування', font=font,
                       command=lambda: controller.frames[Test].tkraise()).grid(row=2, columnspan=2)

        self.grid_rowconfigure(3, minsize=30)

        tkinter.Label(self, text='Дослідження', font=font_bold).grid(row=4, columnspan=2, pady=12)

        tkinter.Button(self, text='Системи з одним директивним строком', font=font,
                       command=lambda: controller.frames[ResearchOneDueDate].tkraise()).grid(row=5, column=0,
                                                                                             sticky='nwes')
        tkinter.Button(self, text='Системи з двома директивними строками', font=font,
                       command=lambda: controller.frames[ResearchTwoDueDates].tkraise()).grid(row=5, column=1,
                                                                                              sticky='nwes')
