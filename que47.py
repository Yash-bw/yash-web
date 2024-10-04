#program : Write a program that checks if a string starts with vowels using if and elif conditions.
# input : "apple"
# output : "strats with a vowel"

def check_string():
    str = "apple"
    vowel = "AEIOUaeiou"
    if str and str[0] in vowel:
        print("starts with a vowel")
    elif str :
        print("starts with not vowel")
    else :
        print("there is empty string")
check_string()