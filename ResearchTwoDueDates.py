from params import *


class ResearchTwoDueDates(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        tkinter.Label(self,
                      text='Вітаємо в системі з підтримки дослідження\nалгоритмів розв\'язання задач теорії розкладів',
                      font=font_header).grid(row=0, columnspan=2, pady=12)

