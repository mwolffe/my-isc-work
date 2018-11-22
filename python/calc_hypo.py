from math import sqrt


def calc_hypo(a,b):
    if type(a) not in (int,float) or type(b) not in (int, float):
        print("Type a number!")
        return(False)
    
    elif a <= 0 or b <= 0:
        print("Length of side cannot be less than or equal to 0")

    else:
        hypo = sqrt(a**2 + b**2)
        return hypo

a = float(input("What is the length of the adjacent? "))
b = float(input("What is the length of the opposite? "))

print("The hypotenuse is " + str(calc_hypo(a,b)))
