# 🐍 OOP — Part 5: @property, Getter, Setter, Deleter

> **Source:** Corey Schafer OOP #6 + Apna College  
> **Focus:** DSA perspective only

---

## 📌 Problem pehle samjho — phir solution

Socho `Employee` class hai:

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last  = last
        self.email = first + '.' + last + '@company.com'

emp_1 = Employee("John", "Smith")

print(emp_1.first)   # → John
print(emp_1.email)   # → John.Smith@company.com

# Ab naam badla
emp_1.first = "Jim"

print(emp_1.first)   # → Jim          ← naam badla ✅
print(emp_1.email)   # → John.Smith@company.com  ← email nahi badla ❌
```

> **Problem:** `first` badla lekin `email` automatically update nahi hua  
> Kyunki `email` `__init__` mein ek baar set hua — phir update nahi hota

---

## 📌 Pehla fix — email ko method banao

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last  = last

    def email(self):                                    # method ban gaya
        return f"{self.first}.{self.last}@company.com"

emp_1 = Employee("John", "Smith")
emp_1.first = "Jim"

print(emp_1.email())   # → Jim.Smith@company.com  ✅  (ab update hoga)
```

> **Naya problem:** Pehle `emp_1.email` tha — ab `emp_1.email()` ho gaya  
> Jo log pehle se is class use kar rahe the — unka code toot jaayega  
> `()` lagana padega — breaking change hai

---

## 📌 Solution — `@property` decorator

> **Feel:**  
> `@property` lagao aur method ko attribute jaisa use kar sakte ho — bina `()` ke!  
> Bahar se dekhne mein attribute lagta hai, andar se method hai.

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last  = last

    @property                                           # ← ye lagaya
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee("John", "Smith")
emp_1.first = "Jim"

print(emp_1.email)      # → Jim.Smith@company.com  ✅  (bina () ke!)
print(emp_1.fullname)   # → Jim Smith              ✅  (bina () ke!)
```

> **Definition:**  
> `@property` decorator ek method ko attribute ki tarah access karne deta hai —  
> bina parentheses `()` ke call kar sakte ho, lekin andar se function hi run hota hai.

---

## 📌 Setter — value set karna bhi chahiye

```python
emp_1.fullname = "Corey Schafer"   # ❌ AttributeError — property set nahi hoti by default
```

> Getter se sirf read kar sakte ho.  
> Agar set bhi karna ho toh `@property_name.setter` define karo.

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last  = last

    @property
    def fullname(self):                          # getter — read karna
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):                    # setter — write karna
        first, last  = name.split(' ')
        self.first   = first
        self.last    = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

emp_1 = Employee("John", "Smith")

# Getter use karna
print(emp_1.fullname)   # → John Smith

# Setter use karna
emp_1.fullname = "Corey Schafer"   # ✅ ab kaam karega

print(emp_1.first)    # → Corey    (setter ne split karke set kiya)
print(emp_1.last)     # → Schafer
print(emp_1.email)    # → Corey.Schafer@company.com
```

---

## 📌 Deleter — delete karna

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last  = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first  = first
        self.last   = last

    @fullname.deleter
    def fullname(self):                          # deleter — delete karna
        print("Deleting fullname...")
        self.first = None
        self.last  = None

emp_1 = Employee("John", "Smith")

del emp_1.fullname       # deleter call hoga

print(emp_1.first)       # → None
print(emp_1.last)        # → None
```

---

## 📌 Teen decorators — ek jagah

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius    # _ ek convention hai — "seedha mat use karo"

    @property
    def celsius(self):             # getter — read
        return self._celsius

    @celsius.setter
    def celsius(self, value):      # setter — write + validation
        if value < -273.15:
            print("Temperature below absolute zero!")
        else:
            self._celsius = value

    @celsius.deleter
    def celsius(self):             # deleter — delete
        print("Deleting temperature...")
        del self._celsius

t = Temperature(25)

print(t.celsius)    # → 25          (getter)
t.celsius = 30      # (setter)
print(t.celsius)    # → 30

t.celsius = -300    # → Temperature below absolute zero! (validation)
print(t.celsius)    # → 30  (change nahi hua)

del t.celsius       # (deleter)
```

> **Definition:**  
> Getter  = `@property`               → sirf read karo  
> Setter  = `@property_name.setter`   → write karo + validation add kar sakte ho  
> Deleter = `@property_name.deleter`  → delete karo  

---

## 📌 `_` vs `__` — naming convention

```python
class Example:
    def __init__(self):
        self.public    = "sabka"       # public — koi restriction nahi
        self._private  = "convention"  # single _ = "seedha use mat karo, private treat karo"
                                       # but bahar se access HO sakta hai (bas convention)
        self.__mangled = "hidden"      # double __ = name mangling, bahar se access nahi
```

> ```
> self.name    → public      — freely use karo
> self._name   → protected   → convention: "direct mat use karo"
> self.__name  → private     → actually hide ho jaata hai
> ```

---

## 🎯 DSA Section — @property kahan aata hai

### 1. Validation ke saath attribute set karna

```python
class Stack:
    def __init__(self, max_size):
        self._items    = []
        self._max_size = max_size

    @property
    def size(self):                        # getter — current size
        return len(self._items)

    @property
    def is_full(self):                     # computed property — calculate karke return
        return len(self._items) >= self._max_size

    @property
    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        if self.is_full:
            print("Stack overflow!")
        else:
            self._items.append(item)

    def pop(self):
        if self.is_empty:
            print("Stack underflow!")
            return None
        return self._items.pop()

s = Stack(3)
s.push(1)
s.push(2)
s.push(3)

print(s.size)       # → 3   (getter, bina ())
print(s.is_full)    # → True
s.push(4)           # → Stack overflow!
```

### 2. Read-only property — sirf read, set nahi kar sakte

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):                         # read-only computed property
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):               # read-only computed property
        return 2 * 3.14159 * self._radius

c = Circle(5)
print(c.radius)          # → 5
print(c.area)            # → 78.53975
print(c.circumference)   # → 31.4159

c.area = 100             # ❌ AttributeError — setter define nahi kiya = read-only
```

---

## 📌 Saare Decorators — ek saath summary

```python
class MyClass:

    @property
    def name(self):           # getter — read karo, bina ()
        return self._name

    @name.setter
    def name(self, value):    # setter — set karo + validation
        self._name = value

    @name.deleter
    def name(self):           # deleter — delete karo
        del self._name

    @classmethod
    def class_method(cls):    # class ka data use karna — cls
        pass

    @staticmethod
    def static_method():      # independent utility — na self na cls
        pass
```

---

## 📌 Quick Reference

```
@property              → method ko attribute jaisa use karo, bina ()
@prop_name.setter      → write + validation
@prop_name.deleter     → delete

NAMING CONVENTION:
self.name    → public    — freely use karo
self._name   → protected — convention, "seedha mat use karo"
self.__name  → private   — actually hide hota hai

GETTER ONLY  → set karne ki koshish → AttributeError
SETTER bhi   → set + get dono kaam karte hain
VALIDATION   → setter mein if/else laga ke invalid values rok sakte hain

ALL DECORATORS:
@property          → getter
@x.setter          → setter
@x.deleter         → deleter
@classmethod       → cls
@staticmethod      → independent
```

---

*Source: Corey Schafer OOP #6 + Apna College | DSA focus*