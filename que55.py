# Program : anagram string 

def anagram_string():
    str = "silent"
    str1 = "listen"
    if sorted(str) == sorted(str1) :
        print("string is anagram")
    else :
        print("string is not anagram")
anagram_string()