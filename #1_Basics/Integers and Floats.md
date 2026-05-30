# 🐍 Python — Integers & Floats

> **Source:** Corey Schafer - Python Tutorial #3  
> **Tera focus:** DSA syntax reference — quick dekho aur kaam karo

---

## 📌 Types — int vs float

```python
x = 5      # int   → whole number, no decimal
y = 2.5    # float → has decimal point

type(x)    # → <class 'int'>
type(y)    # → <class 'float'>

# int + int   = int
# int + float = float  (Python auto-converts)
print(5 + 2)    # → 7      (int)
print(5 + 2.0)  # → 7.0   (float)
```

---

## 📌 Arithmetic Operators

```python
a = 5
b = 2

a + b    # → 7    addition
a - b    # → 3    subtraction
a * b    # → 10   multiplication
a / b    # → 2.5  division       ← ALWAYS returns float
a // b   # → 2    floor division ← ALWAYS returns int (rounds DOWN)
a ** b   # → 25   exponentiation (a to the power b)
a % b    # → 1    modulo (remainder)
```

> ⚠️ **`/` vs `//` — ye confuse karta hai sabko:**
>
> ```python
> 7 / 2    # → 3.5   (float, exact division)
> 7 // 2   # → 3     (int, floor — chops decimal)
> -7 // 2  # → -4    (floor DOWN karta hai, -3.5 → -4)
> ```

---

## 📌 Augmented Assignment (Shorthand)

```python
num = 10

num += 1   # num = num + 1  → 11
num -= 1   # num = num - 1  → 10
num *= 2   # num = num * 2  → 20
num /= 2   # num = num / 2  → 10.0  (becomes float!)
num **= 2  # num = num ** 2 → 100.0
num %= 3   # num = num % 3  → 1.0
```

> **DSA mein `+=` sabse zyada use hota hai** — counters, sums, etc.

---

## 📌 Built-in Functions

```python
abs(-7)         # → 7      absolute value (negative → positive)
abs(7)          # → 7      already positive, no change

round(3.5)      # → 4      rounds to nearest even (banker's rounding)
round(3.55, 1)  # → 3.6    2nd arg = decimal places rakhne hain
round(2.675, 2) # → 2.67   ⚠️ float precision issue, careful

pow(2, 10)      # → 1024   same as 2 ** 10
pow(2, 10, 100) # → 24     (2**10) % 100  ← 3rd arg = modulo, DSA mein use hota hai

min(3, 1, 4, 1) # → 1
max(3, 1, 4, 1) # → 4
sum([1,2,3,4])  # → 10
```

---

## 📌 Comparison Operators

```python
num_1 = 3
num_2 = 2

num_1 > num_2   # → True   greater than
num_1 < num_2   # → False  less than
num_1 >= num_2  # → True   greater than OR equal   ← tere notes mein miss tha
num_1 <= num_2  # → False  less than OR equal       ← tere notes mein miss tha
num_1 == num_2  # → False  equal to
num_1 != num_2  # → True   not equal to
```

> **Comparison ka result hamesha `True` ya `False` hota hai** — ye boolean hai

---

## 📌 Type Conversion

```python
# String → int / float
num_1 = '100'
num_2 = '200'
print(int(num_1) + int(num_2))   # → 300

# int ↔ float
int(2.9)    # → 2      (decimal chop ho jata hai, round NAHI hota!)
float(5)    # → 5.0

# int → string (useful in DSA — digits ko iterate karna ho)
str(123)    # → '123'
list(str(123))   # → ['1', '2', '3']   ← very useful trick
```

---

## 📌 math Module (jab built-ins kam padein)

```python
import math

math.floor(3.9)   # → 3    round down
math.ceil(3.1)    # → 4    round up
math.sqrt(25)     # → 5.0  square root (returns float)
math.factorial(5) # → 120
math.gcd(12, 8)   # → 4    GCD of two numbers
math.pi           # → 3.141592653589793
math.inf          # → infinity  (DSA mein use hota hai min tracking ke liye)
```

> `math.inf` kab use hota hai DSA mein:
>
> ```python
> min_val = math.inf
> for num in [5, 3, 8, 1]:
>     if num < min_val:
>         min_val = num
> # → 1
> ```

---

## 📌 Modulo `%` — DSA ka sabse kaam aane wala operator

```python
10 % 3   # → 1   (10 = 3×3 + 1, remainder is 1)
9  % 3   # → 0   (perfectly divisible → remainder 0)
```

> **Common DSA uses:**
>
> ```python
> # Even/Odd check
> n % 2 == 0   # True → even
> n % 2 != 0   # True → odd
>
> # Divisibility check
> n % 5 == 0   # True → divisible by 5
>
> # Last digit of a number
> 12345 % 10   # → 5
>
> # Remove last digit
> 12345 // 10  # → 1234
>
> # Circular index (array mein wrap-around)
> index = (index + 1) % n
> ```

---

## 📌 Integer ↔ Digits (DSA mein bahut use hota hai)

```python
n = 12345

# Last digit
n % 10        # → 5

# Remove last digit  
n // 10       # → 1234

# Number of digits
len(str(n))   # → 5   (easiest way)

# Loop through each digit
while n > 0:
    digit = n % 10    # last digit
    n = n // 10       # remove last digit

# All digits as list
digits = [int(d) for d in str(12345)]   # → [1, 2, 3, 4, 5]
```

---

## 📌 Float Precision — ek important gotcha

```python
print(0.1 + 0.2)          # → 0.30000000000000004  ⚠️ not 0.3!

# Fix karne ke liye:
round(0.1 + 0.2, 2)       # → 0.3
```

> **Why?** Floats binary mein exactly represent nahi hote.  
> DSA mein mostly integers use hote hain, toh ye usually problem nahi banta.  
> Finance/Backend mein `decimal` module use karte hain.

---

## 📌 Quick Reference

```
TYPES           : int (whole), float (decimal)
ARITHMETIC      : +  -  *  /  //  **  %
SHORTHAND       : +=  -=  *=  /=  **=  %=
COMPARISON      : >  <  >=  <=  ==  !=

BUILT-INS       : abs()  round()  pow()  min()  max()  sum()
CONVERSION      : int()  float()  str()
MATH MODULE     : math.sqrt()  math.floor()  math.ceil()  math.gcd()  math.inf

MODULO TRICKS   : n%2 → even/odd | n%10 → last digit | n//10 → remove last digit
```

---

## 🎯 DSA Section — Number Problems mein ye yaad rakho

| Problem type | Use karo |
|---|---|
| Even / Odd | `n % 2 == 0` |
| Divisibility | `n % k == 0` |
| Last digit | `n % 10` |
| Digits iterate karna | `while n > 0: d = n%10; n //= 10` |
| Power calculate | `**` ya `pow(base, exp, mod)` |
| Infinity initialize | `math.inf` ya `float('inf')` |
| Square root | `math.sqrt(n)` ya `n ** 0.5` |
| GCD | `math.gcd(a, b)` |

---

---

## 🛠️ Dev Section — Backend / Django / FastAPI / AI-ML

> **Abhi ignore kar sakta hai — 3-5 days baad kaam aayega**

### Django / FastAPI mein int & float kahan aata hai

```python
# 1. URL parameters — string aati hai, int mein convert karna padta hai
# FastAPI (automatic conversion kar deta hai)
@app.get("/users/{user_id}")
def get_user(user_id: int):   # FastAPI auto int() karta hai
    ...

# Django (manually karna padta hai)
user_id = int(request.GET.get('id', 0))

# 2. Pagination — page number, items per page
page     = int(request.GET.get('page', 1))
per_page = 10
offset   = (page - 1) * per_page   # modulo/floor division use hota hai

# 3. Price / Amount fields
price = round(float(request.data['price']), 2)  # 2 decimal places
```

### AI/ML mein int & float

```python
# Numpy arrays mein dtype specify karna
import numpy as np
arr = np.array([1, 2, 3], dtype=float)   # int → float conversion

# Normalization (0 to 1 range mein laana)
pixel = 255
normalized = pixel / 255.0   # → 1.0

# Learning rate, thresholds — float constants
learning_rate = 0.001
threshold     = 0.5

if probability > threshold:
    print("Positive")
```

### `decimal` module — Finance/Backend mein float ke badle use karo

```python
from decimal import Decimal

# Float precision problem:
0.1 + 0.2              # → 0.30000000000000004  ❌

# Decimal se fix:
Decimal('0.1') + Decimal('0.2')   # → 0.3  ✅

# Django models mein price store karna
# models.py
price = models.DecimalField(max_digits=10, decimal_places=2)
```

---

*Source: Corey Schafer Python Tutorial #3 | Extended for DSA + Backend/AI-ML*
