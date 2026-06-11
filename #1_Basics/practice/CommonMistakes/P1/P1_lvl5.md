# 🔴 Level 5: Creative / Tricky Logical Scenarios

---

## 4. Take time (hours and minutes) and print the smaller angle between the hour and minute hands

### Formula

[
\text{Angle} = \frac{1}{2}\left|60 \times \text{hr} - 11 \times \text{min}\right|
]

If the angle is greater than 180°, then:

[
\text{Smaller Angle} = 360 - \text{Angle}
]

### Code

```python
hr = 9
min = 35

angle = abs((60 * hr) - (11 * min)) / 2

if angle > 180:
    angle = 360 - angle

print(angle)
```

---

## 5. Take three numbers and check if they are in Arithmetic Progression (AP)

### Concept

A sequence is in AP if the difference between consecutive terms remains constant.

### Example

```text
2, 4, 6, 8, 10
```

Differences:

```text
4 - 2 = 2
6 - 4 = 2
8 - 6 = 2
10 - 8 = 2
```

AP ✅

### Key Condition

```python
b - a == c - b
```

For a list:

```python
nums[i] - nums[i-1] == constant_difference
```

### Quick Note

```text
AP → Same Difference
```

---

## 6. Take three numbers and check if they are in Geometric Progression (GP)

### Concept

A sequence is in GP if the ratio between consecutive terms remains constant.

### Example

```text
2, 4, 8, 16
```

Ratios:

```text
4 / 2 = 2
8 / 4 = 2
16 / 8 = 2
```

GP ✅

### Key Condition

Instead of division:

```python
b * b == a * c
```

For a list:

```python
nums[i] ** 2 == nums[i-1] * nums[i+1]
```

### Quick Note

```text
GP → Same Ratio
```

---

## 10. Take a year and print the corresponding century

### Formula

```python
century = (year - 1) // 100 + 1
```

### Why?

```text
1 - 100      → 1st Century
101 - 200    → 2nd Century
1901 - 2000  → 20th Century
2001 - 2100  → 21st Century
```

The `-1` correctly handles boundary years such as 2000.

### Code

```python
year = 2025

century = (year - 1) // 100 + 1

print(f"{century}th century")
```

### Examples

```text
1900 → 19th Century
1901 → 20th Century
2000 → 20th Century
2001 → 21st Century
2025 → 21st Century
```
