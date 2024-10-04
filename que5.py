# question- Implement stack using a list, and write function to push element to the stack,pop the top elements and disply the current element.
#challenge : Emplement error handling when tring to pop from an empty stack.
def current_stack():
    lists = [1,2,3,4,5,6]
    #lists = []
    empty_list = []
    #list.append(7)
    #print(list)
    list1 = lists.pop()
    while list1 :
        try:
            print("this is New_list")
            break
        except:
            print("No item in this list")
    else:
        print("No empty item found in list")
    print(list1)
current_stack()





