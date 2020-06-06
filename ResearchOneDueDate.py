from params import *
import Gantt


class ResearchOneDueDate(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        arr = ['S', 'M', 'L']

        self.button = tkinter.Button(self, text='Назад', font=font, bg=light_grey_color, fg=dark_grey_color,
                                     command=lambda: self.reset_frame()).grid(row=0, columnspan=2, sticky='W')

        tkinter.Label(self, text='Параметри генератора', font=font_header).grid(row=1, columnspan=2, padx=275, pady=50)

        tkinter.Label(self, text='Розмір директивного строку', font=font).grid(row=2, column=0, padx=20, pady=10)
        self.d_var = tkinter.StringVar()
        self.d_var.set(arr[0])
        self.d_menu = tkinter.OptionMenu(self, self.d_var, *arr)
        self.d_menu.config(font=font)
        self.d_menu.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        tkinter.Label(self, text='Розмір директивного строку', font=font).grid(row=3, column=0, padx=20, pady=10)
        self.d_var = tkinter.StringVar()
        self.d_var.set(arr[0])
        self.d_menu = tkinter.OptionMenu(self, self.d_var, *arr)
        self.d_menu.config(font=font)
        self.d_menu.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        tkinter.Label(self, text='Розмір директивного строку', font=font).grid(row=4, column=0, padx=20, pady=10)
        self.d_var = tkinter.StringVar()
        self.d_var.set(arr[0])
        self.d_menu = tkinter.OptionMenu(self, self.d_var, *arr)
        self.d_menu.config(font=font)
        self.d_menu.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        tkinter.Label(self, text='Розмір директивного строку', font=font).grid(row=5, column=0, padx=20, pady=10)
        self.d_var = tkinter.StringVar()
        self.d_var.set(arr[0])
        self.d_menu = tkinter.OptionMenu(self, self.d_var, *arr)
        self.d_menu.config(font=font)
        self.d_menu.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        tkinter.Label(self, text='Розмір директивного строку', font=font).grid(row=6, column=0, padx=20, pady=10)
        self.d_var = tkinter.StringVar()
        self.d_var.set(arr[0])
        self.d_menu = tkinter.OptionMenu(self, self.d_var, *arr)
        self.d_menu.config(font=font)
        self.d_menu.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        tkinter.Button(self, text='Продовжити', font=font_bold,
                       command=lambda: self.kek()).grid(row=7, column=0, pady=50)
        tkinter.Button(self, text='Повне дослідження', font=font_bold,
                       command=lambda: self.kek()).grid(row=7, column=1, pady=50, sticky='w')

        #
        # tkinter.Button(self, text='Submit', font=font,
        #                command=lambda: controller.frames[Gantt].draw_graph().tkraise()).grid(columnspan=2, pady=12)

    def reset_frame(self):
        from MainPage import MainPage
        self.controller.frames[MainPage].tkraise()

    def kek(self):
        print('kek')
