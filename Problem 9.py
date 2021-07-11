
m = 2 

a = 0
b = 0
c = 0

while a + b + c != 1000:
    for n in range(1,m):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2

        if a + b + c == 1000:
            break
    m += 1

print(a*b*c)