#Write a python function calculate area that takes a radius of circal and its return its area. include documentaion string that explan what the function dose.
import math
'''radius = int(input("Enter a number :"))
Area = math.pi*radius**2
print (Area)'''
def calculate_area(radius):
    area = math.pi*radius**2
    return area
radius = int(input("Enter a number"))
print(calculate_area(radius))

