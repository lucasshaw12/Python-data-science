#! python3

# Python tuples data structure exercises.

task_list = ['pay bills', 'tidy up', 'walk the dog', 'go to pharmacy', 'cook dinner']
task_tm = ['8:00', '8:30', '9:00', '10:00', '10:30']

sched_list = [(tm, task) for tm, task in zip(task_tm, task_list)]
print(sched_list)
print(sched_list[1][0])
print(sched_list[1][1])
















































