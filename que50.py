# program : find the diffrence between two sets and display elements from a list using sets 
# sec : {1,2,3} and {2,3,4}

def two_diffrece():
    l1 = {1,2,3}
    l2 = {2,3,4}
    diffrece = l1 - l2
    print(diffrece)
two_diffrece()