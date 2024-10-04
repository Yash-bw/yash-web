# program : flatten a 2d matrix (list of lits) into a single list using list comprehension.
# input : [[1,2],[3,4],[5,6]]
# output : [1,2,3,4,5,6]

def marge_list():
    list1 = [[1,2],[3,4],[5,6]]
    #num = []
    marge = [num for i in  list1 for num in i]
    print(marge)
marge_list()