# program - Write a program to find a longest common subsequence between two tuples. 
# input : (1,2,3,4) and (2,3,5)

def common_subsequence():
    input1 = (1,2,3,4)
    input2 = (2,3,5)
    common = []
    for element in input1:
        if element in input2:
            common.append(element)
    print(tuple(common))

common_subsequence()


