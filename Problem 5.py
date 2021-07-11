def gcd(a, b):
    if b == 0: 
        return a
    else: 
        return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

def MultipleLCM(numbers):
    ans = numbers[0]

    for i in numbers: 
        ans = lcm(ans, i)
    
    return ans

print(MultipleLCM(range(1,21)))
