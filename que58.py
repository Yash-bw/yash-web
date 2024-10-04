# program : create a task scheduler simulation using a queue, Enqueue task (string) and dequeue them one at a time, processing the tasks.prints

def process_task():
    task = ['task1', 'task2', 'task3']
    task.insert(0, 'new task')
    task.pop(3)
    '''for i in range(len(task)):
        count = 0
        task.insert(count,'new ')
        task.pop()'''

    print(task)
process_task()