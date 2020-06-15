from Generator import Generator
from Schedule import Schedule

import matplotlib.pyplot as plt
from numpy import linspace


class Research:
    def __init__(self, num_d, params=None):
        self.num_d = num_d
        self.params = params

    def get_input(self):
        return Generator(self.num_d, self.params).generate()

    def compare(self, z_arr, perfect_arr):
        fig, plot = plt.subplots()
        plot.set_title('Дослідження')

        plot.set_ylim(0, max(max(z_arr), max(perfect_arr)))
        plot.set_xlim(0, len(z_arr))

        plot.set_xlabel('Експеримент')
        plot.set_ylabel('Цільова функція')

        plot.grid(True)

        x = linspace(1, len(z_arr), num=len(z_arr))
        plot.plot(x, z_arr, 'ro', x, perfect_arr, 'b--')
        plt.legend(['Реальна цільова функція', 'Нижня границя'])

        fig.show()

    def research(self):
        data = self.get_input()

        z_arr = []
        perfect_arr = []

        schedule = Schedule()
        for data_set in data:
            d = data_set[1]
            jobs = data_set[2]
            num_machines = data_set[3]
            machines = data_set[4]

            z_arr.append(schedule.tardiness(d, schedule.build_schedule(self.num_d, d, jobs, num_machines, machines)))

            d = [sum(jobs[0]), sum(jobs[0]) + sum(jobs[1])]
            perfect_arr.append(schedule.tardiness(d,
                                                  schedule.build_schedule(self.num_d, d, jobs, num_machines, machines)))

        self.compare(z_arr, perfect_arr)
