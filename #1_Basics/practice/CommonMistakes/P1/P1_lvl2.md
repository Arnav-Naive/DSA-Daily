# Check Character Range

## Using Normal Character Comparison

```python
# Take an alphabet character and check if it lies between
# 'a' and 'm' or 'n' and 'z'

ch = input("Enter char: ")

if ch >= 'a' and ch <= 'm':
    print("lies between a and m")

elif ch >= 'n' and ch <= 'z':
    print("lies between n and z")
```

---

# Using `ord()`

`ord()` converts a character into its ASCII value.

Example:

```python
ord('a')  # 97
ord('b')  # 98
```

## Code Using `ord()`

```python
ch = input("Enter char: ")

if ord(ch) >= ord('a') and ord(ch) <= ord('m'):
    print("lies between a and m")

elif ord(ch) >= ord('n') and ord(ch) <= ord('z'):
    print("lies between n and z")
```

---

# Shorter Python Way

```python
if ord('a') <= ord(ch) <= ord('m'):
```

This chained comparison is common in Python.
