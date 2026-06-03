# 🐍 Python — 5 Common Mistakes

> **Source:** Corey Schafer - Python Tutorial #26  
> **Focus:** DSA syntax reference only

---

## ❌ Mistake 1 — Indentation & Spaces

```python
# Tabs aur spaces mix mat karo — always use 4 spaces (ya consistent tabs)
# Most editors automatically handle this

# Bad ❌
def func():
	x = 1    # tab
        y = 2    # spaces — IndentationError aayega

# Good ✅
def func():
    x = 1    # 4 spaces
    y = 2    # 4 spaces
```

---

## ❌ Mistake 2 — Naming Conflicts

```python
# Built-in names ko variable name mat banao

# Bad ❌
list = [1, 2, 3]      # 'list' built-in hai, ab use nahi kar sakte
print(list([1,2,3]))  # → TypeError

input = 'hello'       # 'input' function hai built-in
sum = 10              # 'sum' function hai built-in

# Good ✅
my_list = [1, 2, 3]
user_input = 'hello'
total = 10
```

> **DSA mein common trap** — `list`, `dict`, `set`, `input`, `sum`, `min`, `max`, `id`  
> ye sab built-in hain — variable name mat banana inhe

---

## ❌ Mistake 3 — Mutable Default Arguments ⚠️ IMPORTANT

### Problem samajhte hain:

```python
def add_employee(emp, emp_list=[]):   # ❌ [] ek baar banta hai, hamesha same list
    emp_list.append(emp)
    print(emp_list)

add_employee('Corey')   # → ['Corey']
add_employee('John')    # → ['Corey', 'John']   ← naya list nahi bana!
add_employee('Jane')    # → ['Corey', 'John', 'Jane']
```

> **Why?** Default argument `[]` sirf ek baar — jab function **define** hota hai tab banta hai.  
> Har call pe naya list nahi banta — same purana list reuse hota hai.
>
> Aise socho:
> ```
> Function define hua  →  emp_list = []  bana (ek baar)
> Call 1: add_employee('Corey')  →  same [] mein add → ['Corey']
> Call 2: add_employee('John')   →  same list mein add → ['Corey', 'John']
> Call 3: add_employee('Jane')   →  same list mein add → ['Corey', 'John', 'Jane']
> ```

### Fix — `None` use karo default mein:

```python
# ✅ Correct way
def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []       # ab har call pe naya list banta hai
    emp_list.append(emp)
    print(emp_list)

add_employee('Corey')   # → ['Corey']
add_employee('John')    # → ['John']    ← naya list!
add_employee('Jane')    # → ['Jane']    ← naya list!

# Explicitly list do toh wahi use hogi
emps = ['John', 'Jane']
add_employee('Corey', emps)   # → ['John', 'Jane', 'Corey']
```

> **Rule:** Default argument mein **kabhi mutable value mat rakho** — `[]`, `{}`, `set()`  
> Hamesha `None` rakho aur function ke andar check karo

---

## ❌ Mistake 4 — datetime ka same issue (tera confusion)

```python
# Bad ❌ — datetime.now() ek baar evaluate hota hai jab function define hota hai
from datetime import datetime
import time

def display_time(time=datetime.now()):   # YE SIRF EK BAAR RUN HOTA HAI
    print(time.strftime('%B %d, %Y %H:%M:%S'))

display_time()    # → same time
time.sleep(1)
display_time()    # → same time  ← time change nahi hua!
```

> **Why same time?** `datetime.now()` function define hote waqt ek baar run hua.  
> Uske baad har call pe wahi stored value use hoti hai — naya `now()` nahi chalata.

```python
# Good ✅ — None use karo, function ke andar now() call karo
def display_time(t=None):
    if t is None:
        t = datetime.now()    # ab har call pe fresh time milega
    print(t.strftime('%B %d, %Y %H:%M:%S'))

display_time()    # → current time
time.sleep(1)
display_time()    # → 1 second baad ka time ✅
```

> **Same concept hai mistake 3 jaisa** — mutable/dynamic default values `None` se replace karo

---

## ❌ Mistake 5 — `import *` (Star Import)

```python
# Bad ❌
from math import *       # math ke SAARE functions import ho gaye
from os import *         # os ke SAARE functions import ho gaye

# Ab pata nahi kaunsa function kahan se aaya
# Naming conflicts ho sakte hain

# Good ✅ — sirf jo chahiye wo import karo
from math import sqrt, floor, ceil
import os
```

> **DSA mein** — hamesha specific import karo, `*` se avoid karo

---

## 🎯 DSA Section — Ye mistakes DSA mein kahan aati hain

### Mutable default arg — DSA trap

```python
# Bad ❌ — graph problems mein ye mistake common hai
def dfs(node, visited=[]):    # ❌ visited list share hogi
    visited.append(node)
    ...

# Good ✅
def dfs(node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    ...
```

### Naming conflict — DSA trap

```python
# Bad ❌ — built-in names shadow ho jaate hain
list = [1, 2, 3]
max = 10
sum = 0
input = "hello"

# Good ✅
nums = [1, 2, 3]
max_val = 10
total = 0
user_input = "hello"
```

---

## 📌 Quick Reference

```
❌ Mistake 1 : Tabs + spaces mix mat karo — consistent raho
❌ Mistake 2 : list, dict, sum, max, min, input — variable name mat banao
❌ Mistake 3 : Default arg mein [] {} set() mat rakho → None use karo
❌ Mistake 4 : Default mein datetime.now() mat rakho → None use karo
❌ Mistake 5 : from module import * mat karo → specific import karo

RULE        : Mutable ya dynamic value kabhi default argument mein nahi
FIX         : def func(x=None): → if x is None: x = []
```

---

*Source: Corey Schafer Python Tutorial #26 | DSA focus*