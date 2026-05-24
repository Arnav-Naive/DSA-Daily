class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return len(nums)

        k = 2

        for i in range(2, len(nums)):

            # if already 2 same numbers exist
            if nums[i] == nums[k - 2]:
                continue

            # keep current number
            nums[k] = nums[i]
            k += 1

        return k