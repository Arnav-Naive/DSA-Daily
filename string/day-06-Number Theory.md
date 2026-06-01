# Day 6 — Number Theory

> Topic: Prime Check, Armstrong, Perfect Number, Factorial, Fibonacci

---

## Q1 — Prime Check

**Problem:** Given a number N, check if it is prime or not.

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())
if is_prime(N):
    print("Prime")
else:
    print("Not Prime")
```

**Key Learnings:**
- A number is prime if nothing from 2 to n-1 divides it
- `n % i == 0` means i divides n
- `range(2, n)` not `range(2, n+1)` — don't include n itself or n%n=0 always

---

## Q2 — Armstrong Number

**Problem:** Given a number N, check if it is an Armstrong number.

```python
def is_armstrong(n):
    x = str(n)
    power = len(x)
    summ = 0
    for d in x:
        summ += int(d) ** power
    if summ == n:
        print("Armstrong")
    else:
        print("Not Armstrong")

N = int(input())
is_armstrong(N)
```

**Key Learnings:**
- `str(n)` converts number to string to loop through digits
- `len(str(n))` gives number of digits
- `int(d) ** power` raises each digit to power of number of digits
- Don't hardcode `** 3` — use `len(x)` so it works for any number

---

## Q3 — Perfect Number

**Problem:** Given a number N, check if it is a Perfect number.

```python
def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        print("Perfect")
    else:
        print("Not Perfect")

N = int(input())
is_perfect(N)
```

**Key Learnings:**
- Sum all divisors of n excluding n itself
- If sum == n → Perfect
- Never use `sum` as variable name — it's a Python built-in

---

## Q4 — Factorial

**Problem:** Given a number N, find its factorial.

```python
# Recursive approach
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Iterative approach
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

N = int(input())
print(factorial(N))
```

**Key Learnings:**
- Recursion always has 2 parts: base case and recursive case
- Base case → when to STOP (if n == 0 or n == 1)
- Without base case → infinite loop crash!
- `result *= i` is same as `result = result * i`

---

## Q5 — Fibonacci

**Problem:** Given a number N, print the first N terms of the Fibonacci series.

```python
# Iterative approach
def fibonacci(n):
    l = []
    for i in range(n):
        if i == 0 or i == 1:
            l.append(i)
        else:
            l.append(l[i-2] + l[i-1])
    print(*l)

# Recursive approach
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

N = int(input())
fibonacci(N)
```

**Key Learnings:**
- Each fibonacci number = sum of previous two
- `l[i-2] + l[i-1]` looks back at previous values in the list
- `print(*l)` prints list space separated
- Recursive fibonacci has 2 base cases: n==0 and n==1

---

## 🧠 Syntax Cheatsheet — Day 6

```python
# Modulus → check divisibility
n % i == 0         # i divides n

# Convert number to string
str(153)           # → "153"

# Number of digits
len(str(153))      # → 3

# Loop through digits
for d in str(n):
    int(d)         # convert each digit back to int

# Power
3 ** 2             # → 9

# Multiply and update
result *= i        # same as result = result * i

# Print list space separated
print(*l)

# Append to list
l.append(value)

# Never use as variable names (Python built-ins)
# sum, list, dict, str, int, len
```

---

## 🧠 Recursion Template — use for any recursive problem

```python
def recursive_function(n):
    # Step 1 — Base case (when to stop)
    if n == 0:
        return ...

    # Step 2 — Recursive case (call itself)
    return recursive_function(n-1)
```

---

*Day 6 Complete ✅*s