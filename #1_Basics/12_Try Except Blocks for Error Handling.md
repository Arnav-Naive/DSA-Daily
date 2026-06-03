# 🐍 Python — Try/Except (Error Handling)

> **Source:** Corey Schafer - Python Tutorial #20  
> **Focus:** DSA syntax reference only

---

## 📌 Basic Structure

```python
try:
    # code jo fail ho sakta hai
except:
    # error aaya toh ye run hoga
else:
    # koi error nahi aaya toh ye run hoga
finally:
    # error aaye ya na aaye — YE HAMESHA run hoga
```

---

## 📌 `e` kya hota hai — tera confusion

```python
except Exception as e:
    print(e)   # actual error message print hoga
```

> `e` = error object — isme exact error message hota hai jo Python ne diya
>
> ```python
> try:
>     x = 1 / 0
> except Exception as e:
>     print(e)          # → division by zero
>     print(type(e))    # → <class 'ZeroDivisionError'>
>
> try:
>     f = open('nofile.txt')
> except Exception as e:
>     print(e)   # → [Errno 2] No such file or directory: 'nofile.txt'
> ```
>
> `as e` optional hai — sirf tab use karo jab exact message dekhna/print karna ho

---

## 📌 Specific vs General Exception

```python
# ❌ Bad — sab kuch ek saath pakad lega, pata nahi kya hua
try:
    f = open('test_file.txt')
    var = bad_var
except Exception:
    print('Something went wrong')   # file error tha ya bad_var? pata nahi

# ✅ Good — specific pehle, general baad mein
try:
    f = open('test_file.txt')
    var = bad_var
except FileNotFoundError as e:
    print('File nahi mili:', e)     # sirf file error pakdega
except NameError as e:
    print('Variable nahi mila:', e) # sirf name error pakdega
except Exception as e:
    print('Kuch aur hua:', e)       # baaki sab
```

> ⚠️ **Order matter karta hai** — specific exceptions pehle, `Exception` hamesha last mein

---

## 📌 else aur finally

```python
try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print('File nahi mili:', e)
except Exception as e:
    print('Kuch aur hua:', e)
else:
    # sirf tab run hoga jab try mein koi error NA aaya ho
    print(f.read())
    f.close()
finally:
    # hamesha run hoga — error aaye ya na aaye
    print('Done!')
```

> **Simple rule:**
> - `else` → success pe kuch karna ho
> - `finally` → cleanup karna ho (file close, connection close etc.) — hamesha run hoga

---

## 📌 Common Exceptions — yaad rakhne wale

```python
ZeroDivisionError    # 1/0
ValueError           # int("abc")  — wrong type ki value
TypeError            # "2" + 2     — wrong type operation
IndexError           # [1,2,3][5]  — list out of range
KeyError             # d['key']    — dict mein key nahi hai
FileNotFoundError    # open('nofile.txt')
NameError            # undefined_var — variable exist nahi karta
AttributeError       # "str".append() — method exist nahi karta
OverflowError        # bahut bada number
RecursionError       # infinite recursion — base case nahi tha
```

---

## 📌 raise — khud error throw karna

```python
# Simple way
def divide(a, b):
    if b == 0:
        raise ValueError("b zero nahi ho sakta!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)   # → b zero nahi ho sakta!
```

---

## 🎯 DSA Section — Kab kahan use karo

### 1. Safe type conversion — input validate karna

```python
# Simple way
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None   # convert nahi hua toh None return karo

safe_int("42")    # → 42
safe_int("abc")   # → None  (error nahi aayega)
```

### 2. Index safe access

```python
# Simple way
def safe_get(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

safe_get([1, 2, 3], 5)   # → None  (IndexError nahi aayega)
```

### 3. Division safe

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
```

### 4. Recursion limit

```python
# Deep recursion mein RecursionError aa sakta hai
import sys
sys.setrecursionlimit(10000)   # default 1000 hai, bada kar sakte ho

# Better solution — recursion ki jagah iteration use karo jab possible ho
```

---

## 📌 Quick Reference

```
try       : ye code run karo
except E  : E error aaya toh ye karo
except E as e : e mein exact error message hoga
else      : koi error nahi aaya toh ye karo
finally   : hamesha run hoga (error ho ya na ho)

raise     : khud error throw karo

COMMON    : ZeroDivisionError, ValueError, TypeError,
            IndexError, KeyError, FileNotFoundError,
            NameError, RecursionError

ORDER     : specific exceptions pehle → Exception last mein
```

---

*Source: Corey Schafer Python Tutorial #20 | DSA focus*