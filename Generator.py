class Generator:
    def __init__(self, num_d=1, params=None):
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

    def generate(self):
        if self.num_d == 1:
            pass
        else:
            pass
