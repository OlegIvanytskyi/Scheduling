from helper import *
from Graph import Graph
from TestOneDueDate import TestOneDueDate
from TestTwoDueDates import TestTwoDueDates
from ResearchOneDueDate import ResearchOneDueDate
from ResearchTwoDueDates import ResearchTwoDueDates


class MainPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        tkinter.Label(self,
                      text='Вітаємо в системі з підтримки дослідження\nалгоритмів розв\'язання задач теорії розкладів',
                      font=font_header).grid(row=0, columnspan=2, pady=12)

        tkinter.Label(self, text='Тестування', font=font_bold).grid(row=1, columnspan=2, pady=12)

        tkinter.Button(self, text='Алгоритми з одним директивним строком', font=font,
                       command=lambda: controller.frames[TestOneDueDate].tkraise()).grid(row=2, column=0, sticky='nwes')
        tkinter.Button(self, text='Алгоритми з двома директивними строками', font=font,
                       command=lambda: controller.frames[TestTwoDueDates].tkraise()).grid(row=2, column=1, sticky='nwes')

        tkinter.Label(self, text='Дослідження', font=font_bold).grid(row=3, columnspan=2, pady=12)

        tkinter.Button(self, text='Системи з одним директивним строком', font=font,
                       command=lambda: controller.frames[ResearchOneDueDate].tkraise()).grid(row=4, column=0, sticky='nwes')
        tkinter.Button(self, text='Системи з двома директивними строками', font=font,
                       command=lambda: controller.frames[ResearchTwoDueDates].tkraise()).grid(row=4, column=1, sticky='nwes')
