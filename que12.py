# program : write a program that simulates a circular queue with a fixed size which wraps around when the queue become full.
# challenge : implement logic to overwrite the oldest element when the queue is .

from collections import deque
def fixed_queue():
    l1 = []
    d = deque(l1)
    count = 10
    for i in range (count):
        d.appendleft('task')
        print(d)
fixed_queue()

'''from collections import deque

def fixed_queue():
    max_size = 5  # Set the maximum size of the circular queue
    d = deque(maxlen=max_size)  # Initialize the deque with a max size
    count = 10  # Total number of elements to be added to the queue
    
    for i in range(count):
        d.append(i+1)  # Add the tasks sequentially to the queue
        print(f'Queue after adding task{i+1}: {list(d)}')

    print(f'Final queue: {list(d)}')  # Final state of the circular queue

fixed_queue()'''
