# Job Scheduling Problem using Greedy Method

def job_scheduling(jobs):

    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [-1] * max_deadline

    total_profit = 0

    # Schedule jobs
    for job in jobs:

        job_id = job[0]
        deadline = job[1]
        profit = job[2]

        for i in range(deadline - 1, -1, -1):

            if slots[i] == -1:

                slots[i] = job_id
                total_profit += profit
                break

    # Display Result
    print("\nScheduled Jobs:")

    for job in slots:

        if job != -1:
            print(job, end=" ")

    print("\nTotal Profit:", total_profit)


# Main Program
n = int(input("Enter number of jobs: "))

jobs = []

print("Enter Job ID, Deadline and Profit:")

for i in range(n):

    job_id = input("Job ID: ")

    deadline = int(input("Deadline: "))

    profit = int(input("Profit: "))

    jobs.append((job_id, deadline, profit))

job_scheduling(jobs)


#INPUT

#Enter number of jobs: 4
#Enter Job ID, Deadline and Profit:
#Job ID: J1
#Deadline: 2
#Profit: 100
#Job ID: J2
#Deadline: 1
#Profit: 19
#Job ID: J3
#Deadline: 2
#Profit: 27
#Job ID: J4
#Deadline: 1
#Profit: 25
