# write a program that iterates over a dictionary and prints each key:value pair
# input : {'a':1, 'b':2}
# output : 'a: 1','b: 2'
def convert():
    input = {'a':1, 'b':2}
    output = []
    for key, value in input.items():
        output.append(f"'{key}:{value}'")
        result = ", ".join(output)
        print(result)
convert()
 
