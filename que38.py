#Program : write a program that uses a for loop to iterate over a list and create a new list where each element is doubled.
# input : [1,2,3]
# output : [2,4,6]

def iterate_value():
    li = [1,2,3]
    new_list = [x*2 for x in (li)]
    print(new_list)
iterate_value()