from copy import deepcopy


class Schedule:
    def __init__(self):
        pass

    # start - zero point (moment of time which indicates the earliest possible beginning of schedule)
    def spt(self, jobs, machine=1, start=0):
        jobs = [job/machine for job in sorted(jobs)]

        schedule = []

        for job in jobs:
            schedule.append([start, job])
            start += job

        return schedule

    def tight_due_date(self, jobs, d, machine=1, start=0):
        jobs = [job/machine for job in sorted(jobs, reverse=True)]

        schedule_before_due_date = []
        schedule_after_due_date = []

        tay1 = d
        tay2 = sum(jobs) - d

        for job in jobs:
            if tay1 >= tay2:
                schedule_before_due_date.append([start, job])
                start += job
                tay1 -= job
            else:
                schedule_after_due_date.insert(0, [0, job])  # setting temporary time of start to 0
                tay2 -= job

        # setting times when the job is starting
        for job in schedule_after_due_date:
            job[0] = start
            start += job[1]

        return schedule_before_due_date + schedule_after_due_date

    def loose_due_date(self, jobs, d, machine=1):
        jobs = [job/machine for job in sorted(jobs, reverse=True)]

        schedule_before_due_date = [[0, job] for job in jobs[::2]]
        schedule_after_due_date = [[0, job] for job in jobs[1::2]][::-1]  # [::-1] is used to reverse the list

        duration = sum([job[1] for job in schedule_before_due_date])  # sum of all jobs that go before due date

        for job in schedule_before_due_date:
            job[0] = d - duration
            duration -= job[1]

        # at this point duration must be equal to 0
        duration = d

        for job in schedule_after_due_date:
            job[0] = duration
            duration += job[1]

        return schedule_before_due_date + schedule_after_due_date

    # function for moving jobs that cannot be executed between due dates
    # situation with first loose and second tight due dates (single machine)
    def move_jobs_between_due_dates(self, d, schedule):
        possible = d[1] - d[0]  # time available between due dates
        actual = 0  # time required for all jobs that are currently between due dates

        # jobs that are standing between due dates
        bad_jobs_first_due_date = []
        bad_jobs_second_due_date = []

        # jobs that must me moved + jobs that are standing on another side of due date (not problematic side)
        new_jobs_first_due_date = []
        new_jobs_second_due_date = []

        # calculate how big the duration of all jobs between due dates is and save these jobs
        for job in schedule[0]:  # schedule[0] - schedule for the first set of jobs (first due date)
            if job[0] >= d[0]:  # if time of start of the job is greater than the first due date
                actual += job[1]
                bad_jobs_first_due_date.append(job[1])
            else:
                new_jobs_first_due_date.append(job[1])  # this job is located before first due date
        for job in schedule[1]:  # schedule[1] - for the second set of jobs
            if job[0] < d[1]:  # if time of start of the job is smaller than the second due date
                actual += job[1]
                bad_jobs_second_due_date.append(job[1])
            else:
                new_jobs_second_due_date.append(job[1])  # this job is located after second due date

        # sort jobs than can be moved to move smallest jobs first
        bad_jobs_first_due_date = sorted(bad_jobs_first_due_date)
        bad_jobs_second_due_date = sorted(bad_jobs_second_due_date)

        # decide which jobs must be moved
        while actual > possible:
            # choosing the smallest job in two sets
            if (bad_jobs_first_due_date and bad_jobs_second_due_date and
                    bad_jobs_first_due_date[0] < bad_jobs_second_due_date[0]) or \
                    (bad_jobs_first_due_date and not bad_jobs_second_due_date):
                change = bad_jobs_first_due_date.pop(0)
                new_jobs_first_due_date.append(change)
                actual -= change
            else:
                change = bad_jobs_second_due_date.pop(0)
                new_jobs_second_due_date.append(change)
                actual -= change

        # sort jobs in respective order (from longer to shorter before due date and vice versa)
        new_jobs_first_due_date = [[0, job] for job in sorted(new_jobs_first_due_date, reverse=True)]
        bad_jobs_first_due_date = [[d[0], job] for job in sorted(bad_jobs_first_due_date)]

        bad_jobs_second_due_date = [[0, job] for job in sorted(bad_jobs_second_due_date, reverse=True)]
        new_jobs_second_due_date = [[d[1], job] for job in sorted(new_jobs_second_due_date)]

        # form new schedules
        duration = sum([job[1] for job in new_jobs_first_due_date])  # sum of all jobs that go before due date

        for job in new_jobs_first_due_date:
            job[0] = d[0] - duration
            duration -= job[1]

        # at this point duration must be equal to 0
        duration = d[0]

        for job in bad_jobs_first_due_date:
            job[0] = duration
            duration += job[1]

        duration = sum([job[1] for job in bad_jobs_second_due_date])  # sum of all jobs that go before due date

        for job in bad_jobs_second_due_date:
            job[0] = d[1] - duration
            duration -= job[1]

        # at this point duration must be equal to 0
        duration = d[1]

        for job in new_jobs_second_due_date:
            job[0] = duration
            duration += job[1]

        return [new_jobs_first_due_date + bad_jobs_first_due_date, bad_jobs_second_due_date + new_jobs_second_due_date]

    def divide(self, num_d, jobs, num_machines):

        assigned = []  # list of lists with jobs for each due date

        for i in range(num_d):
            due_date_jobs = jobs[i]  # jobs with this due date
            due_date_jobs = sorted(due_date_jobs, reverse=True)

            for j in range(num_machines, len(due_date_jobs), 2*num_machines):
                due_date_jobs[j:j+num_machines] = sorted(due_date_jobs[j:j+num_machines])  # sort some sections of jobs
                                                                                           # in reverse order (wave sort)

            # list of lists with jobs for each machine
            due_date_assigned = [
                [due_date_jobs[k] for k in range(j, len(due_date_jobs), num_machines)] for j in range(num_machines)
            ]

            assigned.append(due_date_assigned)

        return assigned

    # jobs = [[], []] : list - jobs for each due date. Second list is empty
    # d : int - is not a list!
    def one_due_date(self, jobs, d, num_machines, machines):
        machines = sorted(machines, reverse=True)
        assigned = self.divide(1, jobs, num_machines)[0]  # [0] - to take jobs for the first (and only) due date

        schedule = []

        for i in range(num_machines):
            if min(assigned[i]) > d:
                schedule.append(self.spt(assigned[i], machines[i]))
            else:
                schedule_single_machine = self.loose_due_date(assigned[i], d, machines[i])

                if schedule_single_machine[0][0] < 0:
                    schedule.append(self.tight_due_date(assigned[i], d, machines[i]))
                else:
                    schedule.append(schedule_single_machine)
        return schedule

    def two_due_dates(self, jobs, d, num_machines, machines):
        machines = sorted(machines, reverse=True)
        assigned = self.divide(2, jobs, num_machines)

        assigned_first_due_date = assigned[0]
        assigned_second_due_date = assigned[1]

        schedule = []

        for i in range(num_machines):
            # build ideal schedules
            schedule1 = self.loose_due_date(assigned_first_due_date[i], d[0], machines[i])
            schedule2 = self.loose_due_date(assigned_second_due_date[i], d[1], machines[i])

            # if due date not to close ot 0 point AND there is time between two schedules
            if schedule1[0][0] > 0 and schedule1[-1][0] + schedule1[-1][1] < schedule2[0][0]:
                # print('Situation 1')
                schedule.append([schedule1, schedule2])

            # if first due date is too close to the 0 point AND second one is far away from the first due date
            elif schedule1[0][0] < 0 and schedule1[-1][0] + schedule1[-1][1] < schedule2[0][0]:
                # print('Situation 2')
                schedule.append([self.tight_due_date(assigned_first_due_date[i], d[0], machines[i]), schedule2])

            # if first due date is far from 0 point but very close to the second due date
            elif schedule1[0][0] > 0 and schedule1[-1][0] + schedule1[-1][1] > schedule2[0][0]:
                # print('Situation 3')
                schedule.append(self.move_jobs_between_due_dates(d, [schedule1, schedule2]))

            # if both due date are close to 0 point and to each other
            else:
                # print('Situation 4')
                schedule1 = self.tight_due_date(assigned_first_due_date[i], d[0], machines[i])
                schedule2 = self.tight_due_date(assigned_second_due_date[i], d[1], machines[i],
                                                start=(schedule1[-1][0]+schedule1[-1][1]))  # new 0 point for second schedule
                schedule.append([schedule1, schedule2])

        return schedule

    def decide(self, num_d, d, jobs, num_machines, machines):
        # working with copies not to change original data
        jobs_copy = deepcopy(jobs)
        machines_copy = deepcopy(machines)

        if num_d == 1:
            schedule = self.one_due_date(jobs_copy, d[0], num_machines, machines_copy)
            for m in range(num_machines):
                schedule[m] = [schedule[m], []]
            return schedule
        elif num_d == 2:
            return self.two_due_dates(jobs_copy, d, num_machines, machines_copy)
        else:
            return None

    def tardiness(self, d, schedule):
        tard = 0
        for m in schedule:  # for each machine (returns list with two lists for each due date)
            for i in range(2):  # for each due date (returns indices for each due date)
                for job in m[i]:  # for each job on this machine m with this due date d[i] (returns tuples of jobs)
                    tard += abs(job[0] + job[1] - d[i])
        return tard

    def build_schedule(self, num_d, d, jobs, num_machines, machines):
        schedule = self.decide(num_d, d, jobs, num_machines, machines)
        return schedule


def main():
    num_d = 1
    jobs = [[5, 6, 7, 8, 9], []]
    d = [4]
    num_machines = 2
    machines = [1, 2]

    schedule = Schedule().build_schedule(num_d, d, jobs, num_machines, machines)
    print(schedule)
    exit(0)
    for m in range(len(schedule)):
        print(f'machine {m+1}', end='\t')
        print(schedule[m][0], end='\t')
        if schedule[m][1]:
            print(schedule[m][1], end='\t')
        print()

    print(f'\nTardiness = {Schedule().tardiness(d, schedule)}')


if __name__ == '__main__':
    main()
