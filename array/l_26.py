class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # s = set(nums)
        x = 0
        for i in range(len(nums)):
            if nums[i] != nums[x]:
                x = x+1
                nums[x] = nums[i]
        # return len(s)
        return x+1

# return the number of unique elements
# and also nums should be modified in place such that first k elements are unique elements
# it dont care about the remaining elements