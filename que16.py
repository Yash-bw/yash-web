# program : write a program to filter out vowels from a given string using list comprehension.
# * input : "hellow world"
# * output : "hll wrld"
def filter_vowels():
    stri = str(input("input : "))
    vowels = ('a','e','i','o','u','A','E','I','o','U')
    filter = ''.join([char for char in stri if char not in vowels ])
    print(filter)
filter_vowels()
