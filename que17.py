# program : generate a list of all the divisors of a number using list comprehension.
# input - 12
# output - [1,2,3,4,6,12]

def divisors():
    number = int(input("Enter a number: "))
    divi = [i for i in range(1,number+1) if number % i == 0]
    print(divi)
divisors()
