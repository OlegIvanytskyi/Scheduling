from params import *
from tkinter.filedialog import askopenfilename
from Gantt import Gantt


class Test(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        self.button = tkinter.Button(self, text='Назад', font=font, bg=light_grey_color, fg=dark_grey_color,
                                     command=lambda: self.reset_frame()).place(x=0, y=0)

        tkinter.Button(self, text='Оберіть файл з вхідними даними', font=font, bg=blue_color, fg='white',
                       command=lambda: self.get_filename()).pack(pady=25)

        self.literal = tkinter.Label(self, text='Обраний файл', font=font)

        self.text = tkinter.StringVar()
        self.text.set('')
        self.label = tkinter.Label(self, textvariable=self.text, font=font, borderwidth=3, relief="groove", pady=20)

        self.button = tkinter.Button(self, text='Продовжити', font=font, bg=blue_color, fg='white',
                                     command=lambda: self.call_graph())

    def get_filename(self):
        filename = askopenfilename()

        self.literal.pack(pady=10)
        self.label.pack()
        self.text.set(filename)
        self.button.pack(pady=20)

    def reset_frame(self):
        from MainPage import MainPage
        self.controller.frames[MainPage].tkraise()

    def call_graph(self):
        self.controller.frames[Gantt].set(self.text)
        self.controller.frames[Gantt].draw_graph()
