# write a program that uses a nested loop to print a right-angled triangle pattern of stars.
# input : 4(height)


def triangle():
    for i in range(0,5):
        for j in range(0,i+1):
            print("*",end="")
        #print()
     
triangle()

