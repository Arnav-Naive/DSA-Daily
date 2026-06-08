# 🐍 OOP — Part 1: Classes, Objects, __init__, Self & Attributes

> __Source:__ Corey Schafer OOP #1, #2 + Apna College  
> __Focus:__ DSA perspective only

---

## 📌 Class kya hota hai? Object kya hota hai?

> __Simple analogy:__  
> Class = Blueprint (naqsha)  
> Object/Instance = Us blueprint se bana actual ghar  
>
> `Employee` class = blueprint  
> `emp_1 = Employee(...)` = us blueprint se bana ek actual object

```python
class Employee:
    pass               # abhi khaali class

emp_1 = Employee()     # object/instance bana
emp_2 = Employee()     # dusra object — dono alag hain memory mein

print(emp_1)           # → <__main__.Employee object at 0x...>
print(type(emp_1))     # → <class '__main__.Employee'>
```

> __Object aur Instance — same cheez hai!__  
> Dono words interchangeable hain. `emp_1` ek instance bhi hai aur object bhi.  
> `Employee` = class (blueprint)  
> `emp_1`, `emp_2` = instances/objects (actual cheezein)

---

## 📌 `__init__` — Constructor

> __Simple analogy:__  
> Jab ghar banta hai toh architect decide karta hai — "har ghar mein 2 kamre, 1 bathroom hoga"  
> `__init__` wahi kaam karta hai — object bante waqt automatically run hota hai aur  
> us object ka data set karta hai.

```python
class Employee:
    def __init__(self, first, last, pay):
        # ye 3 cheezein har Employee object mein store hongi
        self.first = first
        self.last  = last
        self.pay   = pay

emp_1 = Employee('Arnav', 'Gupta', 50000)
emp_2 = Employee('John',  'Doe',   30000)

print(emp_1.first)   # → 'Arnav'
print(emp_2.pay)     # → 30000
```

> __`__init__` ka naam kyu ajeeb hai?__  
> `__` (double underscore = "dunder") matlab Python ka special/built-in method hai.  
> Inhe "magic methods" ya "dunder methods" bolte hain — aage OOP Part 4 mein cover hoga.

---

## 📌 `self` — Tera Sabse Bada Confusion Clear

> __Simple explanation:__  
> `self` = "main khud" — object apne aap ko refer karta hai  
>
> Jab tu likhta hai `emp_1.fullname()`, Python internally ye karta hai:  
> `Employee.fullname(emp_1)` — matlab `emp_1` automatically pehle argument ki jagah chala jaata hai  
> Isliye function mein `self` likhna ZAROORI hai — warna Python ko pata nahi kiska data use kare

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first   # self.first = is object ka first naam
        self.last  = last
        self.pay   = pay

    def fullname(self):               # self zaroori hai ← tere notes mein ye missing tha
        return f'{self.first} {self.last}'

emp_1 = Employee('Arnav', 'Gupta', 50000)
emp_2 = Employee('John',  'Doe',   30000)

# Ye dono same kaam karte hain:
print(emp_1.fullname())            # → 'Arnav Gupta'   (recommended)
print(Employee.fullname(emp_1))    # → 'Arnav Gupta'   (same cheez andar se)
```

> __`self` sirf class ke ANDAR hota hai__  
> Bahar se access karte waqt object ka naam use karo:
>
> ```python
> emp_1.first    # ✅ bahar se aise access karo
> emp_1.self.first  # ❌ GALAT — self bahar nahi hota
> ```

---

## 📌 Instance Attributes vs Class Attributes

> __Simple analogy:__  
> School mein:  
>
> - Har student ka apna `naam` aur `roll_no` hota hai → __Instance Attribute__  
> - Lekin school ka naam sabka ek hi hota hai → __Class Attribute__

```python
class Student:
    college_name = "ABC College"   # Class Attribute — sabke liye EK, memory mein ek baar

    def __init__(self, name, marks):
        self.name  = name    # Instance Attribute — har object ka APNA
        self.marks = marks   # Instance Attribute — har object ka APNA

s1 = Student("Karan",  [80, 90, 100])
s2 = Student("Arnav",  [70, 85, 95])
```

### Access karna

```python
# Class attribute — class se ya object se dono se access kar sakte ho
print(Student.college_name)   # → "ABC College"
print(s1.college_name)        # → "ABC College"  (object se bhi kaam karta hai)

# Instance attribute — sirf object se
print(s1.name)    # → "Karan"
print(s2.name)    # → "Arnav"
```

### Precedence — Instance > Class

```python
class Student:
    college_name = "ABC College"
    name = "anonymous"          # class attribute

    def __init__(self, name, marks):
        self.name = name        # instance attribute — ye class attribute ko OVERRIDE karta hai

s1 = Student("Karan", [80, 90])
print(s1.name)   # → "Karan"   ← instance attribute ki precedence zyada hai
                 #    "anonymous" nahi aayega
```

### Class attribute change karna

```python
class Employee:
    raise_amount = 1.04    # class attribute

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Arnav', 'Gupta', 50000)
emp_2 = Employee('John',  'Doe',   30000)

# Class level pe change — SABKE liye change ho jaayega
Employee.raise_amount = 1.05
print(emp_1.raise_amount)   # → 1.05
print(emp_2.raise_amount)   # → 1.05

# Object level pe change — sirf US object ke liye naya attribute ban jaata hai
emp_1.raise_amount = 1.10
print(emp_1.raise_amount)   # → 1.10  (emp_1 ka apna naya attribute)
print(emp_2.raise_amount)   # → 1.05  (emp_2 wala class wala hi use kar raha hai)
```

---

## 📌 `__dict__` — Object ke andar kya hai dekhna

```python
print(emp_1.__dict__)      # → {'first': 'Arnav', 'last': 'Gupta', 'pay': 50000}
print(Employee.__dict__)   # → class ki saari info (zyada info, usually nahi chahiye)
```

---

## 📌 Class Variable — Counting objects

```python
class Employee:
    num_of_emp  = 0     # class variable — kitne objects bane track karna
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        Employee.num_of_emp += 1   # har object bante waqt count badh jaata hai

print(Employee.num_of_emp)   # → 0

emp_1 = Employee('Arnav', 'Gupta', 50000)
emp_2 = Employee('John',  'Doe',   30000)

print(Employee.num_of_emp)   # → 2
```

---

## 📌 Private Attributes — `__` se hide karna

```python
class Student:
    def __init__(self, acc_no, acc_password):
        self.acc_no       = acc_no          # public — bahar se access ho sakta hai
        self.__acc_password = acc_password  # private — __ lagao aur bahar se nahi access hoga

    def show(self):
        print(self.__acc_password)   # ✅ class ke ANDAR access kar sakte hain

s1 = Student("12345", "myPass123")

print(s1.acc_no)          # ✅ → "12345"
print(s1.__acc_password)  # ❌ AttributeError — bahar se nahi access hoga
s1.show()                 # ✅ → "myPass123"  (andar se access hua)
```

> __Python mein sach mein private nahi hota__ — ye sirf naming convention hai  
> `__name` ko Python internally `_ClassName__name` mein badal deta hai (name mangling)  
> Ye encapsulation ka ek tarika hai — aage Part 4 mein detail mein cover hoga

---

## 📌 `del` — Object ya attribute delete karna

```python
s1 = Student("Karan", [80, 90])

del s1.name   # sirf name attribute delete karo
del s1        # poora object delete karo
```

---

## 🎯 DSA Section — OOP Basics kahan aata hai

### 1. DSA problems mein class use karna — Node (Linked List ke liye)

```python
# Standard way — Node class (Linked List mein use hoga)
class Node:
    def __init__(self, data):
        self.data = data    # actual value
        self.next = None    # agla node ka pointer

node1 = Node(10)
node2 = Node(20)
node1.next = node2   # node1 → node2

print(node1.data)        # → 10
print(node1.next.data)   # → 20
```

### 2. Stack — class se banana

```python
class Stack:
    def __init__(self):
        self.items = []         # instance attribute — har stack ka apna

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(1)
s.push(2)
print(s.pop())       # → 2
print(s.is_empty())  # → False
```

### 3. Common interview mistake — `self` missing

```python
# ❌ GALAT — self nahi diya method mein
class Employee:
    def fullname():          # self missing!
        return self.first    # NameError

# ✅ SAHI
class Employee:
    def fullname(self):      # self hamesha pehla argument
        return self.first
```

---

## 📌 Quick Reference

```
CLASS       : class ClassName:
OBJECT      : obj = ClassName(args)
OBJECT = INSTANCE (same cheez!)

__init__    : constructor — object bante waqt automatically run hota hai
self        : current object ka reference — methods mein hamesha pehla argument

INSTANCE ATTR : self.name = name  → har object ka APNA, __init__ mein define hota hai
CLASS ATTR    : college = "ABC"   → class level pe, SABKE liye common

PRECEDENCE  : instance attribute > class attribute

__dict__    : obj.__dict__  → object ke andar kya hai dekhna
del         : del obj.attr  → attribute delete | del obj → object delete

PRIVATE     : self.__name  → __ lagao → bahar se access nahi hoga
```

---

*Source: Corey Schafer OOP #1, #2 + Apna College | DSA focus*
