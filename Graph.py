import MainPage
from helper import *
#from MainPage import MainPage


class Graph(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

    def draw_graph(self):
        tkinter.Button(self, text="Main Page", font=FONT,
                       command=lambda: self.reset_frame()).pack()

        params = self.controller.frames[MainPage]
        # for multiple machines
        # n, m, seed_d, dev_d, seed_p, dev_p = (int(params.n.get()), int(params.m.get()), params.seed_d_var.get(),
        #                                      params.dev_d_var.get(), params.seed_p_var.get(), params.dev_p_var.get())
        # for 1 machine
        n, m, seed_d, dev_d, seed_p, dev_p = (int(params.n.get()), 1, params.seed_d_var.get(),
                                              params.dev_d_var.get(), params.seed_p_var.get(), params.dev_p_var.get())

        f = Figure(figsize=(4, 4), dpi=75)
        a = f.add_subplot(1, 1, 1)
        a.set_title('seed_d: {}, dev_d: {}, seed_p: {}, dev_p: {}'.format(seed_d, dev_d, seed_p, dev_p))

        y_opt = []
        y_algo = []
        y_pinedo = []

        #jobs_arr = generator(n_iter=100, n_jobs=n, n_machines=m, seed_d=seed_d, dev_d=dev_d, seed_p=seed_p, dev_p=dev_p)

        # for arr in jobs_arr:
        #     n, m, d, jobs = arr[0], arr[1], arr[2], arr[3]
            #if min(jobs) > d or polinomial_criterium(n, m, d, jobs):
            #    continue
            #opt_result = tardiness(equal_machines_good_due_date(n, m, 9999, jobs), 9999)
            # algo_result = tardiness_with_preprocessing(algo(n, m, d, jobs), d)
            # pinedo_result = tardiness_with_preprocessing(pinedo_multiple_machines(n, m, d, jobs), d)
            #
            # y_opt.append(opt_result)
            # y_algo.append(algo_result)
        #     y_pinedo.append(pinedo_result)
        #
        # x = linspace(1, 100, num=len(y_algo))
        # a.plot(x, y_opt, 'ro', x, y_algo, 'b--', x, y_pinedo, 'g--')
        # a.legend(['perfect', '2.1', '2.2'])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        return self

    def reset_frame(self):
        for child in self.winfo_children():
            child.destroy()
        self.controller.frames[MainPage].tkraise()