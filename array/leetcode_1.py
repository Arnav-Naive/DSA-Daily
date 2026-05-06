# Problem: Two Sum
# LC: #1
# Approach 1: Brute Force
# TC: O(n²) | SC: O(1)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]+nums[j] == target):
                    return [i, j]


# Approach 2: HashMap
# TC: O(n) | SC: O(n)
# Pattern: For each num, check if complement exists in seen dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # stores {value: index}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:          # already visited before? O(1) lookup
                return [i, seen[need]]
            seen[nums[i]] = i               # store current number with its index