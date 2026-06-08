# 🐍 OOP — Part 3: Inheritance, super(), MRO, isinstance

> **Source:** Corey Schafer OOP #4 + Apna College  
> **Focus:** DSA perspective only

---

## 📌 Inheritance — Pehle feel lo, definition baad mein

Socho — `Car` class hai. Ab tu `ToyotaCar` banana chahta hai.  
ToyotaCar mein bhi `start()`, `stop()`, `colour` sab kuch hoga jo Car mein hai.  
Kya tu wahi sab dobara likhega? Nahi na — **inherit kar lo Car se!**

```python
class Car:
    colour = "black"

    @staticmethod
    def start():
        print("Engine start...")

    @staticmethod
    def stop():
        print("Engine stop...")

# ToyotaCar ne Car ka sab kuch inherit kar liya
class ToyotaCar(Car):
    def __init__(self, model):
        self.model = model

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

car1.start()          # → Engine start...  (Car se inherit kiya)
car2.stop()           # → Engine stop...   (Car se inherit kiya)
print(car1.colour)    # → black            (Car se inherit kiya)
print(car1.model)     # → Fortuner         (ToyotaCar ka apna)
```

> **Definition:**  
> Inheritance = ek class (child) doosri class (parent) ke attributes aur methods  
> automatically use kar sakti hai — bina dobara likhne ke.  
> Parent = Base Class | Child = Derived Class

---

## 📌 Method Resolution Order (MRO) — Kaun pehle?

Child class mein koi method nahi mila toh Python parent mein dhundta hai.  
Agar child mein same method hai toh **child ki preference** hoti hai.

```python
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def fullname(self):
        return f"{self.first} {self.last}"

# Developer inherits Employee
class Developer(Employee):
    raise_amount = 1.10    # ← Developer ka apna raise_amount (Employee wala override)

dev_1 = Developer("Corey", "Schafer", 50000)

print(dev_1.pay)      # → 50000
dev_1.apply_raise()   # raise_amount = 1.10 use hoga (Developer > Employee)
print(dev_1.pay)      # → 55000

# MRO check karna ho toh:
print(Developer.__mro__)
# → Developer → Employee → object
```

> **Simple rule:** Python pehle Child mein dhundta hai, nahi mila toh Parent mein jaata hai.  
> Yahi hai **Method Resolution Order (MRO)**

---

## 📌 super() — Parent ka constructor call karna

> **Tera confusion:** "feel nahi hua"
>
> **Simple analogy:**  
> Tu naukri join karta hai. Company ka ek common joining form hai (Employee form).  
> Developer ke paas extra field hai — `prog_lang`.  
> Tu pehle common form bharta hai (super()), phir apna extra fill karta hai.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)   # ← Employee ka __init__ call kar diya
        self.prog_lang = prog_lang            # ← apna extra attribute

dev_1 = Developer("Corey", "Schafer", 50000, "Python")

print(dev_1.first)      # → "Corey"    (Employee se aaya)
print(dev_1.pay)        # → 50000      (Employee se aaya)
print(dev_1.prog_lang)  # → "Python"   (Developer ka apna)
```

> **Tere notes ka documented mistake — The super() Chain:**
> ```python
> # ❌ GALAT — parent ke arguments child ke __init__ mein nahi liye
> class Developer(Employee):
>     def __init__(self, name, age):
>         super().__init__(role, department, salary)  # ← ye variables kahan se aaye?? CRASH
>
> # ✅ SAHI — child ke __init__ mein SABKE arguments lao, phir super() mein route karo
> class Developer(Employee):
>     def __init__(self, first, last, pay, prog_lang):   # parent ke + apne dono
>         super().__init__(first, last, pay)              # parent ke route karo
>         self.prog_lang = prog_lang                      # apna set karo
> ```

---

## 📌 Real example — Manager class with employees list

```python
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):  # ← list default None rakhte hain
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())

dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Test",  "Employee", 90000, "Java")

mgr_1 = Manager("Sue", "Smith", 89898, [dev_1])

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()   # → Test Employee
```

---

## 📌 4 Types of Inheritance — Simple examples

### 1. Single Inheritance — ek parent, ek child

```python
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):    # Dog → Animal
    def bark(self):
        print("Woof!")

d = Dog()
d.breathe()   # → Breathing... (Animal se)
d.bark()      # → Woof!
```

### 2. Multilevel Inheritance — chain, dada → baap → beta

```python
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):       # Dog → Animal
    def bark(self):
        print("Woof!")

class GoldenRetriever(Dog):   # GoldenRetriever → Dog → Animal
    def fetch(self):
        print("Fetching!")

g = GoldenRetriever()
g.breathe()   # → Breathing... (Animal se, 2 level upar)
g.bark()      # → Woof!        (Dog se)
g.fetch()     # → Fetching!    (apna)
```

### 3. Hierarchical Inheritance — ek parent, multiple children

```python
class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):     # Car → Vehicle
    def honk(self):
        print("Beep!")

class Bike(Vehicle):    # Bike → Vehicle (alag child, same parent)
    def ring(self):
        print("Ring!")

c = Car()
b = Bike()
c.move()   # → Moving...
b.move()   # → Moving...
```

### 4. Multiple Inheritance — ek child, multiple parents ✅ Python mein SUPPORTED hai

```python
class A:
    def func_a(self):
        print("A")

class B:
    def func_b(self):
        print("B")

class C(A, B):     # C ko dono A aur B se inherit kiya
    def func_c(self):
        print("C")

c1 = C()
c1.func_a()   # → A  (A se)
c1.func_b()   # → B  (B se)
c1.func_c()   # → C  (apna)
```

> **Tere notes mein confusion:** "Multiple inheritance Python mein supported nahi?"  
> Ye GALAT information thi — **Python mein Multiple Inheritance SUPPORTED hai** ✅  
> Java mein nahi hota (diamond problem ki wajah se), Python mein MRO se handle hota hai.

---

## 📌 isinstance() aur issubclass()

```python
dev_1 = Developer("Corey", "Schafer", 50000, "Python")
mgr_1 = Manager("Sue", "Smith", 89898)

# isinstance — object kis class ka instance hai?
print(isinstance(dev_1, Developer))   # → True
print(isinstance(dev_1, Employee))    # → True  (kyunki Developer, Employee ka child hai)
print(isinstance(dev_1, Manager))     # → False

# issubclass — ek class doosri ki subclass hai?
print(issubclass(Developer, Employee))   # → True
print(issubclass(Manager, Employee))     # → True
print(issubclass(Manager, Developer))    # → False
```

> **DSA mein kab aata hai:**  
> Jab check karna ho ki object kisi particular type ka hai ya nahi — type checking mein

---

## 🎯 DSA Section — Inheritance ke patterns

### 1. Linked List Node — inheritance se extend karna

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Doubly Linked List ke liye Node extend karo
class DNode(Node):
    def __init__(self, data):
        super().__init__(data)   # Node ka __init__ call
        self.prev = None         # extra attribute

d = DNode(10)
print(d.data)   # → 10  (Node se inherit)
print(d.prev)   # → None
print(d.next)   # → None
```

### 2. Graph — Base class se inherit karna

```python
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

# Directed graph — same base, thoda extra
class DirectedGraph(Graph):
    def add_edge(self, u, v):           # override kiya — sirf ek direction
        self.adj_list[u].append(v)      # v → u nahi add kiya

# Undirected graph
class UndirectedGraph(Graph):
    def add_edge(self, u, v):           # override kiya — dono directions
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
```

### 3. super() pattern — DSA mein

```python
# Stack jo extra kaam bhi kare
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

# MinStack — normal stack + minimum track karna
class MinStack(Stack):
    def __init__(self):
        super().__init__()         # Stack ka __init__ call
        self.min_items = []        # extra — minimum track karne ke liye

    def push(self, item):
        super().push(item)         # parent ka push bhi call karo
        if not self.min_items or item <= self.min_items[-1]:
            self.min_items.append(item)

    def get_min(self):
        return self.min_items[-1] if self.min_items else None
```

---

## 📌 Quick Reference

```
INHERITANCE     : class Child(Parent):
SUPER           : super().__init__(parent_args)  ← parent ka constructor call karna
MRO             : Child → Parent → object  (is order mein dhundta hai)

TYPES:
Single          : class B(A)
Multilevel      : class C(B) → B(A) → dada chain
Hierarchical    : class B(A), class C(A) — alag children, same parent
Multiple        : class C(A, B) — ek child, multiple parents ✅ Python mein hota hai

isinstance(obj, Class)     → True/False — object us class ka instance hai?
issubclass(Child, Parent)  → True/False — Child us Parent ki subclass hai?

SUPER() RULE    : child ke __init__ mein parent + apne dono arguments lao
                  super().__init__(sirf parent wale args)
                  self.extra = extra_arg
```

---

*Source: Corey Schafer OOP #4 + Apna College | DSA focus*