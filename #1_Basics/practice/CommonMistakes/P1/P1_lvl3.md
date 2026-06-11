# Level 3 Notes — Places Where I Got Stuck

## Character Range Using ord()

Normal:

```python
if 'a' <= ch <= 'm':
```

Using ASCII:

```python
if ord('a') <= ord(ch) <= ord('m'):
```

Useful for many string problems.

---

## Quadrants

Quadrants are numbered anti-clockwise.

```text
       y

  II   |   I
       |
-------+------ x
       |
 III   |   IV
```

```python
x == 0 or y == 0
```

separately (point lies on an axis).

---

## Currency Notes Question

Question:

> Can an amount be formed using only ₹2000, ₹500 and ₹100 notes?

Observation:

```python
2000 % 100 == 0
500 % 100 == 0
100 % 100 == 0
```

Therefore:

```python
amount % 100 == 0
```

means possible.

Otherwise not possible.

---

## Perfect Square Logic

Core condition:

```python
i * i == num
```

Perfect square.

```python
i * i > num
```

Not a perfect square.

Example:

```python
16 -> Perfect Square
20 -> Not Perfect Square
```

---

## Perfect Square (Binary Search)

For very large numbers:

```python
left = 1
right = num
```

Check:

```python
mid * mid
```

If too small:

```python
left = mid + 1
```

If too large:

```python
right = mid - 1
```

Time Complexity:

```python
Brute Force -> O(√n)
Binary Search -> O(log n)
```

---
