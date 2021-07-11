def SquareDifference(n):
    sumOfSquare = sum([i ** 2 for i in range(1, n+1)])
    squareOfSum = sum(range(1, n+1)) ** 2

    return squareOfSum - sumOfSquare

print(SquareDifference(100))