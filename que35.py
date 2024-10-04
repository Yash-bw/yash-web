# Write a function that takes  two dictionaries and merges them into one.
# input : {'a':1} and {'b':2}
# output : {'a':1, 'b':2}

def dict_merges():
    di1 = {'a':1}
    di2 = {'b':2}
    merges = di1|di2 
    print(merges)
dict_merges() 