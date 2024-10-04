# program : write a program to check if number is positive, nagetive, or zero. 
# input : 5
# output : positive

def check_number():
    num = int(input("Enter a number"))
    if num >= 0 :
        print("Number is positive")
    elif num == 0:
        print("Number is zero")
    else:
        print("Number is nagetive")

check_number()