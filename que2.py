# define a lambda function square that takes a number and return its square then use it to print the suuare of 7. 
'''num = int(input("Enter a number :" ))
#square = num ** 2
#print (num ** 2)
square = (lambda x : x ** 2)(num)
print (square)'''


def square(number):
    square_num = lambda x : x **2
    return square_num(number)
number = int(input("Enter a number :"))
print(square(number))
'''return lambda x : x **2 
num = int(input("Enter a number :"))
number = square()(num)
print(square)'''




















































































































  














