def fun(arr, i, n):
    if  i == n or i == n-1:
        return True
        
    if arr[i] > arr[i+1]:
        return False
    
    return fun(arr, i+1, n)
    

class Solution:
    def isSorted(self, arr) -> bool:
        
        i = 0
        n = len(arr)
        
        return fun(arr, i, n)