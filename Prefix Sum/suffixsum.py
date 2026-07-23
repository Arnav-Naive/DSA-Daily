arr = [3, 4, 2, 1, 5]

suffix = [0] * len(arr)
for i in range(len(arr)-2, -1, -1):
    suffix[i] = suffix[i+1] + arr[i+1]

print(suffix)