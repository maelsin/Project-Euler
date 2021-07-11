def isPrime(n):

    PrimeFlag = True

    for i in range(2,n):
        if n % i == 0:
            PrimeFlag = False
            break
    return PrimeFlag

primeList = []
i = 2

while len(primeList) < 10001:
    if isPrime(i) == True:
        primeList.append(i)
    i += 1

print(primeList[-1])