with open('weather.csv', 'r') as reader:
    header = reader.readline()
    count = 0
    rain = []

#readlines reads as lines, not as letters in a string
    for line in reader.readlines():
        x = line.strip().split(",")[-1] #removes \n from end of line
        x = float(x)
        rain.append(x)
        
        
    print(rain)
 
with open('myrain.txt', 'w') as writer:
    writer.write(str(rain) + "\n")
