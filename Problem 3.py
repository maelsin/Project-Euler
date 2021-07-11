
def isPrime(n):

    PrimeFlag = True

    for i in range(2,n):
        if n % i == 0:
            PrimeFlag = False
            break
    return PrimeFlag


def largestPrimeFactor(n):
    for j in range(2, n):
        if isPrime(n):
            return n
            break
        if n % j == 0 and isPrime(j) == True:
            n = n // j



print(largestPrimeFactor(600851475143))

    

   