# program : using a while loop to reverse a list.
# input : [1,2,3,4]

def reverse_loop():
    l1 = [1,2,3,4]
    reversed_list = []
    #l2 = l1[::-1]
    #print(l2)
    i = len(l1)-1
    while i >= 0 :
        reversed_list.append(l1[i])
        i = i-1
    print(reversed_list)
reverse_loop()



    
