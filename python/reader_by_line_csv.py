with open('weather.csv', 'r') as reader:
    line = reader.readline()
    count = 0

    while line != '':
        count += 1
        print(line)
        line = reader.readline()

    print("It's over")
