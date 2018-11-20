from math import sqrt

#set variables for known lengths of two sides of triangle
b = 3
c = 4

#calculate length of hypotenuse
a = sqrt(b**2 + c**2)

#print human readable output of pythagorean theorem with above numbers
print(str(a) + " squared equals " + str(b) + " squared plus " + str(c) + "  squared.")
