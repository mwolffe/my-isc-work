something = "Completely Different"
something_split = something.split()
total_t = 0

for word in something_split:
    if word.lower().find('t') > -1:
        total_t +=1

print(total_t)
    
