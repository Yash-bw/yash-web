# write a program that loops through a list and appends only even numbers to anew list.
# input = [1,2,3,4]
# output = [2,4]
def even():
    li1 = [1,2,3,4]
    li = []
    for i in (li1):
        if i%2 == 0:
            li.append(i)
    print(li)
even()

 