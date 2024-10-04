# program : Given a tuple of numbers, write a program to count how many times each numbers appears in the tuple.
# input : (1,2,2,3,1)

def appears():
    input1 = (1,2,2,3,1)
    dict = {}

    for element in (input1):
        if element in dict:
            dict[element] +=  1
        else:
            dict[element] = 1
    print(dict)
appears()







