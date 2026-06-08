# Day 7 — Pattern Printing + Sorting

---

## 🔑 Key Concepts

### i and j in Pattern Printing
- `i` = row number (outer loop)
- `j` = column number (inner loop)
- Row `i` controls **how many** stars/spaces/numbers to print
- Always `print()` at end of each row to move to next line

### print() end parameter
```python
print("*", end=" ")   # stays on same line, space after
print("*", end="")    # stays on same line, nothing after
print()               # moves to next line
```

---

## Q1 — Right Triangle Star Pattern

```
*
* *
* * *
* * * *
* * * * *
```

```python
def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()

N = int(input())
pattern(N)
```

**Logic:** Row `i` has `i+1` stars → `range(i+1)`

---

## Q2 — Inverted Triangle Star Pattern

```
* * * * *
* * * *
* * *
* *
*
```

```python
def pattern(n):
    for i in range(n):
        for j in range(i, n):
            print("*", end=" ")
        print()

N = int(input())
pattern(N)
```

**Logic:** Row `i` starts from `i` → stars decrease as `i` increases → `range(i, n)`

---

## Q3 — Number Pyramid Pattern

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

```python
def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=" ")
        print()

N = int(input())
pattern(N)
```

**Logic:** Same as Q1 but print `j+1` instead of `*` (j starts from 0 so +1 gives 1,2,3...)

---

## Q4 — Bubble Sort

**Concept:** Compare neighbours, swap if left > right. Largest element bubbles to end each pass.

```python
def bubble_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = 0                          # reset j before every pass
        while j < n-i-1:
            if arr[j] > arr[j+1]:      # compare neighbours
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i += 1
    print(*arr)

N = int(input())
arr = list(map(int, input().split()))
bubble_sort(arr)
```

**Key points:**
- Compare `arr[j]` and `arr[j+1]` (neighbours, not `arr[i]` and `arr[j]`)
- Inner loop goes till `n-i-1` (last i elements already sorted)
- Reset `j = 0` at start of every pass (inside outer loop, outside inner loop)

---

## Q5 — Insertion Sort

**Concept:** Like sorting playing cards. Pick current element, shift larger left elements right, insert in correct position.

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]           # pick current element
        j = i - 1              # start comparing from left
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]  # shift right
            j -= 1
        arr[j+1] = key         # place key in correct position
    print(*arr)

N = int(input())
arr = list(map(int, input().split()))
insertion_sort(arr)
```

**Key points:**
- Start outer loop from index 1 (first element is already "sorted")
- `key` = element being inserted
- Shift elements right until correct position found
- Place `key` at `arr[j+1]` after inner loop

---

## Q6 — Pyramid Pattern (Centered)

```
    *
   * *
  * * *
 * * * *
* * * * *
```

```python
def pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")   # spaces → end="" no extra space
        for k in range(i+1):
            print("*", end=" ")  # stars → end=" " space between stars
        print()

N = int(input())
pattern(N)
```

**Logic:**
- `spaces = n-i-1` (decreases as i increases)
- `stars = i+1` (increases as i increases)
- spaces + stars = n always!
- spaces use `end=""`, stars use `end=" "`

---

## 🧠 Sorting Comparison

| Algorithm | Idea | Time Complexity |
|---|---|---|
| Bubble Sort | Swap neighbours repeatedly | O(n²) |
| Insertion Sort | Insert element in correct position | O(n²) |
| Selection Sort | Find minimum, place at front | O(n²) |

---

## 🧠 Pattern Printing Cheatsheet

| What to print | Code |
|---|---|
| spaces (no gap) | `print(" ", end="")` |
| stars (with gap) | `print("*", end=" ")` |
| numbers | `print(j+1, end=" ")` |
| next line | `print()` |
| space separated list | `print(*arr)` |