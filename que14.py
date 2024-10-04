# program : Write  a function to reverse the order of elements in a queue using a stack.
# * input : Queue with elements [1,2,3,4,5]
# * output : Reversed queue [5,4,3,2,1]

def reverse_order():
    l1 = [1,2,3,4,5,6]
    #new = l1[::-1]
    #print(new)
    new = list(reversed(l1))
    print(new) 
reverse_order()