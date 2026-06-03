# 🐍 Python — Variable Scope (LEGB)

> **Source:** Corey Schafer - Python Tutorial #18  
> **Focus:** DSA syntax reference only

---

## 📌 LEGB — Python variable kahan dhundta hai?

Jab tu koi variable use karta hai, Python is order mein dhundta hai:

```
L → Local      (function ke andar)
E → Enclosing  (outer function, nested functions mein)
G → Global     (file level pe)
B → Built-in   (Python ke built-in names — len, print, range etc.)
```

> Pehle Local mein dhundega, mila nahi toh Enclosing, phir Global, phir Built-in.  
> Kahin nahi mila toh `NameError`.

---

## 📌 Local vs Global

```python
x = 'global x'   # Global

def test():
    x = 'local x'   # Local — sirf is function ke andar
    print(x)         # → 'local x'  (Local milgaya, Global tak nahi gaya)

test()
print(x)   # → 'global x'  (Global wala same hai)
```

---

## 📌 global keyword

```python
x = 'global x'

def test():
    global x          # ab x global wala hai
    x = 'modified!'   # global x change ho jaayega

test()
print(x)   # → 'modified!'
```

> ⚠️ **DSA mein `global` avoid karo** — function ke andar global variable change karna  
> bugs ka reason banta hai. Return karo instead:
> ```python
> # Bad ❌
> count = 0
> def increment():
>     global count
>     count += 1
>
> # Good ✅
> def increment(count):
>     return count + 1
>
> count = increment(count)
> ```

---

## 📌 Enclosing scope — nested functions mein

```python
def outer():
    x = 'outer x'

    def inner():
        print(x)   # Local mein nahi mila → Enclosing mein mila ✅

    inner()

outer()   # → 'outer x'
```

```python
# nonlocal — enclosing variable change karna ho toh
def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'modified!'

    inner()
    print(x)   # → 'modified!'

outer()
```

---

## 🎯 DSA Section — Scope ka practical use

### 1. Recursion mein scope — har call ka apna local scope hota hai

```python
def factorial(n):
    # har recursive call mein 'n' alag local variable hai
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Call stack:
# factorial(3) → n=3
#   factorial(2) → n=2
#     factorial(1) → n=1  ← base case
```

### 2. Counter DSA mein — global ki jagah return use karo

```python
# Simple way ✅
def count_vowels(s):
    count = 0              # local variable
    for c in s:
        if c in "aeiou":
            count += 1
    return count           # return karo, global mat banao

result = count_vowels("hello")
print(result)   # → 2
```

### 3. Nested function DSA mein — helper function pattern

```python
def solve(nums):
    result = []   # outer scope mein hai

    def helper(index):
        if index == len(nums):
            result.append(nums[:])   # result enclosing scope se access ho raha hai
            return
        helper(index + 1)

    helper(0)
    return result
```

---

## 📌 Quick Reference

```
LEGB ORDER  : Local → Enclosing → Global → Built-in

global x    : function ke andar global variable use/modify karna
nonlocal x  : nested function mein outer function ka variable modify karna

DSA RULE    : global avoid karo — parameters pass karo aur return karo ✅
```

---

*Source: Corey Schafer Python Tutorial #18 | DSA focus*