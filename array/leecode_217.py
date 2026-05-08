# simple but not helpful for future

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = len(nums)
        y = len(list(set(nums)))
        if x == y:
            return False
        return True

# Best way :

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)       # no duplicate yet, add to seen
        return False