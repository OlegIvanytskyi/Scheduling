import matplotlib.pyplot as plt
from Schedule import Schedule


class Gantt:
    def __init__(self, path):
        self.filename = path

        with open(self.filename, 'r') as f:
            self.num_d = int(f.readline())
            self.num_jobs = []
            self.jobs = []
            self.d = []

            for _ in range(self.num_d):
                self.num_jobs.append(int(f.readline()))
                self.jobs.append([int(job) for job in f.readline().split()])
                self.d.append(int(f.readline()))
            self.num_machines = int(f.readline())
            self.machines = [int(machine) for machine in f.readline().split()]

    def get_schedule(self):
        return Schedule().build_schedule(self.num_d, self.d, self.jobs, self.num_machines, self.machines)

    def draw_graph(self):
        schedule = self.get_schedule()

        fig, gnt = plt.subplots()
        gnt.set_title('Побудований розклад')

        gnt.set_ylim(0, (self.num_machines + 1) * 10 + 10)
        gnt.set_xlim(0, max([sum([job[1] for job in machine]) for machine in schedule]) + 5)  # max of all schedules+10 # todo

        gnt.set_xlabel('Час')
        gnt.set_ylabel('Машина')

        gnt.grid(True)

        yticks = [(i + 1) * 10 + 5 for i in range(self.num_machines)]
        yticklabels = [str(i + 1) for i in range(self.num_machines)]
        gnt.set_yticks(yticks)
        gnt.set_yticklabels(yticklabels)

        # setting the schedules
        for i in range(self.num_machines):
            gnt.broken_barh(schedule[i], ((i + 1) * 10, 9),
                            facecolors=('orange', 'green', 'blue') * len(schedule),  # mark each job with diff color
                            edgecolors='black')  # color of borders
            for job in schedule[i]:
                gnt.text(x=job[0] + job[1] / 2,  # x = gorizontal position of the label (center of the bar)
                         y=(i + 1) * 10 + 4,  # y = vertical position of the label
                         s=job[1],  # text (length of the job)
                         ha='center', va='center', color='white', size=15)

        # setting the due dates
        for i in range(self.num_d):
            gnt.axvline(x=self.d[i], c='black', linewidth=5)
            # gnt.text(x=self.d[i] + 0.5, y=1, s=f'd = {self.d[i]}', color='black', size=10)  # possible way to
                                                                                              # set xtick for due date

        gnt.set_xticks(list(gnt.get_xticks()) + self.d)  # set xtick for due date

        fig.show()
