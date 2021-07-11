def fibb(n): 
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
         return fibb(n-1) + fibb(n-2)

i = 0 
count = 0
while fibb(i) <= 4000000:
    if fibb(i) % 2 == 0:
        count += fibb(i)
    i += 1

print(count)
