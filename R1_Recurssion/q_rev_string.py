def fun(s, low, hi):
    # s_len = hi-low +1
    
    # if s_len == 0 or s_len == 1:
    #     return True
    if low >= hi :
        return True
    
    if s[low] != s[hi]:
        return False
    
    return fun(s, low+1, hi-1)


class Solution:
    def isPalindrome(self, s):
        # code here
        low = 0
        hi = len(s)-1
        return fun(s, low, hi)
