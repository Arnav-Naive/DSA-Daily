class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1] :
                continue

            j=1+i
            k=len(nums)-1
            while j < k :
                curr_sum = nums[i]+nums[j]+nums[k] 
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                if curr_sum == target:
                    return curr_sum
                elif curr_sum>target:
                    k=k-1
                else:
                    j=j+1
        return closest