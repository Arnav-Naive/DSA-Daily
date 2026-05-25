class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = 0
        sum_  = 0
        
        res = float('inf')
        while high < n :
            sum_  = sum_ + nums[high]

            if sum_ >= target:   # only fier them when sum>=target
                while sum_ >= target :
                    lenght = high-low+1
                    res = min(res, lenght)
                    sum_ = sum_ - nums[low]
                    low += 1
                    
            high += 1

        if res == float('inf') :
            return 0
        
        return res