s = "I love to write python"

#split string s into list of words
split_s = s.split()
print(split_s)

for word in split_s:
    if word.lower().find("i") > -1:
        print("I found I in " + word)

    else:
        print("No i's were found :(")
