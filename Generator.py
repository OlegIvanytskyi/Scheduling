import random

class Generator:
    def __init__(self, num_d, params=None):
        self.num_d = num_d

        if params:
            self.full_research = False

            self.num_jobs = params[0]
            self.d_dist = params[1]
            self.jobs_dist = params[2]
            self.num_machines = params[3]
            self.machines_dist = params[4]
        else:
            self.full_research = True

    def generate_one_due_date(self, num_jobs, d_dist, jobs_dist, num_machines, machines_dist):
        data = []

        for _ in range(100):
            if num_machines == 'S':
                n_machines = 1
            elif num_jobs == 'M':
                n_machines = 3
            else:
                n_machines = 10

            machines = []
            for machine in range(n_machines):
                if machines_dist == 'S':
                    machines.append(1)
                elif machines_dist == 'M':
                    machines.append(random.uniform(0.5, 3))
                else:
                    machines.append(random.uniform(0.5, 10))

            if num_jobs == 'S':
                n_jobs = n_machines * 5
            elif num_jobs == 'M':
                n_jobs = n_machines * 10
            else:
                n_jobs = n_machines * 20

            if jobs_dist == 'S':
                jobs = [random.randint(1, 10) for _ in range(num_jobs)]
            elif jobs_dist == 'M':
                jobs = [random.randint(1, 20) for _ in range(num_jobs)]
            else:
                jobs = [random.randint(1, 50) for _ in range(num_jobs)]

            if d_dist == 'S':
                d = [min(jobs) - 1]
            elif d_dist == 'M':
                d = [sum(jobs) / 2 - 1]
            else:
                d = [sum(jobs)]

            data.append([1, d, [jobs, []], n_machines, machines])

        return data

    def generate_two_due_dates(self, num_jobs, d_dist, jobs_dist, num_machines, machines_dist):
        data = []

        for _ in range(100):
            if num_machines == 'S':
                n_machines = 1
            elif num_jobs == 'M':
                n_machines = 3
            else:
                n_machines = 10

            machines = []
            for machine in range(n_machines):
                if machines_dist == 'S':
                    machines.append(1)
                elif machines_dist == 'M':
                    machines.append(random.uniform(0.5, 3))
                else:
                    machines.append(random.uniform(0.5, 10))

            if num_jobs == 'S':
                n_jobs = n_machines * 5
            elif num_jobs == 'M':
                n_jobs = n_machines * 10
            else:
                n_jobs = n_machines * 20

            if jobs_dist == 'S':
                jobs = [[random.randint(1, 5) for _ in range(num_jobs / 2)],
                        [random.randint(1, 5) for _ in range(num_jobs / 2)]]
            elif jobs_dist == 'M':
                jobs = [[random.randint(1, 10) for _ in range(num_jobs / 2)],
                        [random.randint(1, 10) for _ in range(num_jobs / 2)]]
            else:
                jobs = [[random.randint(1, 20) for _ in range(num_jobs / 2)],
                        [random.randint(1, 20) for _ in range(num_jobs / 2)]]

            d = [random.randint(min(jobs[0]) - 1, sum(jobs[0]))]
            if d_dist == 'S':
                d.append(d[0] + min(jobs[1]) - 1)
            elif d_dist == 'M':
                d.append(d[0] + sum(jobs[1]) / 2 - 1)
            else:
                d.append(d[0] + sum(jobs[1]))

            data.append([1, d, jobs, n_machines, machines])

        return data

    def generate(self):
        if self.full_research:
            arr = ['S', 'M', 'L']
            data = []
            for num_jobs in arr:
                for d_dist in arr:
                    for jobs_dist in arr:
                        for num_machines in arr:
                            for machines_dist in arr:
                                if self.num_d == 1:
                                    data += self.generate_one_due_date(num_jobs, d_dist, jobs_dist,
                                                                       num_machines, machines_dist)
                                elif self.num_d == 2:
                                    data += self.generate_two_due_dates(num_jobs, d_dist, jobs_dist,
                                                                        num_machines, machines_dist)
            return data
        else:
            if self.num_d == 1:
                return self.generate_one_due_date(self.num_jobs, self.d_dist, self.jobs_dist,
                                                  self.num_machines, self.machines_dist)
            elif self.num_d == 2:
                return self.generate_two_due_dates(self.num_jobs, self.d_dist, self.jobs_dist,
                                                   self.num_machines, self.machines_dist)
