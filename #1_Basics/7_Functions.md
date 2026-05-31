# 🐍 Python — Functions

> **Source:** Corey Schafer - Python Tutorial #8  
> **Focus:** DSA syntax reference only

---

## 📌 Basic Function

```python
# Define
def hello_func():
    print("Hello!")    # ⚠️ () mat bhoolna — tere notes mein ye tha

# Call
hello_func()           # → Hello!
```

---

## 📌 return vs print — ye samajhna zaroori hai

```python
# print — sirf screen pe dikhata hai, kuch return nahi karta
def hello_print():
    print("Hello!")

result = hello_print()   # "Hello!" screen pe dikhega
print(result)            # → None   (kuch return nahi kiya toh None milta hai)


# return — value wapas bhejta hai caller ko
def hello_return():
    return "Hello!"

result = hello_return()  # kuch screen pe nahi dikhega
print(result)            # → "Hello!"
```

> **Simple explanation:**
>
> - `print` — sirf dikhao, store nahi kar sakte
> - `return` — value wapas lo, usse store kar sako, aage use kar sako
>
> ```python
> # print ke saath — aage use nahi kar sakte
> def add_print(a, b):
>     print(a + b)
>
> result = add_print(2, 3)   # 5 screen pe dikhega
> result * 2                 # ❌ Error — result is None
>
> # return ke saath — aage use kar sakte ho ✅
> def add_return(a, b):
>     return a + b
>
> result = add_return(2, 3)  # kuch screen pe nahi dikhega
> result * 2                 # → 10  ✅
> ```

> **DSA mein hamesha `return` use karo** — function ka output agle step mein use karna hota hai

---

## 📌 Parameters & Arguments

```python
# Parameter — function define karte waqt (variable name)
def greet(name):          # name = parameter
    return f"Hello {name}"

# Argument — function call karte waqt (actual value)
greet("Arnav")            # "Arnav" = argument


# Default parameter — value na di toh default use hoga
def greet(name="stranger"):
    return f"Hello {name}"

greet("Arnav")   # → "Hello Arnav"
greet()          # → "Hello stranger"
```

---

## 📌 *args — multiple positional arguments

> **Simple explanation:** Jab pata nahi kitne arguments aayenge, tab `*args` use karo.  
> Andar se ye ek **tuple** hota hai.

```python
# Bina *args — fixed number of arguments
def add(a, b):
    return a + b

add(1, 2)        # ✅
add(1, 2, 3)     # ❌ Error — 3 arguments, 2 expected


# *args ke saath — kitne bhi arguments do
def add(*args):
    print(args)        # → (1, 2, 3)  tuple hai ye
    print(type(args))  # → <class 'tuple'>

    # Simple way
    total = 0
    for num in args:
        total += num
    return total

add(1, 2)         # → 3
add(1, 2, 3)      # → 6
add(1, 2, 3, 4)   # → 10
```

---

## 📌 **kwargs — multiple keyword arguments

> **Simple explanation:** Jab naam ke saath arguments dene ho (`name="Arnav"`), tab `**kwargs` use karo.  
> Andar se ye ek **dictionary** hota hai.

```python
def student_info(**kwargs):
    print(kwargs)        # → {'name': 'Arnav', 'age': 21}
    print(type(kwargs))  # → <class 'dict'>

    # Simple way — dict ki tarah use karo
    for key, value in kwargs.items():
        print(key, value)

student_info(name="Arnav", age=21)
# → name Arnav
#   age 21
```

---

## 📌 *args + **kwargs saath mein

```python
def student_info(*args, **kwargs):
    print(args)    # tuple  → positional args
    print(kwargs)  # dict   → keyword args

student_info("Math", "Science", name="Arnav", age=21)
# args   → ('Math', 'Science')
# kwargs → {'name': 'Arnav', 'age': 21}
```

> ⚠️ Order zaroori hai — hamesha `*args` pehle, `**kwargs` baad mein

---

## 📌 Tere notes ka confusion — * aur ** unpacking

```python
courses = ["Math", "Science"]
info    = {"name": "Arnav", "age": 21}

# Bina unpacking — list aur dict as single argument jaata hai
student_info(courses, info)
# args   → (['Math', 'Science'], {'name': 'Arnav', 'age': 21})
# kwargs → {}
# matlab poori list ek argument ban gayi

# * aur ** se unpacking — elements alag alag jaate hain ✅
student_info(*courses, **info)
# args   → ('Math', 'Science')     list ke elements alag ho gaye
# kwargs → {'name': 'Arnav', 'age': 21}   dict ke pairs alag ho gaye
```

> **Simple rule:**
>
> - `*list` → list ke elements alag alag positional arguments ban jaate hain
> - `**dict` → dict ke key-value pairs keyword arguments ban jaate hain

---

## 📌 Docstring — function ko document karna

```python
def is_leap(year):
    """Return True if year is a leap year, False otherwise."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Docstring dekhna ho toh
help(is_leap)      # → Return True if year is a leap year...
print(is_leap.__doc__)
```

---

## 📌 Tere notes ka example — days_in_month

```python
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#              ^index 0 placeholder hai taaki month_days[1] = Jan, [2] = Feb

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2024))      # ❌ Error — month argument missing hai
print(days_in_month(2024, 2))   # → 29  (2024 leap year hai)
print(days_in_month(2024, 1))   # → 31  (January)
```

---

## 📌 Multiple return values

```python
# Simple way
def min_max(lst):
    minimum = lst[0]
    maximum = lst[0]

    for num in lst:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum    # tuple return hota hai

result = min_max([3, 1, 4, 1, 5])
print(result)        # → (1, 5)

# Unpacking se alag alag variable mein
lo, hi = min_max([3, 1, 4, 1, 5])
print(lo)   # → 1
print(hi)   # → 5
```

---

## 🎯 DSA Section — Function Patterns

### 1. Simple function with return

```python
def is_even(n):
    return n % 2 == 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

### 2. Function calling another function

```python
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_strong(n):
    # Strong number — sum of factorials of digits == number
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10
    return total == n

print(is_strong(145))   # → True  (1! + 4! + 5! = 145)
```

### 3. Default arguments DSA mein

```python
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    # ...
```

---

## 📌 Quick Reference

```
DEFINE      : def func_name(params):
RETURN      : return value  ← hamesha return use karo, print nahi
CALL        : func_name(args)

DEFAULT     : def func(x, y=10)  ← y ki value na di toh 10 use hoga
*args       : multiple positional args → tuple ban jaata hai andar
**kwargs    : multiple keyword args   → dict ban jaata hai andar

UNPACKING   : func(*list) | func(**dict)
DOCSTRING   : """description""" — function ke andar pehli line

MULTIPLE RETURN : return a, b  → tuple return hota hai
UNPACK RETURN   : x, y = func()
```

---

*Source: Corey Schafer Python Tutorial #8 | DSA focus*
