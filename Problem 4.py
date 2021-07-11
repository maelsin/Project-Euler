def IsPalindrome(num):
    numString = str(num)
    if numString == numString[::-1]:
        return True
    else:
        return False


palindromeList = [ i * j for i in range(100, 1000) for j in range(100, 1000) if IsPalindrome(i * j) == True ]

print(max(palindromeList))
