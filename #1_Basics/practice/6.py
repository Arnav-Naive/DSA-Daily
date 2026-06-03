# # n = 12345
# # while n > 0:
# #     digit = n % 10    # last digit
# #     print(digit)      # 5 4 3 2 1
# #     n = n // 10       # last digit remove       

# nums = [1, 2, 3, 4]
# # Saare pairs print karo
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):   # i+1 taaki same pair repeat na ho
#         print(nums[i],  nums[j])


s = "hello"

# Frequency count
freq = {}
for c in s:     # when we use freq.get(c, 0) then it is more efficient than if else
    if c in freq:
        freq[c] += 1 
    else:
        freq[c] = 0
print(freq)

# Vowels count
count = 0
for c in s:
    if c in "aeiou":
        count += 1
        print(c, end = " ")
# ---------------------------------------------------------------
# .get() wala (shorter, same kaam)
for c in s:
    freq[c] = freq.get(c, 0) + 1
print(freq)