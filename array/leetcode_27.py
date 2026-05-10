class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count



# just count the  number of elements which are not equal to val
# -----------------
# but LeetCode checks two things:
# Your return value k (count)
# That nums[:k] actually contains the valid elements
# So if you just return count without modifying nums, some test cases will fail.
# Try removing nums[count] = nums[i] and submitting — you'll see it fail.