# Write a program to generate a multiplication table using nested list comprehension.
# output : A 10*10 matrix where element (i,j) is i*j

def multiplication_nestedlist():
    multi = [[i*j for j in range (1,11)] for i in range(1,11)]
    print(multi)
multiplication_nestedlist()

