# program : Write a program to find the key with the highest value in the dictionary.
# input : {'a':1,'b':5,'c':3}

def highest_value():
    input = {'a':1,'b':5,'c':3}
    maxkey = max(zip(input.values(),input.keys()))[1]
    print(maxkey)
highest_value()