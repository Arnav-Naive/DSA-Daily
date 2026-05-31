# 🐍 Python — Loops & Iteration

> **Source:** Corey Schafer - Python Tutorial #7  
> **Focus:** DSA syntax reference only

---

## 📌 for Loop — basic

```python
# List
courses = ['Math', 'Science', 'English']
for course in courses:
    print(course)

# String (characters pe bhi loop chalta hai)
for char in "hello":
    print(char)   # h, e, l, l, o

# Tuple
for item in (1, 2, 3):
    print(item)

# Set (order guaranteed nahi)
for item in {1, 2, 3}:
    print(item)

# Dictionary
for key in student:
    print(key)            # sirf keys

for key, val in student.items():
    print(key, val)       # key aur value dono
```

---

## 📌 range() — DSA mein sabse zyada use hota hai

```python
range(5)        # 0, 1, 2, 3, 4        (0 se start, 5 excluded)
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8        (step = 2)
range(10, 0, -1)# 10, 9, 8 ... 1       (reverse, step = -1)

# Loop with index
for i in range(len(courses)):
    print(i, courses[i])

# Sirf n baar kuch karna ho
for i in range(5):
    print(i)   # 0 1 2 3 4
```

---

## 📌 while Loop

```python
# Standard form
i = 0
while i < 5:
    print(i)
    i += 1    # ⚠️ ye bhool gaye toh infinite loop

# Condition pe based
num = 10
while num > 0:
    print(num)
    num -= 1
```

> **DSA mein while kab use karein:**
>
> - Do pointers (left, right) — jab tak cross na karein
> - Binary search
> - Number ke digits process karna (`while n > 0`)
> - Queue/Stack based problems

---

## 📌 break / continue / pass

```python
# break — loop bilkul band kar do
for i in range(10):
    if i == 5:
        break
    print(i)   # 0 1 2 3 4

# continue — current iteration skip karo, loop chalta rahe
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)   # 1 3 5 7 9  (even skip ho gaye)

# pass — kuch nahi karna (placeholder)
for i in range(5):
    pass   # error nahi aayega, kuch nahi karega
```

---

## 📌 enumerate() — index + value dono chahiye toh

```python
courses = ['Math', 'Science', 'English']

# Bina enumerate (ugly)
for i in range(len(courses)):
    print(i, courses[i])

# enumerate ke saath (clean) ✅
for i, course in enumerate(courses):
    print(i, course)
# → 0 Math
#   1 Science
#   2 English

# 1 se start karna ho toh
for i, course in enumerate(courses, start=1):
    print(i, course)
# → 1 Math
#   2 Science
#   3 English
```

---

## 📌 Nested Loops — 2D problems ke liye

```python
# Matrix traverse karna
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item)

# Index ke saath
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j])
```

> ⚠️ Nested loop = O(n²) — DSA mein avoid karna hota hai jab possible ho

---

## 📌 Loop ke saath else — lesser known but useful

```python
# else block tab run hota hai jab loop normally complete ho
# (break nahi hua ho)

for i in range(5):
    if i == 10:     # ye kabhi true nahi hoga
        break
else:
    print("Loop completed")   # → ye print hoga

# Practical use — prime check
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")   # sirf tab print hoga jab koi factor nahi mila
```

---

## 🎯 DSA Section — Common Loop Patterns

### 1. Array traverse + condition

```python
nums = [1, 2, 3, 4, 5]

# Sum
total = 0
for num in nums:
    total += num

# Max element
max_val = nums[0]
for num in nums:
    if num > max_val:
        max_val = num
```

### 2. Two pointer — while loop se

```python
arr = [1, 2, 3, 4, 5]
left  = 0
right = len(arr) - 1

while left < right:
    print(arr[left], arr[right])
    left  += 1
    right -= 1
```

### 3. Number ke digits nikalna

```python
n = 12345
while n > 0:
    digit = n % 10    # last digit
    print(digit)      # 5 4 3 2 1
    n = n // 10       # last digit remove
```

### 4. Nested loop — pairs dhundna

```python
nums = [1, 2, 3, 4]
# Saare pairs print karo
for i in range(len(nums)):
    for j in range(i+1, len(nums)):   # i+1 taaki same pair repeat na ho
        print(nums[i], nums[j])
```

### 5. String characters pe loop

```python
s = "hello"

# Frequency count
freq = {}
for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 0

# .get() wala (shorter, same kaam)
for c in s:
    freq[c] = freq.get(c, 0) + 1

# Vowels count
count = 0
for c in s:
    if c in "aeiou":
        count += 1
```

---

## 📌 Quick Reference

```
for x in iterable     → list, string, tuple, set, dict pe loop
for i in range(n)     → 0 to n-1
for i in range(a,b)   → a to b-1
for i in range(a,b,s) → a to b-1, step s
for i,v in enumerate  → index + value dono

while condition       → jab tak condition true hai

break                 → loop band karo
continue              → current iteration skip
pass                  → kuch mat karo (placeholder)

for...else            → loop bina break ke complete hua toh else chalega
```

---

*Source: Corey Schafer Python Tutorial #7 | DSA focus*
