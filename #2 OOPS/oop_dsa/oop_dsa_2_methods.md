# 🐍 OOP — Part 2: Methods, @classmethod, @staticmethod & Decorators

> **Source:** Corey Schafer OOP #3 + Apna College  
> **Focus:** DSA perspective only

---

## 📌 Teen Types ke Methods — Summary pehle

```
Instance Method   → self leta hai  → object ka data use/change karta hai
@classmethod      → cls leta hai   → class ka data use/change karta hai
@staticmethod     → kuch nahi leta → related utility function, class se independent
```

> **Simple analogy — School ke example se:**
>
> - Instance method → "Karan ka naam badlo" — specific student pe kaam
> - @classmethod → "School ka naam badlo" — poori school pe kaam  
> - @staticmethod → "Do numbers add karo" — school se koi lena dena nahi, bas kaam ka function

---

## 📌 1. Instance Method — sabse common

```python
class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    # Instance method — self leta hai, object ka data use karta hai
    def welcome(self):
        print(f"Welcome, {self.name}!")

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Karan", [80, 90, 100])
s1.welcome()          # → Welcome, Karan!
print(s1.average())   # → 90.0
```

---

## 📌 2. @classmethod — class ka data change karna ho

```python
class Student:
    school_name = "Delhi School"   # class attribute

    def __init__(self, name):
        self.name = name

    # Normal method — object ka naam change karta hai
    def change_my_name(self, new_name):
        self.name = new_name

    # @classmethod — school ka naam change karta hai (sabke liye)
    @classmethod
    def change_school(cls, new_school_name):
        cls.school_name = new_school_name   # cls = class khud

s1 = Student("Akash")
s2 = Student("Prakash")

s1.change_my_name("Akash Kumar")   # sirf s1 ka naam badla
Student.change_school("Gyan School")  # sabka school badla

print(s1.name)          # → "Akash Kumar"
print(s2.name)          # → "Prakash"
print(Student.school_name)  # → "Gyan School"
print(s1.school_name)       # → "Gyan School"
print(s2.school_name)       # → "Gyan School"
```

> **`cls` kya hai?**  
> Wahi jo `self` instance ke liye hota hai — `cls` class ke liye hota hai  
> `cls.school_name` matlab class ka school_name change karo

### @classmethod as Factory Method — string se object banana

> **Simple analogy:**  
> Factory mein raw material aata hai (string "Rohan-45000")  
> Factory process karta hai  
> Taiyaar product nikalta hai (Employee object)  
> Ye kaam @classmethod karta hai

```python
class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    # Standard way
    @classmethod
    def from_string(cls, emp_data):
        name, salary = emp_data.split('-')     # "Rohan-45000" → ["Rohan", "45000"]
        return cls(name, int(salary))          # cls() = Employee() — naya object bana ke return

# Tere notes ka Question 3 — Factory Method
emp1 = Employee.from_string("Rohan-45000")
print(emp1.name)    # → "Rohan"
print(emp1.salary)  # → 45000
```

> **`cls(name, int(salary))` kya karta hai?**  
> `cls` = `Employee` class hi hai  
> `cls(name, salary)` = `Employee(name, salary)` — naya object bana ke return karta hai

---

## 📌 3. @staticmethod — utility function, class se independent

```python
class Student:
    @staticmethod
    def add_num(a, b):
        return a + b

# Call — object banana zaroori nahi, seedha class se
print(Student.add_num(3, 5))   # → 8

# Object se bhi call kar sakte ho (but usually class se karte hain)
s1 = Student()
print(s1.add_num(3, 5))        # → 8
```

> **Kab use karein @staticmethod?**  
> Jab method class ya object ke data pe depend na kare — sirf ek utility function ho  
> Tere notes ka HotelRoom example:

```python
class HotelRoom:
    def __init__(self, room_no, is_booked=False):   # default=False ← tere notes mein mistake thi
        self.room_no   = room_no
        self.is_booked = is_booked

    def book_room(self):
        if self.is_booked:                 # ← shortcut: if True check
            print("Already Occupied")
        else:
            self.is_booked = True          # ← = nahi == ← tere notes mein mistake thi
            print(f"Room {self.room_no} booked!")

    @staticmethod
    def clean_price(raw_price):            # room ke data se koi lena dena nahi
        return int(raw_price.replace("$", ""))

room1 = HotelRoom(301)
room1.book_room()    # → Room 301 booked!
room1.book_room()    # → Already Occupied

price = HotelRoom.clean_price("$500")
print(price)         # → 500
```

---

## 📌 Teen methods ka farak — ek jagah

```python
class Student:
    school_name = "Delhi School"

    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def show(self):                        # Instance method
        print(self.name, self.marks)       # self — object ka data

    @classmethod
    def change_school(cls, new_name):      # Class method
        cls.school_name = new_name         # cls — class ka data

    @staticmethod
    def add(a, b):                         # Static method
        return a + b                       # na self na cls — independent

s1 = Student("Karan", [80, 90])

s1.show()                          # Instance — object se call
Student.change_school("New School")  # Classmethod — class se call
Student.add(3, 4)                  # Staticmethod — class se call
```

---

## 📌 Decorators — simple explanation

> **Tera confusion:** "decorator kya hota hai?"  
>
> **Simple analogy:**  
> Tu ek plain burger bana raha hai.  
> Decorator = cheese add karne wala wrapper  
> Burger same rehta hai, bas extra feature aa jaati hai  
>
> Decorator = ek function jo doosre function ko wrap karta hai aur extra feature add karta hai

```python
# Simple decorator — step by step

# Step 1: Ek normal function
def my_decorator(func):          # func = jo function wrap karna hai
    def wrapper():
        print("Kuch extra kaam pehle")
        func()                   # original function call karo
        print("Kuch extra kaam baad mein")
    return wrapper               # wrapper return karo

# Step 2: Decorator use karna
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)   # wrap kar diya

say_hello()
# → Kuch extra kaam pehle
# → Hello!
# → Kuch extra kaam baad mein

# Shortcut — @ syntax (same kaam, clean way)
@my_decorator
def say_hello():
    print("Hello!")

say_hello()   # same output
```

> **DSA/Interview ke liye kitna zaroori hai?**  
> Decorators ka FEEL aana chahiye — kya karte hain ye samajh aana chahiye  
> Deep implementation DSA mein nahi chahiye  
> `@classmethod`, `@staticmethod`, `@property` — ye teen yaad rakho, ye sab jagah aate hain

---

## 📌 Closures — ek line mein

> **Tera confusion:** "feel nahi aaya"  
>
> **Simple explanation:**  
> Inner function outer function ke variables yaad rakhta hai — even after outer function khatam ho jaaye  
>
> ```python
> def outer():
>     message = "Hello"        # outer ka variable
>     def inner():
>         print(message)       # inner yaad rakhta hai 'message' ko
>     return inner
>
> func = outer()   # outer khatam ho gaya
> func()           # → "Hello"  ← inner ne message yaad rakha!
> ```
>
> **DSA mein directly use nahi hota** — bas itna samajh lo ki decorator ke andar ye concept kaam karta hai

---

## 🎯 DSA Section — Methods ka use

### @staticmethod DSA mein — utility functions

```python
class Solution:
    # LeetCode style — static method as helper
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def count_primes(self, nums):
        count = 0
        for n in nums:
            if self.is_prime(n):   # helper call
                count += 1
        return count
```

### @classmethod DSA mein — factory pattern

```python
# Graph Node factory method
class GraphNode:
    def __init__(self, val, neighbors=None):
        self.val       = val
        self.neighbors = neighbors if neighbors else []

    @classmethod
    def from_list(cls, val, neighbor_list):
        node = cls(val)
        node.neighbors = neighbor_list
        return node

node = GraphNode.from_list(1, [2, 3, 4])
```

### Tere noted mistakes — summary

```python
# ❌ Mistake 1: is_booked default galat
def __init__(self, room_no, is_booked=False):   # ✅ aise hota hai default
# ❌ def __init__(self, room_no, is_booked(default: False)):  # GALAT syntax

# ❌ Mistake 2: == vs =
self.is_booked == True   # ❌ ye comparison hai, kuch change nahi hoga
self.is_booked = True    # ✅ ye assignment hai

# ❌ Mistake 3: @classmethod se price clean karna galat tha
# clean_price ka room ke data se koi lena dena nahi → @staticmethod use karo
```

---

## 📌 Quick Reference

```
INSTANCE METHOD  : def method(self):         → object data use karna
@classmethod     : def method(cls):          → class data use/change karna
@staticmethod    : def method(a, b):         → independent utility function

CALL:
instance method  : obj.method()
classmethod      : ClassName.method() ya obj.method()
staticmethod     : ClassName.method() ya obj.method()

FACTORY METHOD   : @classmethod se string/data se naya object banana
                   return cls(args)

DECORATOR        : @something — function ke upar likhte hain
                   extra feature add karta hai bina original change kiye

COMMON MISTAKES  : is_booked=False  ← default aise
                   self.x = value   ← assignment, == nahi
                   @staticmethod    ← class/object data nahi chahiye toh
```

---

*Source: Corey Schafer OOP #3 + Apna College | DSA focus*
