def remove_c(s, c, n, i):
    
    if i == n:
        return ""
    
    ans = remove_c(s, c, n, i+1)
    if s[i] == c:
        return ans + ""
    else:
        return s[i] + ans

class Solution:
    # Function to remove all occurrences of the character from the string
    def removeCharacter(self, s, c):
        # code here
        i = 0
        n = len(s)
        return remove_c(s, c, n, i) 