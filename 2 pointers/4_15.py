class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        x=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1] :
                continue
            j=1+i
            k=len(nums)-1
            while j < k :
                sum = nums[i]+nums[j]+nums[k]  # 'sum'--> sum() is already a Python built-in function.
                if sum > 0 :
                    k = k-1
                elif sum < 0 :
                    j = j+1
                else :
                    x.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                    while j<k and nums[j] == nums[j-1]:
                        j=j+1
                    while j<k and nums[k] == nums[k+1]:
                        k=k-1
        return x