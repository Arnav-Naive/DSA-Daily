**Print all numbers that are palindromes between 1–500.**
            def palindrome(num):
                num = str(num)

                i = 0
                j = len(num) - 1

                while i < j:
                    if num[i] != num[j]:
                        return False

                    i += 1
                    j -= 1

                return True


            for i in range(1, 501):
                if palindrome(i):
                    print(i)

---

-

---

**Print all numbers from 1–n whose binary representation has an even number of 1s.**

# Question 6: Print all numbers from `1` to `n` whose binary representation has an even number of `1`s

## What does the question mean?

For every number from `1` to `n`:

1. Convert the number to binary.
2. Count how many `1`s are present.
3. If the count of `1`s is even, print that number.

---

## Example (`n = 10`)

```text
1  -> 1      -> one 1      -> odd    ❌
2  -> 10     -> one 1      -> odd    ❌
3  -> 11     -> two 1s     -> even   ✅
4  -> 100    -> one 1      -> odd    ❌
5  -> 101    -> two 1s     -> even   ✅
6  -> 110    -> two 1s     -> even   ✅
7  -> 111    -> three 1s   -> odd    ❌
8  -> 1000   -> one 1      -> odd    ❌
9  -> 1001   -> two 1s     -> even   ✅
10 -> 1010   -> two 1s     -> even   ✅
```

Output:

```text
3 5 6 9 10
```

---

## Important Note

```python
bin(10)
```

returns:

```text
'0b1010'
```

`bin()` returns a **string**, not an integer.

So this is wrong:

```python
num = bin(num)

while num > 0:
    ...
```

because strings cannot be used with `%` and `//`.

---

## Solution 1 (Recommended)

```python
def count1s(num):
    return bin(num).count('1')


n = 50

for i in range(1, n + 1):
    if count1s(i) % 2 == 0:
        print(i)
```

---

## Solution 2 (Without `.count()`)

```python
def count1s(num):
    b = bin(num)
    count = 0

    for ch in b:
        if ch == '1':
            count += 1

    return count


n = 50

for i in range(1, n + 1):
    x = count1s(i)

    if x % 2 == 0:
        print(i)
```

---

## Concept Learned

```text
bin(num)          -> converts number to binary string
.count('1')       -> counts the number of 1s
Even number of 1s -> count % 2 == 0
```

This idea is called **Parity of Set Bits** and appears later in Bit Manipulation problems.
