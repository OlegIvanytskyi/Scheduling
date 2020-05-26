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

    # at this point duration must be equal to 0
    duration = d

    for job in schedule_after_due_date:
        job[0] = duration
        duration += job[1]

    return schedule_before_due_date + schedule_after_due_date


# function for moving jobs that cannot be executed between due dates
# situation with first loose and second tight due dates (single machine)
def move_jobs_between_due_dates(d, schedule):
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
        if bad_jobs_first_due_date and bad_jobs_first_due_date[0] < bad_jobs_second_due_date[0]:
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

    return new_jobs_first_due_date + bad_jobs_first_due_date + bad_jobs_second_due_date + new_jobs_second_due_date


def divide(num_d, jobs, num_machines):

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


def one_due_date(num_jobs, jobs, d, num_machines, machines):
    machines = sorted(machines, reverse=True)
    assigned = divide(1, jobs, num_machines)
    # todo continue with multiple machines

    if min(jobs) > d:
        return spt(jobs)

    schedule = loose_due_date(jobs, d)

    if schedule[0][1] < 0:
        return tight_due_date(jobs, d)
    return schedule


def two_due_dates(num_jobs, jobs, d, num_machines, machines):
    return 0


def decide(num_d, num_jobs, jobs, d, num_machines, machines):
    # working with copies not to change original data
    jobs_copy = deepcopy(jobs)
    machines_copy = deepcopy(machines)

    if num_d == 1:
        return one_due_date(num_jobs[0], jobs_copy, d[0], num_machines, machines_copy)
    elif num_d == 2:
        return two_due_dates(num_jobs, jobs_copy, d, num_machines, machines_copy)
    else:
        return None


def main():
    assigned = move_jobs_between_due_dates([20, 30], [[[10, 5], [15, 3], [18, 2], [20, 3], [23, 4]],
                                                      [[18, 7], [25, 4], [29, 1], [30, 3], [33, 6]]])


if __name__ == '__main__':
    main()
