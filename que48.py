# program : write a program that finds the union and intersection of twp sets.
# input : {1,2,3} and {2,3,4}
# output : union : {1,2,3,4} Intersection {2,3}

def union_intersection():
    l1 = {1,2,3}
    l2 = {2,3,4}
    unoin =  l1|l2
    intersection = l1&l2
    print(unoin)
    print(intersection)
union_intersection()
