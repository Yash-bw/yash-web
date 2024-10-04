# program : emplement a program that asks the user to input a year and determines if it is leap year.
#  input : 2024 
#  output : True

def leap_year():
    year = int(input("Enter a year : "))
    condition = True
    #while condition :
    if year % 4 == 0:
        print(" True " )
    else :
        print(" False ")        
leap_year()