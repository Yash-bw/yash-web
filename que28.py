# program : Write a function that accepts  a list of tuples and sorts them by the second element in each tuple.
# * input : [ (1,2),(3,1),(5,3)]

def List_tuple():
    l1 = [(1,2),(3,1),(5,3)]
    #tuple = sorted(l1,key=last)
    l2 =sorted(l1, key=lambda  l : l[1])
    print(l2)
List_tuple()

