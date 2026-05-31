# 🐍 Python — Conditionals & Booleans

> **Source:** Corey Schafer - Python Tutorial #6  
> **Focus:** DSA syntax reference only

---

## 📌 Comparison Operators (already pata hai tujhe)

```python
==   # equal
!=   # not equal
>    # greater than
<    # less than
>=   # greater than or equal
<=   # less than or equal
```

---

## 📌 if / elif / else

```python
x = 10

if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
else:
    print("Less")
```

---

## 📌 Logical Operators — and / or / not

```python
x = 5

# and — dono true hone chahiye
if x > 0 and x < 10:
    print("Single digit positive")   # → prints this

# or — ek bhi true ho toh chalega
if x < 0 or x > 3:
    print("Yes")   # → prints this

# not — condition ulti kar deta hai
if not x == 10:
    print("Not ten")   # → prints this
```

---

## 📌 is vs == — identity vs equality

```python
a = [1, 2, 3]
b = [1, 2, 3]

# == checks value (values same hain?)
print(a == b)   # → True   (values same hain)

# is checks identity (same object hai memory mein?)
print(a is b)   # → False  (alag objects hain memory mein)

print(id(a))    # alag id
print(id(b))    # alag id

# Same object kab hoga?
c = a           # c aur a same object point kar rahe hain
print(a is c)   # → True
print(id(a) == id(c))  # → True
```

> **DSA mein:**
>
> - Values compare karna ho → `==` use karo (99% cases)
> - `None` check karna ho → `is None` use karo (standard way)
>
> ```python
> if result is None:
>     print("Not found")
> ```

---

## 📌 Falsy Values — ye sab `False` jaisa behave karta hai

```python
# Ye sab if condition mein False maane jaate hain:
False
None
0          # zero (int)
0.0        # zero (float)
''         # empty string
[]         # empty list
()         # empty tuple
{}         # empty dict ya set
```

```python
# Standard way — check karna ki value hai ya nahi
name = ''

if name:
    print("Name exists")
else:
    print("Name is empty")   # → ye print hoga

# Ye dono same kaam karte hain:
if name != '':   # explicit check
if name:         # Pythonic check (falsy use karta hai)
```

> **DSA mein kahan aata hai:**
>
> ```python
> # Stack empty hai ya nahi check karna
> stack = []
> if stack:              # stack mein kuch hai
>     top = stack.pop()
>
> # String empty hai ya nahi
> s = ""
> if not s:
>     print("Empty string")
> ```

---

## 📌 Nested if

```python
x = 15

if x > 0:
    if x > 10:
        print("Greater than 10")
    else:
        print("Between 0 and 10")
else:
    print("Negative or zero")
```

---

## 📌 Ternary Operator — one line if/else

```python
# Standard form:
x = 10
if x > 5:
    result = "Big"
else:
    result = "Small"

# Shortcut (ek line mein):
result = "Big" if x > 5 else "Small"
```

> Simple conditions mein use karo, complex mein mat karo — confusing lagta hai

---

## 🎯 DSA Section

| Situation | Use |
|---|---|
| Values compare karna | `==` |
| Same object check karna | `is` |
| None check karna | `if x is None` |
| Empty list/string/dict check | `if not lst` |
| Range check | `if 0 <= x < n` |
| Multiple conditions | `and` / `or` |

```python
# Range check — DSA mein bahut common
n = len(arr)
if 0 <= index < n:       # valid index hai ya nahi
    print(arr[index])

# Multiple conditions
if x > 0 and x % 2 == 0:    # positive even number
    print("Positive even")
```

---

## 📌 Quick Reference

```
COMPARISON  : ==  !=  >  <  >=  <=
LOGICAL     : and | or | not
IDENTITY    : is | is not  (None check ke liye)
FALSY       : False, None, 0, 0.0, '', [], (), {}

if x:           → True if x is not falsy
if not x:       → True if x is falsy
if x is None:   → None check karna ho toh
```

---

*Source: Corey Schafer Python Tutorial #6 | DSA focus*
