mylist = [23, "hi", 2.4e10]
for (count, item) in enumerate(mylist):
    print(count, item)


(first, middle, last) = mylist

print(mylist)

(first, middle, last) = (middle, last, first)

print(first, middle, last)
