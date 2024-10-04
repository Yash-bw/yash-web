# program - Implement a  queue using a list where elements are enqueued from the rear and dequeued from the front.
# challenge : handle the case when trying to deqeue from the empty eqeue.

from collections import deque
def queue_enqueue_dequeue():
    l1 =  [ 1,2,3,4,5,6]
    #l2 = []
    d = deque(l1)
    l3 =  d.appendleft(0)
    print(d)
    l4 = d.pop()
    while d :
        try:
            print("this is new list")
            break
        except:
            print("No item in this list ")
    else:
        print("Updated list ")
    print(d)
    
queue_enqueue_dequeue()
