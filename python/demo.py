s = []

for x in range(10):
    res = x**2
    if res % 2 == 0:
        s.append(res)
print(s)


#alternatively
S = [x**2 for x in range(10)
     if x**2 % 2 == 0]

print(S)
