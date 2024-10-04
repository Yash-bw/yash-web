# program : Write a program that checks if a given a number is divisible both 3 and 5 .
# input : 15
# output : True

def divisible():
    num = int(input("Enter a number"))
    condition = True
    while condition :
        if num % 3 == 0 and num % 5 == 0:
            print(True)
            break
        else :
            print(False)
divisible()