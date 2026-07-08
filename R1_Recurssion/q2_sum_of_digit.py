def fun(n):
    if n == 0:
        return 0
    
    d = n % 10
    n = n // 10
    ans = fun(n)
    
    return d + ans

class Solution:
    def sumOfDigits(self, n):
        
        return fun(n)