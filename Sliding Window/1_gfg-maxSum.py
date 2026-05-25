class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        # code here 
        lo=0
        hi=k-1
        
        ssum = 0
        for i in range(lo, hi+1):  # hi+1
            ssum += arr[i]
        
        res = ssum    # res = ssum --> ko initialize kro
        while hi < n : # 
            res = max(res, ssum)
            lo += 1
            hi += 1
            
            if hi == n: # if dont what this condition then -> while hi < n-1 : ]]>shoue be the condition
                break
            ssum = ssum - arr[lo-1]
            ssum = ssum + arr[hi]
        
        return res