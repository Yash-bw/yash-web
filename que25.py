# program - Write a program that deletes an element from a list at a specified using the del statement.
# input - [1,2,3,4] and index 2
# output - [1,2,4]

def delete_item():
    list1 = [1,2,3,4]
    del list1[2]
    print(list1)
delete_item()