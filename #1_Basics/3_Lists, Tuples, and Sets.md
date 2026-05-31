# 🐍 Python — Lists, Tuples & Sets

> **Source:** Corey Schafer - Python Tutorial #4 + Slicing + Sorting + Mutable vs Immutable  
> **Focus:** DSA syntax reference only

---

## 📌 Quick Comparison — Teen mein se kab kya use karein?

| | List | Tuple | Set |
|---|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |
| Mutable? | ✅ Yes | ❌ No | ✅ Yes |
| Ordered? | ✅ Yes | ✅ Yes | ❌ No |
| Duplicates? | ✅ Yes | ✅ Yes | ❌ No |
| Indexing? | ✅ Yes | ✅ Yes | ❌ No |
| `in` check speed | O(n) slow | O(n) slow | O(1) fast ⚡ |

---

## 📌 LIST

### Basics & Indexing

```python
courses = ['History', 'Math', 'Phys', 'CompSci']
#index:       0          1       2        3
#neg index:  -4         -3      -2       -1

courses[0]    # → 'History'   first element
courses[-1]   # → 'CompSci'   last element  ← bahut use hota hai DSA mein
courses[0:2]  # → ['History', 'Math']   index 0,1 (2 excluded)
courses[:2]   # → ['History', 'Math']   same as above
courses[2:]   # → ['Phys', 'CompSci']   index 2 to end
courses[::-1] # → ['CompSci', 'Phys', 'Math', 'History']  reverse
```

---

### Add / Insert

```python
courses.append('Art')        # end mein add → O(1)
courses.insert(0, 'Art')     # specific index pe add → O(n)

# ⚠️ Tere notes mein ek mistake thi:
courses_2 = ['Math', 'Art']
courses.insert(0, courses_2)   # ❌ WRONG — list andar list ban jaati hai
                                # → [['Math', 'Art'], 'History', ...]

courses.extend(courses_2)      # ✅ CORRECT — elements merge hote hain
                                # → ['History', 'Math', 'Phys', 'CompSci', 'Math', 'Art']
```

---

### Remove / Pop

```python
courses.remove('Math')   # value se remove — value nahi mili toh ValueError
courses.pop()            # last element remove karta hai aur return karta hai
courses.pop(0)           # specific index se remove

popped = courses.pop()   # popped mein removed element aa jaata hai
print(popped)            # → 'CompSci'
```

---

### Sorting

```python
courses = ['History', 'Math', 'Phys', 'CompSci']
nums    = [4, 1, 24, 6]

# In-place sort (original list badal jaati hai)
courses.sort()              # alphabetical A→Z
courses.sort(reverse=True)  # alphabetical Z→A
nums.sort()                 # ascending
nums.sort(reverse=True)     # descending
courses.reverse()           # just reverse, sort nahi karta

# New list return karta hai (original same rehti hai)
sorted_courses = sorted(courses)             # A→Z, original unchanged
sorted_courses = sorted(courses, reverse=True)  # Z→A

# ⚠️ sort() vs sorted() difference:
courses.sort()          # original modify hoti hai, kuch return nahi (None)
x = sorted(courses)     # original same, naya list return hota hai
```

> **DSA mein kab kya use karein:**
> - Original bachani ho → `sorted()`
> - In-place theek hai → `.sort()`
> - `.sort()` sirf list pe kaam karta hai
> - `sorted()` kisi bhi iterable pe kaam karta hai (string, tuple, etc.)

---

### min / max / sum / index / in

```python
nums = [4, 1, 24, 6]

min(nums)               # → 1
max(nums)               # → 24
sum(nums)               # → 35

courses.index('Math')   # → 1  (index return karta hai)
                        # ⚠️ value nahi mili toh ValueError
'Math' in courses       # → True   O(n)
'Art'  in courses       # → False
```

---

### Looping — aur enumerate ka confusion clear karo

```python
courses = ['History', 'Math', 'Phys', 'CompSci']

# Normal loop
for course in courses:
    print(course)
# → History, Math, Phys, CompSci

# enumerate ke bina index chahiye toh ye karte hain log:
for i in range(len(courses)):
    print(i, courses[i])
# → 0 History, 1 Math ...  (kaam karta hai but ugly hai)

# enumerate = index + value dono ek saath — CLEAN way ✅
for index, course in enumerate(courses):
    print(index, course)
# → 0 History
#   1 Math
#   2 Phys
#   3 CompSci

# start=1 matlab counting 0 se nahi 1 se shuru hogi
for index, course in enumerate(courses, start=1):
    print(index, course)
# → 1 History
#   2 Math
#   3 Phys
#   4 CompSci
```

> **enumerate kyun use karein?**
> Jab tujhe loop mein **value bhi chahiye aur position bhi** —
> `range(len())` se ugly code hota hai, `enumerate` clean aur Pythonic hai.
> DSA mein bahut use hota hai jab index track karna ho.

---

### join — list → string

```python
courses = ['Math', 'Art', 'CompSci']

', '.join(courses)    # → 'Math, Art, CompSci'
' - '.join(courses)   # → 'Math - Art - CompSci'
''.join(courses)      # → 'MathArtCompSci'

# ⚠️ Tere notes mein ek mistake thi:
new_list = courses.join(courses)   # ❌ WRONG — join list pe nahi hota
course_str = ', '.join(courses)    # ✅ CORRECT — join STRING pe hota hai (separator)
```

---

### Slicing — List aur String dono pe same kaam karta hai

```python
my_list = [0, 1, 2, 3, 4, 5]

my_list[1:4]    # → [1, 2, 3]      start:end (end excluded)
my_list[:3]     # → [0, 1, 2]      beginning se
my_list[2:]     # → [2, 3, 4, 5]   end tak
my_list[::2]    # → [0, 2, 4]      har 2nd element
my_list[::-1]   # → [5, 4, 3, 2, 1, 0]  reverse ← DSA mein most used

# List copy karna (important!)
copy = my_list[:]       # shallow copy — original se alag
copy = my_list          # ❌ ye copy nahi, same object ka reference hai!
```

---

### Mutable vs Immutable — important concept

```python
# LIST IS MUTABLE — matlab ek variable dusre ko assign karo
# toh dono same object point karte hain

list_1 = ['History', 'Math', 'CompSci']
list_2 = list_1          # dono same list point kar rahe hain

list_1.append('Art')
print(list_1)   # → ['History', 'Math', 'CompSci', 'Art']
print(list_2)   # → ['History', 'Math', 'CompSci', 'Art']  ← ye bhi change ho gaya!

# Fix — copy banana hai toh:
list_2 = list_1.copy()   # ✅ ab alag objects hain
list_2 = list_1[:]       # ✅ ye bhi kaam karta hai
```

---

## 📌 TUPLE

```python
tuple_1 = ('Math', 'Art', 'CompSci', 'Phys')
tuple_2 = tuple_1

# Immutable hai — change nahi ho sakta
tuple_1.append('Art')   # ❌ AttributeError — tuples mein append nahi hota
tuple_1[0] = 'History'  # ❌ TypeError — item assignment nahi hota

# tuple_2 bhi same object point karta hai
# but kyunki change hi nahi ho sakta, koi problem nahi

# Jo kuch kar sakte ho:
tuple_1[0]          # ✅ indexing
tuple_1[1:3]        # ✅ slicing
'Math' in tuple_1   # ✅ membership check
for x in tuple_1:   # ✅ looping
len(tuple_1)        # ✅ length
min(tuple_1)        # ✅ min/max (comparable types ho toh)
sorted(tuple_1)     # ✅ sorted (returns list, not tuple)
```

> **DSA mein tuple kab use karein:**
> - Fixed data store karna ho jo change na ho
> - Dictionary key banana ho (list key nahi ban sakti, tuple ban sakti hai)
> - Function se multiple values return karna → `return x, y` actually tuple return karta hai
> ```python
> def min_max(lst):
>     return min(lst), max(lst)   # tuple return ho raha hai
>
> lo, hi = min_max([3,1,4,1,5])  # tuple unpacking
> ```

---

## 📌 SET

```python
cs_courses  = {'History', 'Math', 'CompSci', 'Phys', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)   # → {'History', 'Math', 'CompSci', 'Phys'}
                    # Math duplicate tha — remove ho gaya
                    # ⚠️ order guaranteed nahi hai sets mein
```

### Set Operations — DSA mein bahut kaam aate hain

```python
cs_courses.intersection(art_courses)  # dono mein common → {'History', 'Math'}
cs_courses.difference(art_courses)    # cs mein hai, art mein nahi → {'CompSci', 'Phys'}
cs_courses.union(art_courses)         # dono ka combination (no duplicates)
cs_courses.issubset(art_courses)      # kya cs, art ka subset hai? → False

# Short-hand operators (same kaam):
cs_courses & art_courses   # intersection
cs_courses - art_courses   # difference
cs_courses | art_courses   # union
```

### Set mein add/remove

```python
cs_courses.add('Art')       # ek element add
cs_courses.discard('Math')  # remove — element nahi mila toh bhi error nahi
cs_courses.remove('Math')   # remove — element nahi mila toh KeyError
```

### `in` operator — Set fastest hai

```python
'Math' in cs_courses    # → True  ← O(1) — hash table hai andar se
'Math' in [1,2,3,...]   # → O(n)  — list poori check karni padti hai
```

---

## 📌 Empty banana — ek common mistake

```python
empty_list  = []        # ✅
empty_list  = list()    # ✅

empty_tuple = ()        # ✅
empty_tuple = tuple()   # ✅

empty_set   = set()     # ✅ set() use karo
empty_set   = {}        # ❌ YE DICT HAI, SET NAHI — bahut common mistake!

empty_dict  = {}        # ✅ ye dict hai
```

---

## 🎯 DSA Section — Kab kya use karein

| Situation | Use |
|---|---|
| Order matter karta hai, duplicates hain | `list` |
| Fast lookup / membership check | `set` |
| Duplicates hatane hain | `set(my_list)` |
| Do lists ke common elements | `set(a) & set(b)` |
| Fixed data, change nahi hoga | `tuple` |
| Dict key banana hai | `tuple` (list nahi ban sakti key) |
| Multiple values return karna | `tuple` unpacking |
| Index bhi chahiye loop mein | `enumerate()` |
| List reverse karna | `lst[::-1]` ya `lst.reverse()` |
| Original bachate hue sort karna | `sorted(lst)` |

---

## 📌 Quick Reference

```
LIST    : []  — ordered, mutable, duplicates allowed
TUPLE   : ()  — ordered, immutable, duplicates allowed
SET     : {}  — unordered, mutable, NO duplicates, fast lookup

ADD     : list.append() | list.insert(i, val) | list.extend() | set.add()
REMOVE  : list.remove(val) | list.pop() | set.discard(val)
SORT    : list.sort() — in-place | sorted(list) — new list
SEARCH  : val in list → O(n) | val in set → O(1)
LOOP    : for x in lst | for i, x in enumerate(lst)
JOIN    : 'sep'.join(list) → string
SLICE   : lst[start:end:step] | lst[::-1] reverse

EMPTY   : [] list() | () tuple() | set()  ← {} nahi, wo dict hai!
```

---

*Source: Corey Schafer Python Tutorial #4 + Slicing + Sorting | DSA focus*