# program - create a stack to reverse a given string (without using the reversed() function ). push each string charator into the stack and then pop them to from thr revarsed string.


def reverse_string():
    input_str = str(input("string : "))
    #input_str = ("abcdefghijklmnopqrstuvwxyz")
    #reverse_str = input_str[::-1]
    #print(reverse_str)
    str_list = list(input_str)
    reversed_str = (" ")
    while str_list:
        reversed_str += str_list.pop()
    print (reversed_str)
reverse_string()
        
    