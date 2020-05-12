from copy import deepcopy


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
    machines = sorted(machines)
    jobs = sorted(jobs, reverse=True)

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


def loose_due_date(num_jobs, jobs, num_machines, machines):
    return 0


def tight_due_date(num_jobs, jobs, num_machines, machines):
    return 0


def impossible(schedule):
    return True


def main():
    pass


if __name__ == '__main__':
    main()
