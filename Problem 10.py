import math
def nPrimes(n):
    intArray = [i for i in range(2,n+1)]
    p = 2

    while p <= math.sqrt(n):
        if p in intArray:
            pMultiples = [p**2 + j*p for j in range(n // p)]
            intArray = list(set(intArray) - set(pMultiples))
        p += 1
    return intArray

print(sum(nPrimes(2000000)))
    


