# 🐍 Python Strings — Complete Reference

> **Based on:** Corey Schafer - Python Tutorial for Beginners #2  
> **Extended with:** DSA + Backend Dev perspective, all built-ins with examples

---

## 📌 What is a String?

A string is a **sequence of characters** enclosed in single `'...'`, double `"..."`, or triple `'''...''' / """..."""` quotes.

```python
s = 'hello'
s = "hello"
s = '''hello
world'''        # multi-line string
s = """hello
world"""        # also multi-line
```

> **DSA Note:** Strings in Python are **immutable** — you cannot change a character in-place.  
> Every operation returns a **new** string. This matters for time complexity in loops.

```python
s = "hello"
s[0] = 'H'   # ❌ TypeError: 'str' object does not support item assignment
s = 'H' + s[1:]   # ✅ creates a new string → "Hello"
```

---

## 📌 Your Notes (from Corey Schafer)

```python
s = "Hello World"

s.lower()           # → "hello world"
s.upper()           # → "HELLO WORLD"
s.replace('World', 'John')  # → "Hello John"

# f-strings (formatted strings)
greet = 'Hello'
name  = 'John'
print(f'{greet}, {name.upper()}. Welcome!')   # Hello, JOHN. Welcome!

# Explore all string methods
print(dir(name))        # lists all method names
print(help(str))        # full description of ALL string methods
print(help(str.lower))  # description of one specific method
```

---

## 📌 Indexing & Slicing

```python
s = "Hello"
#    01234   (positive index)
#   -5-4-3-2-1  (negative index)

s[0]     # 'H'
s[-1]    # 'o'   (last character)
s[1:4]   # 'ell' (start inclusive, end exclusive)
s[:3]    # 'Hel' (from beginning)
s[2:]    # 'llo' (to end)
s[::-1]  # 'olleH' (reverse the string — very common in DSA!)
s[::2]   # 'Hlo'  (every 2nd character)
```

> **DSA Use:** Reversing a string → `s[::-1]` is O(n) and very clean.

---

## 📌 All String Methods — With Examples

### 🔠 Case Methods

| Method | What it does |
|--------|-------------|
| `s.lower()` | All lowercase |
| `s.upper()` | All uppercase |
| `s.title()` | First letter of each word capitalized |
| `s.capitalize()` | Only first letter of whole string capitalized |
| `s.swapcase()` | Swap upper↔lower |

```python
s = "hello WORLD"

s.lower()       # → "hello world"
s.upper()       # → "HELLO WORLD"
s.title()       # → "Hello World"
s.capitalize()  # → "Hello world"
s.swapcase()    # → "HELLO world"
```

> **DSA Use:** `s.lower()` is used constantly — when comparing strings case-insensitively  
> e.g. check if two strings are anagrams → compare `sorted(s.lower())` == `sorted(t.lower())`

---

### ✂️ Strip Methods (remove whitespace / characters)

| Method | What it does |
|--------|-------------|
| `s.strip()` | Remove spaces from both sides |
| `s.lstrip()` | Remove spaces from left only |
| `s.rstrip()` | Remove spaces from right only |
| `s.strip('x')` | Remove specific character from both sides |

```python
s = "   hello   "
s.strip()    # → "hello"
s.lstrip()   # → "hello   "
s.rstrip()   # → "   hello"

s2 = "***hello***"
s2.strip('*')   # → "hello"
```

> **DSA Use:** Cleaning input strings before processing  
> **Dev Use:** Cleaning user form input, reading lines from files (`line.strip()` removes `\n`)

---

### 🔍 Search & Check Methods

#### `s.find(sub)` — returns index of first occurrence, `-1` if not found

```python
s = "hello world"
s.find('o')       # → 4
s.find('world')   # → 6
s.find('xyz')     # → -1  (not found, no error)
```

#### `s.index(sub)` — same as find, but raises `ValueError` if not found

```python
s = "hello world"
s.index('o')     # → 4
s.index('xyz')   # ❌ ValueError — use find() if you're not sure it exists
```

> **When to use which?**  
> `find()` → when "not found" is a valid case (DSA, parsing)  
> `index()` → when it MUST exist, and you want an error if it doesn't

#### `s.count(sub)` — count how many times a substring appears

```python
s = "banana"
s.count('a')    # → 3
s.count('an')   # → 2
s.count('xyz')  # → 0
```

> **DSA Use:** Count vowels, count specific characters — very common in easy problems

#### `s.startswith(prefix)` and `s.endswith(suffix)`

```python
s = "Hello World"
s.startswith('Hello')   # → True
s.startswith('World')   # → False
s.endswith('World')     # → True
s.endswith('Hello')     # → False

# You can pass a tuple to check multiple options!
s.startswith(('Hello', 'Hi', 'Hey'))   # → True  ← DSA trick
```

---

### ✅ Boolean / Validation Methods

These return `True` or `False`. Used heavily in DSA for checking character types.

| Method | Returns True when... |
|--------|----------------------|
| `s.isalpha()` | ALL characters are letters (a-z, A-Z) |
| `s.isdigit()` | ALL characters are digits (0-9) |
| `s.isalnum()` | ALL characters are letters OR digits |
| `s.isspace()` | ALL characters are whitespace |
| `s.islower()` | ALL letters are lowercase |
| `s.isupper()` | ALL letters are uppercase |
| `s.istitle()` | String is title-cased |

#### `s.isalpha()` — is it purely letters?

```python
"hello".isalpha()     # → True
"hello123".isalpha()  # → False  (has digits)
"hello!".isalpha()    # → False  (has special char)
"".isalpha()          # → False  (empty string)
```

> **DSA Use:** Filtering only letter characters from a string  
> Example — count only alphabetic characters:

```python
s = "h3ll0 w0rld!"
count = sum(1 for c in s if c.isalpha())   # → 7
```

#### `s.isdigit()` — is it purely numbers?

```python
"123".isdigit()     # → True
"12.3".isdigit()    # → False  (dot is not a digit)
"12a".isdigit()     # → False
"-5".isdigit()      # → False  (minus sign is not a digit)
```

> **DSA Use:** Validate if a string represents a number before converting  
> Before doing `int(s)`, check `s.isdigit()` to avoid ValueError

```python
s = "42"
if s.isdigit():
    num = int(s)    # safe conversion
```

#### `s.isalnum()` — letters or digits only?

```python
"hello123".isalnum()   # → True
"hello 123".isalnum()  # → False  (space is not alnum)
"hello!".isalnum()     # → False
```

> **DSA Use:** Check if a string is a valid alphanumeric identifier  
> Also useful in palindrome problems where you ignore spaces/punctuation:

```python
# Palindrome check ignoring non-alnum chars
s = "A man, a plan, a canal: Panama"
filtered = ''.join(c.lower() for c in s if c.isalnum())
# → "amanaplanacanalpanama"
print(filtered == filtered[::-1])  # → True
```

#### `s.isspace()`

```python
"   ".isspace()    # → True
"  a  ".isspace()  # → False
"".isspace()       # → False  (empty is NOT space)
```

---

### 🔗 Split & Join Methods

#### `s.split(separator)` — split string into a list

```python
s = "hello world foo bar"
s.split()          # → ['hello', 'world', 'foo', 'bar']  (splits on whitespace by default)
s.split(' ')       # → ['hello', 'world', 'foo', 'bar']

s2 = "a,b,c,d"
s2.split(',')      # → ['a', 'b', 'c', 'd']

s3 = "one::two::three"
s3.split('::')     # → ['one', 'two', 'three']

# Limit number of splits
"a b c d".split(' ', 2)   # → ['a', 'b', 'c d']  (max 2 splits)
```

> **DSA Use:** Split a sentence into words for word count, anagram check, etc.  
> **Dev Use:** Parsing CSV rows, splitting URL paths, reading config files

#### `'separator'.join(list)` — join a list into a string

```python
words = ['hello', 'world']
' '.join(words)     # → "hello world"
'-'.join(words)     # → "hello-world"
''.join(words)      # → "helloworld"

# DSA: Rebuild a string after modifying a list of chars
chars = ['h', 'e', 'l', 'l', 'o']
''.join(chars)      # → "hello"
```

> **Important:** `join()` is called on the **separator**, not the list.  
> `''.join(list)` is the most common DSA pattern.

```python
# DSA Example: Reverse words in a sentence
s = "the sky is blue"
result = ' '.join(s.split()[::-1])   # → "blue is sky the"
```

---

### 🔄 Replace & Modify Methods

#### `s.replace(old, new, count=-1)`

```python
s = "banana"
s.replace('a', 'o')       # → "bonono"  (replaces ALL)
s.replace('a', 'o', 2)    # → "bonona"  (replaces first 2 only)
s.replace('xyz', 'abc')   # → "banana"  (no match = no change, no error)
```

> **DSA Use:** Remove specific characters from a string:

```python
# Remove all spaces
s = "hello world"
s.replace(' ', '')   # → "helloworld"

# Remove all vowels
s = "hello world"
for v in "aeiou":
    s = s.replace(v, '')
# → "hll wrld"
```

#### `s.zfill(width)` — pad with zeros on the left

```python
"42".zfill(5)     # → "00042"
"hello".zfill(8)  # → "000hello"
```

> **DSA Use:** Binary number formatting, padding IDs

#### `s.center(width, fillchar)`, `s.ljust()`, `s.rjust()`

```python
"hi".center(10)          # → "    hi    "
"hi".center(10, '-')     # → "----hi----"
"hi".ljust(10, '.')      # → "hi........"
"hi".rjust(10, '.')      # → "........hi"
```

> **Dev Use:** Pretty-printing tables, CLI output formatting

---

### 📋 Other Useful Methods

#### `s.strip()` vs `s.split()` — don't confuse them

```python
"  hello  ".strip()   # → "hello"       (removes spaces, returns string)
"hello world".split() # → ['hello', 'world']  (returns a list)
```

#### `s.encode()` — convert string to bytes

```python
"hello".encode()           # → b'hello'
"hello".encode('utf-8')    # → b'hello'
```

> **Dev Use:** Sending data over network, hashing passwords, file I/O

---

## 📌 String Formatting — 3 Ways

```python
name = "John"
age  = 25

# 1. Old style (% formatting) — avoid in modern Python
print("Hello %s, you are %d" % (name, age))

# 2. .format() method
print("Hello {}, you are {}".format(name, age))
print("Hello {0}, you are {1}".format(name, age))
print("Hello {n}, you are {a}".format(n=name, a=age))

# 3. f-strings (Python 3.6+) — RECOMMENDED ✅
print(f"Hello {name}, you are {age}")
print(f"Hello {name.upper()}, you are {age + 1}")   # expressions inside!
print(f"Pi is approximately {3.14159:.2f}")           # format spec: 2 decimal places
```

> **Dev Use:** f-strings are the cleanest and fastest — use them always in modern Python

---

## 📌 len() and in operator

```python
s = "hello"
len(s)           # → 5  (number of characters)

'h' in s         # → True
'z' in s         # → False
'ell' in s       # → True   (works for substrings too!)
'ell' not in s   # → False
```

> **DSA Use:** `len()` for string length (O(1) in Python).  
> `in` operator is O(n) — checks if substring exists.

---

## 📌 Iterating over Strings

```python
s = "hello"

# Loop over characters
for c in s:
    print(c)    # h, e, l, l, o

# Loop with index (useful in DSA)
for i, c in enumerate(s):
    print(i, c)   # 0 h, 1 e, 2 l, 3 l, 4 o

# Using while loop (less common but sometimes needed)
i = 0
while i < len(s):
    print(s[i])
    i += 1
```

---

## 📌 String Multiplication & Concatenation

```python
# Concatenation
"hello" + " " + "world"   # → "hello world"

# Multiplication (repeat)
"ha" * 3    # → "hahaha"
"-" * 20    # → "--------------------"   (useful for dividers)

# ⚠️ Don't concatenate in a loop — use join instead!
# BAD (O(n²) because strings are immutable):
result = ""
for c in "hello":
    result += c   # creates a new string every time

# GOOD (O(n)):
result = ''.join(c for c in "hello")
```

---

## 📌 ord() and chr() — Characters and ASCII

```python
ord('a')    # → 97   (ASCII value of 'a')
ord('A')    # → 65
ord('z')    # → 122
ord('0')    # → 48

chr(97)     # → 'a'
chr(65)     # → 'A'
chr(48)     # → '0'
```

> **DSA Use:** This is VERY important for DSA problems!

```python
# Check if character is lowercase letter
c = 'm'
'a' <= c <= 'z'     # → True

# Convert lowercase to uppercase manually (without .upper())
c = 'm'
chr(ord(c) - 32)    # → 'M'

# Get position of letter in alphabet (a=0, b=1, ...)
c = 'd'
ord(c) - ord('a')   # → 3

# Used in frequency array approach (26 letters):
freq = [0] * 26
s = "banana"
for c in s:
    freq[ord(c) - ord('a')] += 1
# freq[0] = count of 'a', freq[1] = count of 'b', etc.
```

---

## 📌 Common DSA Patterns with Strings

### 1. Count vowels

```python
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

count_vowels("Hello World")   # → 3
```

### 2. Reverse a string

```python
s = "hello"
s[::-1]           # → "olleh"  (slicing — most Pythonic)
''.join(reversed(s))   # → "olleh"  (using reversed())
```

### 3. Check palindrome

```python
def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

is_palindrome("racecar")    # → True
is_palindrome("A man a plan a canal Panama".replace(' ', ''))  # → True
```

### 4. Check anagram

```python
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

is_anagram("listen", "silent")   # → True
is_anagram("hello", "world")     # → False
```

### 5. Count frequency of each character

```python
from collections import Counter
s = "banana"
Counter(s)   # → Counter({'a': 3, 'n': 2, 'b': 1})

# Without Counter (manual way):
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
# → {'b': 1, 'a': 3, 'n': 2}
```

### 6. Remove duplicates (keep order)

```python
s = "banana"
seen = set()
result = ''.join(c for c in s if not (c in seen or seen.add(c)))
# → "ban"
```

### 7. Check if string has all unique characters

```python
def all_unique(s):
    return len(s) == len(set(s))

all_unique("hello")    # → False  ('l' repeats)
all_unique("world")    # → True
```

---

## 📌 Quick Reference Cheat Sheet

```
CREATION        : s = "hello" | s = 'hello' | s = """multi line"""
INDEXING        : s[0] s[-1] s[1:4] s[::-1]
LENGTH          : len(s)
IN OPERATOR     : 'x' in s → True/False

CASE            : .lower() .upper() .title() .capitalize() .swapcase()
STRIP           : .strip() .lstrip() .rstrip() .strip('char')
SEARCH          : .find() → index or -1 | .index() → index or ValueError
COUNT           : .count('x') → int
STARTS/ENDS     : .startswith() .endswith()

BOOLEAN CHECKS  : .isalpha() .isdigit() .isalnum() .isspace() .islower() .isupper()
SPLIT           : .split(sep) → list
JOIN            : sep.join(list) → string
REPLACE         : .replace(old, new)

ASCII           : ord('a') → 97 | chr(97) → 'a'
FORMAT          : f"Hello {name}" ← use this always

EXPLORE         : dir(s) → all methods | help(str.method) → docs
```

---

## 📌 What's Coming Next?

Once you're comfortable with strings, the next topics build directly on this:

- **Lists** — similar indexing/slicing, but **mutable**
- **Dictionaries** — `Counter` (from collections) is basically a dict
- **Sets** — used in uniqueness checks (like `set(s)`)
- **OOP** — strings *are* objects, `.lower()` is a method call on an object

---

*Notes based on Corey Schafer's Python Tutorial #2 | Extended for DSA + Backend Dev*
