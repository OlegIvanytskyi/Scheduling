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

        tkinter.Label(self, text='Розмір директивного строку', font=font).grid(row=2, column=0, pady=20)


        # tkinter.Label(self, text='Parameters', font=font).grid(columnspan=2, pady=12)
        #
        # tkinter.Label(self, text='Enter number of jobs: ', font=font).grid(row=1, column=0, pady=5)
        # self.n = tkinter.Entry(self, font=font)
        # self.n.grid(row=1, column=1, pady=5)
        #
        # tkinter.Label(self, text='Enter number of machines: ', font=font).grid(row=2, column=0, pady=5)
        # self.m = tkinter.Entry(self, font=font)
        # self.m.grid(row=2, column=1, pady=5)
        #
        # size_arr = ['S', 'M', 'L']
        #
        # tkinter.Label(self, text='Choose the size of mean due date: ', font=font).grid(row=3, column=0, pady=5)
        # self.seed_d_var = tkinter.StringVar()
        # self.seed_d_var.set('S')
        # self.seed_d_menu = tkinter.OptionMenu(self, self.seed_d_var, *size_arr)
        # self.seed_d_menu.config(font=font)
        # self.seed_d_menu.grid(row=3, column=1, sticky='ew', pady=5)
        #
        # tkinter.Label(self, text='Choose the size of deviation of due date: ', font=font).grid(row=4, column=0, pady=5)
        # self.dev_d_var = tkinter.StringVar()
        # self.dev_d_var.set('S')
        # self.dev_d_menu = tkinter.OptionMenu(self, self.dev_d_var, *size_arr)
        # self.dev_d_menu.config(font=font)
        # self.dev_d_menu.grid(row=4, column=1, sticky='ew', pady=5)
        #
        # tkinter.Label(self, text='Choose the size of mean p: ', font=font).grid(row=5, column=0, pady=5)
        # self.seed_p_var = tkinter.StringVar()
        # self.seed_p_var.set('S')
        # self.seed_p_menu = tkinter.OptionMenu(self, self.seed_p_var, *size_arr)
        # self.seed_p_menu.config(font=font)
        # self.seed_p_menu.grid(row=5, column=1, sticky='ew', pady=5)
        #
        # tkinter.Label(self, text='Choose the size of deviation of p: ', font=font).grid(row=6, column=0, pady=5)
        # self.dev_p_var = tkinter.StringVar()
        # self.dev_p_var.set('S')
        # self.dev_p_menu = tkinter.OptionMenu(self, self.dev_p_var, *size_arr)
        # self.dev_p_menu.config(font=font)
        # self.dev_p_menu.grid(row=6, column=1, sticky='ew', pady=5)
        #
        # tkinter.Button(self, text='Submit', font=font,
        #                command=lambda: controller.frames[Gantt].draw_graph().tkraise()).grid(columnspan=2, pady=12)

    def reset_frame(self):
        from MainPage import MainPage
        self.controller.frames[MainPage].tkraise()