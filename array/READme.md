Strings
# Strings are immutable — you can't do s[0] = "x"
# In DSA, convert to list, modify, join back
s = list("hello")
s[0] = "H"
"".join(s)         # "Hello"
---
Dictionaries 
# Most common DSA pattern — frequency counter
nums = [1, 2, 2, 3, 3, 3]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
# freq = {1:1, 2:2, 3:3}
---
Sets
# DSA use — remove duplicates instantly
nums = [1, 2, 2, 3, 3]
list(set(nums))    # [1, 2, 3]
---
Loops
# enumerate — use this instead of range(len(a))
nums = [10, 20, 30]
for i, val in enumerate(nums):
    print(i, val)   # 0 10 / 1 20 / 2 30
# range
for i in range(2, 5):    # 2,3,4
for i in range(4, 0, -1): # 4,3,2,1 — reverse loop
# while — two pointer problems use this heavily
left, right = 0, len(nums) - 1
while left < right:
    # do something
    left += 1
    right -= 1
---
Functions
# Multiple return values — common in DSA
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])  # lo=1, hi=4

