with open('hello.txt', 'r') as reader:
    data = reader.read(5)
    while data != '': #do this as long as data is present
        print(len(data))#
        data = reader.read(5) #reassign in the while loop. This chunks data in blocks of 5 bytes
print(len(data))
