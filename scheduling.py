from copy import deepcopy


# start - zero point (moment of time which indicates the earliest possible beginning of schedule)
def spt(jobs, start=0):
    jobs = sorted(jobs)

    schedule = []

    for job in jobs:
        schedule.append([start, job])
        start += job

    return schedule


def tight_due_date(jobs, d, start=0):
    jobs = sorted(jobs, reverse=True)

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


def loose_due_date(jobs, d):
    jobs = sorted(jobs, reverse=True)

    schedule_before_due_date = [[0, job] for job in jobs[::2]]
    schedule_after_due_date = [[0, job] for job in jobs[1::2]][::-1]  # [::-1] is used to reverse the list

    duration = sum([job[1] for job in schedule_before_due_date])  # sum of all jobs that go before due date

    for job in schedule_before_due_date:
        job[0] = d - duration
        duration -= job[1]

    # at this point duration must be equal to d

    for job in schedule_after_due_date:
        job[0] = duration
        duration += job[1]

    return schedule_before_due_date + schedule_after_due_date


def divide(num_d, num_jobs, jobs, d, num_machines, machines):
    machines = sorted(machines, reverse=True)

    assigned = []  # list of lists with jobs for each due date

    for i in range(num_d):
        due_date_jobs = jobs[i]  # jobs with this due date
        due_date_jobs = sorted(due_date_jobs, reverse=True)

        for j in range(num_machines, len(due_date_jobs), 2*num_machines):
            due_date_jobs[j:j+num_machines] = sorted(due_date_jobs[j:j+num_machines])

        # list of lists with jobs for each machine
        due_date_assigned = [
            [due_date_jobs[k] for k in range(j, len(due_date_jobs), num_machines)] for j in range(num_machines)
        ]

        assigned.append(due_date_assigned)

    return assigned


def decide(num_d, num_jobs, jobs, d, num_machines, machines):
    # working with copies not to change original data
    num_jobs_copy = deepcopy(num_jobs)
    jobs_copy = deepcopy(jobs)
    d_copy = deepcopy(d)
    num_machines_copy = num_machines
    machines_copy = deepcopy(machines)

    if num_d == 1:
        return one_due_date(num_jobs_copy, jobs_copy, d_copy, num_machines_copy, machines_copy)
    elif num_d == 2:
        return two_due_dates(num_jobs_copy, jobs_copy, d_copy, num_machines_copy, machines_copy)
    else:
        # TODO unsupported number of due dates
        return None


def one_due_date(num_jobs, jobs, d, num_machines, machines):
    jobs = jobs[0]
    d = d[0]
    if min(jobs) > d:
        return SPT(num_jobs, jobs, num_machines, machines)
    else:
        schedule = loose_due_date(num_jobs, jobs, num_machines, machines)

        if impossible(schedule):
            return tight_due_date(num_jobs, jobs, num_machines, machines)
        return schedule


def two_due_dates(num_jobs, jobs, d, num_machines, machines):
    return 0


def SPT(num_jobs, jobs, num_machines, machines):
    machines = sorted(machines, reverse=True)
    jobs = sorted(jobs)

    schedule = [[] for _ in range(num_machines)]

    machine = 0
    times = [0 for _ in range(num_machines)]  # time available for next job
    for job in jobs:
        schedule[machine].append((times[machine], job))
        times[machine] += job
        machine += 1
        if machine == num_machines:
            machine = 0
    return schedule


def impossible(schedule):
    return True


def main():
    assigned = divide(1, 13, [[10, 10, 9, 8, 8, 6, 5, 7, 4, 3, 2, 2, 1, 1]], 10, 3, [1, 1, 1])
    for d in assigned:
        for m in d:
            for j in m:
                print(j, end=' ')
            print()


if __name__ == '__main__':
    main()
