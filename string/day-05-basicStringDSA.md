# Day 5 — Strings I (Two Pointer Problems)

> Topic: Reverse String, Palindrome Check, Count Vowels/Consonants, Character Frequency

---

## Q1 — Reverse a String

**Problem:** Given a string S, reverse it using the two-pointer approach.

```python
def reverse_string(s):
    chars = list(s)
    l = 0
    r = len(s) - 1
    while l < r:
        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r -= 1
    return "".join(chars)

S = input()
print(reverse_string(S))
```

**Key Learnings:**
- Strings are immutable in Python → convert to `list` first
- Use `chars[l], chars[r] = chars[r], chars[l]` for swapping (no `swap()` function in Python)
- `"".join(chars)` joins list back into string with no separator

---

## Q2 — Palindrome Check

**Problem:** Given a string S, check whether it is a palindrome or not.

```python
def is_palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

S = input()
if is_palindrome(S):
    print("YES")
else:
    print("NO")
```

**Key Learnings:**
- No need to reverse — just compare characters from both ends
- If any mismatch → return `False` immediately
- If loop completes → return `True`

---

## Q3 — Count Vowels & Consonants

**Problem:** Given a string S, count the number of vowels and consonants.

```python
def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for i in s:
        if i in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)

S = input()
count_vowels_consonants(S)
```

**Key Learnings:**
- `if ch in 'aeiou'` is cleaner than writing all 5 conditions with `or`
- `in` keyword works for strings, lists, and dictionaries
- Use `else` to count consonants, not a separate `if`

---

## Q4 — Character Frequency

**Problem:** Given a string S, print the frequency of each character.

```python
def char_frequency(s):
    freq = {}
    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i], 0) + 1
    for key in freq:
        print(key + ":", freq[key])

S = input()
char_frequency(S)
```

**Key Learnings:**
- Use a dictionary `{}` to store character counts
- `freq.get(key, 0)` returns 0 if key doesn't exist yet
- `for i in s` → `i` is the **character**
- `for i in range(len(s))` → `i` is the **index**, use `s[i]`

---

## 🧠 Syntax Cheatsheet — Day 5

```python
# Swap two elements in a list
a, b = b, a

# Join list to string
"".join(['h','e','l','l','o'])   # → "hello"

# Check character in string
if ch in 'aeiou': ...

# Dictionary get with default
freq.get(key, 0)

# Loop by character vs index
for ch in s:              # ch is the character
for i in range(len(s)):   # i is the index → use s[i]

# in keyword works everywhere
if x in 'aeiou': ...      # string
if x in [1,2,3]: ...      # list
if x in dict: ...         # dictionary
```

---

*Day 5 Complete ✅*