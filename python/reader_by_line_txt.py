#Finds the average length of a line in a text file 

with open('hello.txt', 'r') as reader:
    line = reader.readline() #Gives line the value of a single line from file
    total = 0
    count = 0

    while line != '':
        count += 1
        total += len(line)
        line = reader.readline()

print ('The average line length is', int(float(total) / float(count)))
