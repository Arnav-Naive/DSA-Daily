# `if __name__ == '__main__'`

## 🟢 1. Beginner Level: The Simple Mental Model

Python me `__name__` ek hidden automatic variable hota hai jo har file (`.py`) ke paas pehle se hota hai. Yeh variable Python ko batata hai ki file **kahan** aur **kaise** chal rahi hai.

- **Rule 1:** Agar tum kisi file ko **Direct Run** karte ho (jaise terminal me `python script.py` likh kar), toh Python uske `__name__` variable ke andar ki value `"__main__"` set kar deta hai.
- **Rule 2:** Agar us file ko tum kisi doosri file me **`import`** karte ho, toh uske `__name__` variable ki value badal kar **uss file ka apna naam** ho jati hai.

---

## 🟡 2. Intermediate Level: Why and How to Use It

Jab tum `import` use karte ho, toh Python us imported file ke saare top-level code (functions ke bahar likhi hui cheezein) ko turant execute kar deta hai. Hum is automatic execution ko rokne ke liye conditional block lagate hain.

### The Problem (Bina Iske)

Socho tumne ek file banayi `math_helper.py`:

```python
def square(n):
    return n * n

# Yeh print statement hamesha chalega jab bhi koi is file ko touch karega
print("Testing square of 4:", square(4))
```

### The Fix (Iske Saath)

```python
def square(n):
    return n * n

if __name__ == '__main__':
    print("Testing square of 4:", square(4))
```

Ab `print` sirf tab chalega jab tum **directly** `math_helper.py` run karoge. Import karne par nahi chalega.

---

### Real Example (Images se)

**`file_1.py`** — function define karo + simple test block:

```python
def add(x, y):
    return x + y

if __name__ == '__main__':
    if add(1, 2) == 3:
        print("Pass")
    else:
        print("Fail")
```

**`file_2.py`** — sirf function use karo:

```python
import file_1

print(file_1.add(1, 2))   # Output: 3
```

| Kaun run kiya? | Kya hua? |
|---|---|
| `python file_1.py` | `Pass` print hua (test block chala) |
| `python file_2.py` | `3` print hua (test block nahi chala) |

> ✅ **Great for simple testing** — quick Pass/Fail checks ke liye yeh pattern theek hai.
> ❌ **Not for advanced testing** — production-level testing ke liye `unittest` ya `pytest` use karo.
