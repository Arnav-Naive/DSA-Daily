class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        officer = 0
        cm = 1
        res = 1
        n = len(nums)

        while cm < n :
            if nums[cm] == nums[cm-1] :
                cm += 1
                continue
            else :
                nums[officer+1] = nums[cm]
                officer += 1
                cm += 1
                res += 1
        return res