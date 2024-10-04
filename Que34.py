# program : create a dictionary that maps numbers to their squares using a dictnary comprehension.
# input : range(1,6)
# output : {1:1, 2:4, 3:9, 4:16, 5:25}


def dict_comprehension():
    dictnary = { x : x**2 for x in range(1,6)}
    print(dictnary)
dict_comprehension()