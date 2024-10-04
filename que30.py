# Write a function that zips two tuple into a list of tuple.
#input1 :  (1,2,3)
#input2 : (4,5,6)


def zip_function():
    input1 = (1,2,3)
    input2 = (4,5,6)
    new = zip(input1, input2)
    print(tuple(new))
zip_function()