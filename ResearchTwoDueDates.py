from params import *
from Research import Research


class ResearchTwoDueDates(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        arr = ['S', 'M', 'L']

        self.button = tkinter.Button(self, text='Назад', font=font, bg=light_grey_color, fg=dark_grey_color,
                                     command=lambda: self.reset_frame()).grid(row=0, columnspan=2, sticky='W')

        tkinter.Label(self, text='Параметри генератора', font=font_header).grid(row=1, columnspan=2, padx=275, pady=50)

        tkinter.Label(self, text='Кількості робіт', font=font).grid(row=2, column=0, padx=20, pady=10, sticky='ew')
        self.n_var = tkinter.StringVar()
        self.n_var.set(arr[0])
        self.n_menu = tkinter.OptionMenu(self, self.n_var, *arr)
        self.n_menu.config(font=font)
        self.n_menu.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        tkinter.Label(self, text='Розміри директивних строків', font=font).grid(row=3, column=0, padx=20, pady=10,
                                                                                sticky='ew')
        self.d_var = tkinter.StringVar()
        self.d_var.set(arr[0])
        self.d_menu = tkinter.OptionMenu(self, self.d_var, *arr)
        self.d_menu.config(font=font)
        self.d_menu.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        tkinter.Label(self, text='Розміри робіт', font=font).grid(row=4, column=0, padx=20, pady=10, sticky='ew')
        self.jobs_var = tkinter.StringVar()
        self.jobs_var.set(arr[0])
        self.jobs_menu = tkinter.OptionMenu(self, self.jobs_var, *arr)
        self.jobs_menu.config(font=font)
        self.jobs_menu.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        tkinter.Label(self, text='Кількість машин', font=font).grid(row=5, column=0, padx=20, pady=10, sticky='ew')
        self.m_var = tkinter.StringVar()
        self.m_var.set(arr[0])
        self.m_menu = tkinter.OptionMenu(self, self.m_var, *arr)
        self.m_menu.config(font=font)
        self.m_menu.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        tkinter.Label(self, text='Продуктивності машин', font=font).grid(row=6, column=0, padx=20, pady=10, sticky='ew')
        self.h_var = tkinter.StringVar()
        self.h_var.set(arr[0])
        self.h_menu = tkinter.OptionMenu(self, self.h_var, *arr)
        self.h_menu.config(font=font)
        self.h_menu.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        tkinter.Button(self, text='Продовжити', font=font_bold,
                       command=lambda: self.research(False)).grid(row=7, column=0, pady=50)
        tkinter.Button(self, text='Повне дослідження', font=font_bold,
                       command=lambda: self.research(True)).grid(row=7, column=1, pady=50, sticky='w')

    def reset_frame(self):
        from MainPage import MainPage
        self.controller.frames[MainPage].tkraise()

    def research(self, full_research=True):
        if full_research:
            research = Research(2)
        else:
            research = Research(2, [self.n_var.get(), self.d_var.get(),
                                self.jobs_var.get(), self.m_var.get(), self.h_var.get()])
        research.research()
