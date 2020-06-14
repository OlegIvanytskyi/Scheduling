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

        return data

    def generate_two_due_dates(self, num_jobs, d_dist, jobs_dist, num_machines, machines_dist):
        data = []

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
                                    data.append(self.generate_one_due_date(num_jobs, d_dist, jobs_dist,
                                                                           num_machines, machines_dist))
                                elif self.num_d == 2:
                                    data.append(self.generate_two_due_dates(num_jobs, d_dist, jobs_dist,
                                                                            num_machines, machines_dist))
            return data
        else:
            if self.num_d == 1:
                return self.generate_one_due_date(self.num_jobs, self.d_dist, self.jobs_dist,
                                                  self.num_machines, self.machines_dist)
            elif self.num_d == 2:
                return self.generate_two_due_dates(self.num_jobs, self.d_dist, self.jobs_dist,
                                                   self.num_machines, self.machines_dist)
