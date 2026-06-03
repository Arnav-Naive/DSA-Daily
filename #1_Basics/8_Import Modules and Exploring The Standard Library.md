# 🐍 Python — Modules & Standard Library

> **Source:** Corey Schafer - Python Tutorial #9  
> **Focus:** DSA syntax reference only

---

## 📌 Module kya hota hai?

Ek alag `.py` file jisme functions, variables etc. hote hain — doosri files mein import kar sako.

---

## 📌 Import karne ke tarike

```python
# Way 1 — poora module import karo, naam se access karo
import my_module
my_module.find_index(courses, 'Math')

# Way 2 — alias de do (short naam)
import my_module as mm
mm.find_index(courses, 'Math')

# Way 3 — specific cheez import karo
from my_module import find_index
find_index(courses, 'Math')   # seedha use karo, module naam nahi chahiye

# Way 4 — multiple cheezein ek saath
from my_module import find_index, test
```

> **Simple rule:**
>
> - Apna module → `import my_module as mm`
> - Sirf ek function chahiye → `from my_module import func`
> - Standard library → `import math`, `import os` etc.

---

## 📌 sys.path — Python module kahan dhundta hai?

```python
import sys
print(sys.path)   # list of directories jahan Python modules dhundta hai
```

> Jab `import my_module` likhte ho, Python in sab folders mein dhundta hai.  
> Agar module kisi aur location pe hai:
>
> ```python
> sys.path.append('/path/to/your/directory')
> import my_module   # ab mil jaayega
> ```

---

## 📌 os.getcwd() — current working directory

```python
import os
print(os.getcwd())   # current directory ka path deta hai
                     # jahan se script run ho rahi hai
```

---

## 📌 `__file__` — module ki location

```python
import my_module
print(my_module.__file__)   # module ki exact file path batata hai
```

> `__` (dunder) ke baare mein aage OOP mein padhunga — abhi ignore karo

---

## 🎯 DSA Section — Standard Library jo DSA mein kaam aati hai

### `math` — most used in DSA

```python
import math

math.sqrt(25)       # → 5.0   square root
math.floor(3.7)     # → 3     round down
math.ceil(3.2)      # → 4     round up
math.factorial(5)   # → 120
math.gcd(12, 8)     # → 4     GCD of two numbers
math.inf            # → infinity  (min tracking mein use hota hai)
math.log(8, 2)      # → 3.0   log base 2 of 8
```

### `random` — kabhi kabhi DSA problems mein

```python
import random

random.choice([1, 2, 3, 4])     # list se random ek element
random.randint(1, 10)           # 1 se 10 ke beech random int (dono inclusive)
random.shuffle(my_list)         # list in-place shuffle karta hai
```

### `collections` — DSA mein bahut important ⚡

```python
from collections import Counter, deque, defaultdict

# Counter — frequency count ek line mein
Counter("banana")          # → Counter({'a': 3, 'n': 2, 'b': 1})
Counter([1, 2, 2, 3, 3])   # → Counter({2: 2, 3: 2, 1: 1})

# deque — double ended queue (stack + queue dono kaam karta hai)
dq = deque([1, 2, 3])
dq.append(4)        # right se add   → [1, 2, 3, 4]
dq.appendleft(0)    # left se add    → [0, 1, 2, 3, 4]
dq.pop()            # right se remove
dq.popleft()        # left se remove  ← list mein ye O(n) hota, deque mein O(1) ⚡

# defaultdict — key nahi mili toh default value deta hai, KeyError nahi

# Simple way (bina defaultdict)
freq = {}
for c in "banana":
    if c not in freq:
        freq[c] = 0
    freq[c] += 1

# Shortcut (defaultdict se)
freq = defaultdict(int)   # default value = 0
for c in "banana":
    freq[c] += 1          # KeyError nahi aayega
```

### `heapq` — priority queue DSA mein

```python
import heapq

nums = [3, 1, 4, 1, 5, 9]

# Min heap
heapq.heapify(nums)              # list ko heap mein convert karo
heapq.heappush(nums, 2)          # element add karo
smallest = heapq.heappop(nums)   # smallest element nikalo

# K largest/smallest elements — common interview question
heapq.nlargest(3, nums)     # → top 3 largest
heapq.nsmallest(3, nums)    # → top 3 smallest
```

### `datetime` & `calendar`

```python
import datetime
import calendar

datetime.date.today()       # → aaj ki date
calendar.isleap(2024)       # → True (2024 leap year hai)
```

---

## 📌 Quick Reference

```
IMPORT          : import module | import module as m | from module import func

SYS.PATH        : Python yahan dhundta hai modules ko
OS.GETCWD()     : current directory ka path

# DSA ke liye important modules:
math            : sqrt, floor, ceil, factorial, gcd, inf, log
collections     : Counter, deque, defaultdict   ← bahut use hoga
heapq           : min heap, nlargest, nsmallest
random          : choice, randint, shuffle
```

---

*Source: Corey Schafer Python Tutorial #9 | DSA focus*
