#program : Write a program that counts the occurrences of each word in a sentence using a dictionary.
# input : "Hello world hello"
from collections import Counter
import re
def count_occurrences():
    str = "Hello world hello"
    new_str = str.lower()
    li = re.split(r'\W+',new_str)
    cnt = Counter()
    for i in (li):
        cnt[i] += 1
    print(cnt)
count_occurrences()


