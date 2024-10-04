# program : create a list of squares for all even numbers between 1 and 20 using list comprehension.
# * output : [ 4, 8, 36, 64, 81, 100, 144, 196, 256, 324, 400]

'''def squares_even_number():
    number = int(input("Enter a number"))
    list = []
    for i in range (number+1):
        if i%2 == 0 :
            #number += list
            list.append(i**2)
        if list :
            print(list)
        else :
            print("there are not a even number")
squares_even_number()'''

def squares_even_number():
    number = int(input("Enter anumber"))
    squares = [i**2 for i in range (number+1)]
    print(squares)
squares_even_number()