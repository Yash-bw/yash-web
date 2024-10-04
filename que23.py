# program : Genrate a list of tuples representing all possible combinations of two lists .
# input : list1: [1,2], list2 = [3,4]
# output : [(1,3),(1,4),(2,3)(2,4)]

from itertools import product
def list_combinations():
    list1 = [1,2]
    list2 = [3,4]
    combo = list(product(list1,list2))
    print(combo)
list_combinations()