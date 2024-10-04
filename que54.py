# program : write a function to cpmpare two tuple element-wise and tuple of booleans indicting the compraison result.
# input : (1,2,3) and  (1,3,2)
# output : (True, False, True)

def compair_two_tuple():
    t = (1,2,3)
    t1 = (1,3,2)
    compare = tuple(t==t1 for t, t1 in zip(t,t1))
    print(compare)
compair_two_tuple()

    
