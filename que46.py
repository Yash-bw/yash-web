# program : Write a program that uses elif to determine the grade based on a student score 
#  input : 85
# output : "b"

def grade():
    score = int(input("Enter a number : "))
    number = 100
    if number >= score :
        print("gread : b")
    elif number <= score :
        print("gread : a")
    else:
        print("gread d")
grade()