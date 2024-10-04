# program : write a list comprehension to find common elements two lists.
# * input : list1 = [1,2,3,4], lists2 = [3,4,5,6]
# * output : [3,4]

def common_list():
    list1 = [1,2,3,4]
    list2 = [3,4,5,6]
    common = [x for x in list1 if x in list2]
    print(common)
common_list()
