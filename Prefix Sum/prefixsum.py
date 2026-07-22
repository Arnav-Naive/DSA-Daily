arr = [3, 4, 2, 1, 5]

prefix = [0] * len(arr)
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i-1]

print(prefix)