# program - create a task scheduler simulates circular queue. enqueue task (string) and dequeue them one at time, processing the task.
# input : list of task like [ 'task1', 'task2', 'task3']
# output : processed tasks in order

from collections import deque
def circular_queue():
    l1 =['task1', 'task2', 'task3', 'task4']
    d  = deque(l1)
    for i in range (len(l1)):
        d.appendleft('task')
        d.pop()
        print(d)
circular_queue()