import MainPage
from params import *
from numpy import linspace
import matplotlib.pyplot as plt
from scheduling import decide


class Graph(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        self.filename = ''

    def reset_frame(self):
        for child in self.winfo_children():
            child.destroy()
        from Test import Test
        self.controller.frames[Test].tkraise()

    def set(self, stringvar):
        self.filename = stringvar.get()

    def get_schedule(self):
        with open(self.filename, 'r') as f:
            num_d = int(f.readline())
            num_jobs = []
            jobs = []
            d = []

            for _ in range(num_d):
                num_jobs.append(int(f.readline()))
                jobs.append([int(job) for job in f.readline().split()])
                d.append(int(f.readline()))
            num_machines = [int(num) for num in f.readline().split()]
            machines = [int(machine) for machine in f.readline().split()]
        return decide(num_d, num_jobs, jobs, d, num_machines, machines)

    def draw_graph(self):
        self.button = tkinter.Button(self, text='Назад', font=font, command=lambda: self.reset_frame()).pack()

        schedule = self.get_schedule()

        fig, gnt = plt.subplots()

        gnt.set_ylim(0, 50)
        gnt.set_xlim(0, 160)

        gnt.set_xlabel('Час')
        gnt.set_ylabel('Машина')

        gnt.set_yticks([15, 25, 35])
        gnt.set_yticklabels(['1', '2', '3'])

        gnt.grid(True)

        gnt.broken_barh([(40, 50)], (30, 9), facecolors=('tab:orange'))

        gnt.broken_barh([(110, 10), (150, 10)], (10, 9), facecolors='tab:blue')

        gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9), facecolors=('tab:red'))

        # f = Figure(figsize=(4, 4), dpi=75)
        # a = f.add_subplot(1, 1, 1)
        # a.set_title('kek')
        #
        # x = linspace(1, 100, num=10)
        # a.plot(x, [l*2 for l in x], 'ro', x, [l+2 for l in x], 'b--', x, x, 'g--')
        # a.legend(['perfect', '2.1', '2.2'])

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        return self
