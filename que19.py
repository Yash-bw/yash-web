# program Using list comprehension, convert list of string to upper case, but only for strings that have more then 3 characters.
# input : ['apple', 'cat', 'dog', 'elephant']
# output : ['apple', 'elephant']

def  list_string():
    list1 = ['apple', 'cat', 'dog', 'elephany']
    new = [i.upper() for i in list1 if len(i) > 3]
    print(new)
list_string()