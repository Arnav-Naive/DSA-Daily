# 🐍 Python — Dictionaries

> **Source:** Corey Schafer - Python Tutorial #5  
> **Focus:** DSA syntax reference only

---

## 📌 What is a Dictionary?

Key-value pairs — DSA mein **HashMap** ya **Hash Table** bolte hain isse.

```python
student = {
    'name'   : 'John',
    'age'    : 20,
    'gender' : 'Male',
    'courses': ['Math', 'Science', 'English'],  # value kuch bhi ho sakta hai
}
```

> **Important properties:**
>
> - Keys **unique** honi chahiye — duplicate key add karo toh purani overwrite hoti hai
> - Keys **immutable** honi chahiye — string, int, tuple ban sakti hai key. List nahi ban sakti ❌
> - Values kuch bhi ho sakti hain — list, dict, int, string, sab kuch ✅
> - Python 3.7+ mein **insertion order maintain** hoti hai

---

## 📌 Access karna

```python
print(student['name'])      # → 'John'
print(student['courses'])   # → ['Math', 'Science', 'English']

# ⚠️ Key exist nahi karti toh KeyError aata hai
print(student['phone'])     # ❌ KeyError: 'phone'

# Safe way — .get() use karo
print(student.get('phone'))          # → None   (error nahi aata)
print(student.get('phone', 'N/A'))   # → 'N/A'  (default value)
```

> **DSA mein `.get()` bahut use hota hai** — jab pata nahi key hai ya nahi:
>
> ```python
> freq = {}
> for char in "banana":
>     freq[char] = freq.get(char, 0) + 1
> # → {'b': 1, 'a': 3, 'n': 2}
> ```

---

## 📌 Add / Update / Delete

```python
# Add new key
student['phone'] = '555-5555'

# Update existing key
student['name'] = 'Jane'

# Update multiple keys ek saath — .update()
student.update({'name': 'Jannee', 'age': 26, 'phone': '111-1111'})

# Delete
del student['age']            # key-value dono remove, kuch return nahi karta
age = student.pop('age')      # value return karta hai, phir remove karta hai
                               # ⚠️ key nahi mili toh KeyError — safe way:
age = student.pop('age', None) # → None return karta hai agar key nahi hai
```

---

## 📌 Useful Methods

```python
len(student)          # → 4   kitne key-value pairs hain

# ⚠️ Tere notes mein ye mistake thi:
student.keys()        # ✅ parentheses zaroori hain — keys return karta hai
student.values()      # ✅ parentheses zaroori hain — values return karta hai
student.items()       # ✅ (key, value) tuples ki list return karta hai

# Check karna — key exist karti hai ya nahi
'name' in student         # → True   (keys mein check karta hai)
'John' in student         # → False  (values mein nahi dhundta)
'John' in student.values()# → True   (values mein check karna ho toh)
```

---

## 📌 Looping

```python
# Sirf keys
for key in student:
    print(key)
# → name, age, gender, courses

# Sirf values
for value in student.values():
    print(value)

# Key aur value dono
for key, value in student.items():
    print(key, value)
# → name John
#   age 20
#   gender Male
#   courses ['Math', 'Science', 'English']
```

---

## 📌 Nested Dictionary

```python
users = {
    'user1': {'name': 'John', 'age': 20},
    'user2': {'name': 'Jane', 'age': 25},
}

users['user1']['name']   # → 'John'
users['user2']['age']    # → 25
```

---

## 📌 Empty Dictionary

```python
empty = {}        # ✅ dict
empty = dict()    # ✅ dict

# ⚠️ {} set nahi hai — set ke liye set() use karo
```

---

## 🎯 DSA Section — Dictionary ke Common Patterns

### 1. Frequency Counter — sabse common pattern

```python
# Character frequency
s = "banana"
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
# → {'b': 1, 'a': 3, 'n': 2}

# Ya collections.Counter se (shortcut):
from collections import Counter
Counter("banana")   # → Counter({'a': 3, 'n': 2, 'b': 1})
```

### 2. Two Sum — classic interview problem

```python
# Find two numbers that add up to target
nums = [2, 7, 11, 15]
target = 9

seen = {}
for i, num in enumerate(nums):
    diff = target - num
    if diff in seen:
        print([seen[diff], i])   # → [0, 1]
    seen[num] = i
```

### 3. Group karna — list of items ko categorize karna

```python
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
groups = {}
for word in words:
    key = ''.join(sorted(word))   # anagram ka sorted form same hoga
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
# → {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
```

### 4. Memoization (Recursion optimize karna)

```python
memo = {}
def fib(n):
    if n <= 1: return n
    if n in memo: return memo[n]   # already calculated hai toh dict se lo
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

---

## 📌 Quick Reference

```
CREATE      : {'key': val} | dict()
ACCESS      : d['key'] → KeyError if missing
SAFE ACCESS : d.get('key') → None | d.get('key', default)
ADD/UPDATE  : d['key'] = val | d.update({...})
DELETE      : del d['key'] | d.pop('key') | d.pop('key', None)
LENGTH      : len(d)

CHECK       : 'key' in d → checks keys only
KEYS        : d.keys()    ← parentheses zaroori!
VALUES      : d.values()  ← parentheses zaroori!
PAIRS       : d.items()

LOOP KEYS   : for k in d
LOOP BOTH   : for k, v in d.items()

EMPTY       : {} ya dict()  ← {} set nahi hai!
```

---

*Source: Corey Schafer Python Tutorial #5 | DSA focus*
