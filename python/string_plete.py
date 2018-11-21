something = "Completely Different"
something_split = something.split()
total = 0

while total < 1:
    for word in something_split:
        if word.lower().find('plete') > -1:
            print("I found plete in " + word)
            total += 1


    
