#Write a program to invert a dictionary, i.e., keys become values and values become keys.
# input : {'a':1,'b':2}
def invert_dict():
    input = {'a':1,'b':2}
    new = dict(zip(input.values(), input.keys())) 
    print(new)
invert_dict()
