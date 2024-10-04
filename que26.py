# Write a function to remove a slice of alist using the statement.
# * input - [1,2,3,4,5] and slice(1:3)
# output  - [1,4,5]

def slice_item():
    input = [1,2,3,4,5]
    del input[1:3]
    print(input)
slice_item()