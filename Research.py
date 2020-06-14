from Generator import Generator
from Schedule import Schedule


class Research:
    def __init__(self, num_d, params=None):
        self.num_d = num_d
        self.params = params

    def get_input(self):
        return Generator(self.num_d, self.params).generate()

    def compare(self, z_arr, perfect_arr):
        pass

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
