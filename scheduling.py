def decide(num_d, num_jobs, jobs, d, num_machines, machines):
    if num_d == 1:
        return one_due_date(num_d, num_jobs, jobs, d, num_machines, machines)
    elif num_d == 2:
        return two_due_dates(num_d, num_jobs, jobs, d, num_machines, machines)
    else:
        # TODO unsupported number of due dates
        return None


def one_due_date(num_d, num_jobs, jobs, d, num_machines, machines):
    jobs = jobs[0]
    if min(jobs) > d:
        return SPT(num_jobs, jobs, num_machines, machines)
    else:
        schedule = loose_due_date(num_jobs, jobs, num_machines, machines)

        if impossible(schedule):
            return tight_due_date(num_jobs, jobs, num_machines, machines)
        return schedule


def two_due_dates(num_d, num_jobs, jobs, d, num_machines, machines):
    return 0


def SPT(num_jobs, jobs, num_machines, machines):
    pass


def loose_due_date(num_jobs, jobs, num_machines, machines):
    pass


def tight_due_date(num_jobs, jobs, num_machines, machines):
    pass


def impossible(schedule):
    return True