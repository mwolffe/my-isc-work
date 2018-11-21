with open('temp.txt', 'w') as writer:
    writer.write('elements\n') #\n adds a newline between strings
    writer.writelines(('He\n', 'Ne\n', 'Ar\n'))

