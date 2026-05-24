# thsi is a very easy looking que , coud be done using 'swap' function 

class Solution:

    def suwap(self, nums, i, j):
        # same index swap not needed
        if i == j:
            return
        nums[i] = nums[i] + nums[j]
        nums[j] = nums[i] - nums[j]
        nums[i] = nums[i] - nums[j]

    def sortColors(self, nums: List[int]) -> None:

        lo = 0
        mid = 0
        hi = len(nums) - 1

        while mid <= hi:
            if nums[mid] == 0:
                self.suwap(nums, mid, lo)
                mid += 1
                lo += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                self.suwap(nums, mid, hi)
                hi -= 1