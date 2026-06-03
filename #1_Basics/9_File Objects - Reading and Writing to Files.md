# 🐍 Python — File I/O

> **Source:** Corey Schafer #11 + Apna College  
> **Focus:** DSA syntax reference only

---

## 📌 File open karna — basic

```python
f = open("demo.txt", "r")   # same folder mein hai toh sirf naam
f = open("C:/path/demo.txt", "r")  # alag location pe hai toh full path

data = f.read()
print(data)

f.close()   # ⚠️ close karna zaroori hai — warna memory leak
```

---

## 📌 Modes

```
'r'   → read only (default)
'w'   → write — TRUNCATE karta hai (pura purana data delete ho jaata hai)
'a'   → append — end mein add karta hai, purana data safe
'x'   → nayi file banao, agar exist karti hai toh error

't'   → text mode (default)
'b'   → binary mode (images, videos ke liye)

# Combine kar sakte ho:
'r+'  → read + write, NO truncate
'w+'  → read + write, TRUNCATE (pura data delete)
'a+'  → read + write, NO truncate, pointer end pe
'rb'  → binary read
```

> **Truncate kya hota hai?**
> Matlab file khulte hi **pura purana content delete** ho jaata hai — blank file ban jaati hai.
> `'w'` mode mein ye automatically hota hai.
> ```
> File before: "Hello World"
> open("file.txt", "w")  →  file ab empty hai ""  ← truncate
> open("file.txt", "a")  →  file same hai "Hello World"  ← no truncate
> ```

---

## 📌 Pointer — cursor visualization

```
File content: "Hello World"
Index:          0123456789...

Shuru mein pointer yahan hota hai:
[ H e l l o   W o r l d ]
  ^
  pointer at 0

f.read(5) ke baad — 5 characters padhe:
[ H e l l o   W o r l d ]
              ^
              pointer at 5

f.read() ab yahan se padhega — "World"
```

```python
f.tell()       # pointer ki current position batata hai
f.seek(0)      # pointer ko wapas start pe le jao
f.seek(5)      # pointer ko index 5 pe le jao
```

---

## 📌 Reading — 4 tarike

```python
# Way 1 — poora file ek saath
data = f.read()          # poora content ek string mein

# Way 2 — n characters padhna
data = f.read(5)         # sirf pehle 5 characters

# Way 3 — ek line at a time
line1 = f.readline()     # pehli line
line2 = f.readline()     # dusri line (pointer aage badh jaata hai)

# Way 4 — saari lines ek list mein
lines = f.readlines()    # → ['line1\n', 'line2\n', 'line3\n']

# Way 5 — loop se (most common, clean)
for line in f:
    print(line, end='')  # end='' isliye kyunki line mein already \n hai
```

---

## 📌 with statement — RECOMMENDED WAY ✅

```python
# Bina with (manually close karna padta hai)
f = open("demo.txt", "r")
data = f.read()
f.close()   # bhool gaye toh problem

# with ke saath (automatically close ho jaata hai) ✅
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
# yahan se bahar nikla toh file automatically close
```

> **Hamesha `with` use karo** — clean, safe, close bhoolne ki problem nahi

---

## 📌 Writing

```python
# Overwrite (truncate) — purana content delete ho jaata hai
with open("demo.txt", "w") as f:
    f.write("I want to learn Python")
    f.write("Then I will move to Django")  # same line pe likhega

# Append — end mein add hoga, purana safe
with open("demo.txt", "a") as f:
    f.write("\nNew line added")
```

> ⚠️ File exist nahi karti? **Dono `'w'` aur `'a'` nayi file bana dete hain**

---

## 📌 File modify karna — proper flow

```python
# Step 1: Read
with open("demo.txt", "r") as f:
    data = f.read()

# Step 2: Modify (memory mein)
new_data = data.replace("Java", "Python")

# Step 3: Write back
with open("demo.txt", "w") as f:
    f.write(new_data)
```

---

## 📌 File delete karna

```python
import os
os.remove("demo.txt")

# Safe way — pehle check karo exist karti hai ya nahi
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("File not found")
```

---

## 📌 Useful file properties

```python
with open("demo.txt", "r") as f:
    print(f.name)    # → "demo.txt"
    print(f.mode)    # → "r"
```

---

## 📌 Two files simultaneously — read from one, write to another

```python
with open("input.txt", "r") as read_file:
    with open("output.txt", "w") as write_file:
        for line in read_file:
            write_file.write(line)
```

---

## 🎯 DSA Section — File related problems

### Que: Kis line mein "learning" pehli baar aata hai? -1 if not found

```python
# Simple way
def find_word_line(filename, word):
    with open(filename, "r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if word in lines[i]:
            return i + 1      # line number (1 se start)
    return -1

print(find_word_line("demo.txt", "learning"))
```

### Chunk by chunk padhna (badi files ke liye)

```python
# Simple way
with open("demo.txt", "r") as f:
    size = 10
    content = f.read(size)

    while len(content) > 0:
        print(content, end='')
        content = f.read(size)
```

---

## 📌 r+ vs w+ vs a+ — pointer aur truncate

```
MODE  | TRUNCATE? | POINTER START | READ | WRITE
r+    | No        | Beginning     | ✅   | ✅ (overwrites)
w+    | Yes ⚠️    | Beginning     | ✅   | ✅
a+    | No        | End           | ✅   | ✅ (appends)
```

---

## 📌 Quick Reference

```
OPEN        : open("path", "mode")
CLOSE       : f.close()  ← ya with use karo (recommended)
WITH        : with open("file", "r") as f:

READ ALL    : f.read()
READ N      : f.read(5)
READ LINE   : f.readline()
READ LINES  : f.readlines()  → list of lines
LOOP LINES  : for line in f

WRITE       : f.write("text")
POINTER     : f.tell() → position | f.seek(0) → reset

DELETE      : os.remove("file.txt")
CHECK       : os.path.exists("file.txt")

MODES       : r(read) w(write,truncate) a(append) r+(rw) w+(rw,truncate) a+(rw,append)
```

---

*Source: Corey Schafer #11 + Apna College(Shradha Khapra) | DSA focus*