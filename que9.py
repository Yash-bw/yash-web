# program - Design a stack-based solustion to check if a given word is a palindrome 
#   * input - "madam"
#   * output - "True/False"

def palindrome():
    input_string = str(input("input : "))
    #palindrome_string = ''.join(reversed(input_string))
    palindrom_string =  input_string[::-1]
    if input_string == palindrom_string:
        print("True")
    else:
        print("False")
palindrome()