# 🐍 OOP — Part 4: 4 Pillars + Dunder/Magic Methods

> **Source:** Corey Schafer OOP #5 + Apna College  
> **Focus:** DSA perspective only

---

## 📌 Pillar 1 — Encapsulation

Socho — ATM machine hai.  
Tu balance dekhta hai, paisa nikalta hai.  
Lekin andar ka circuit, wiring, code — kuch nahi dikhta tujhe.  
Jo zaroori hai wahi show hota hai, baaki sab andar band hai.

```python
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no      = acc_no       # public — dikha sakte hain
        self.__balance   = balance      # private — __ lagaya, bahar se nahi dikhega

    def deposit(self, amount):          # controlled access
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):         # controlled access
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):              # sirf read karne do, directly change mat karne do
        return self.__balance

acc = BankAccount("12345", 10000)

acc.deposit(5000)
acc.withdraw(2000)
print(acc.get_balance())   # → 13000

print(acc.__balance)       # ❌ AttributeError — bahar se direct access nahi
```

> **Definition:**  
> Encapsulation = data (attributes) aur methods ko ek unit (class) mein band karna  
> aur sensitive data ko private rakhna taaki bahar se directly change na ho sake.

---

## 📌 Pillar 2 — Abstraction

Socho — tu car chalata hai.  
Accelerator dabao — speed badhti hai.  
Andar engine kaise kaam karta hai? Fuel injection kaise hoti hai? Tujhe pata nahi — aur jaanna bhi nahi chahiye.  
Sirf zaroori controls dikhte hain — baaki complexity chupi hai.

```python
# Simple example — implementation hide karna
class PaymentSystem:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):                          # user sirf ye call karta hai
        self.__validate()                   # andar kya hota hai — user ko nahi pata
        self.__process_payment()
        self.__send_confirmation()
        print(f"Payment of {self.amount} done!")

    def __validate(self):                   # private — user ko nahi dikhta
        print("Validating...")

    def __process_payment(self):            # private — user ko nahi dikhta
        print("Processing...")

    def __send_confirmation(self):          # private — user ko nahi dikhta
        print("Sending confirmation...")

p = PaymentSystem(500)
p.pay()   # user sirf .pay() jaanta hai — andar kya hota hai nahi jaanta
```

> **Definition:**  
> Abstraction = unnecessary implementation details chupaana, sirf essential  
> features user ko dikhana. User ko KAISE kaam karta hai nahi pata — bas KYA karta hai pata hai.

> **Encapsulation vs Abstraction — fark:**
>
> ```
> Encapsulation → DATA hide karna (private variables)
> Abstraction   → COMPLEXITY hide karna (private methods, implementation)
> Dono saath kaam karte hain
> ```

---

## 📌 Pillar 3 — Inheritance

Pehle se cover hai — File 3 dekho.

```
Parent class → Child class
Child ko parent ka sab kuch milta hai
super() se parent ka constructor call karte hain
```

---

## 📌 Pillar 4 — Polymorphism

Socho — `+` operator.  
`2 + 3` = 5 (numbers add hote hain)  
`"Hello" + " World"` = "Hello World" (strings join hoti hain)  
Same operator `+` — alag alag kaam karta hai context ke hisaab se.  
Ye hai polymorphism.

```python
# Same method naam — alag alag class mein alag kaam
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

# Same function call — alag output
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(animal.speak())   # → Woof! Meow! Quack!
```

> **Definition:**  
> Polymorphism = same naam ka method/operator alag alag class mein alag kaam kare.  
> "Poly" = many, "morph" = forms — ek cheez ke many forms.

---

## 📌 Dunder/Magic Methods — Operators ke andar ka sach

> **Feel pehle:**  
> Tu likhta hai `2 + 3` — simple lagta hai.  
> Python andar se actually ye karta hai: `(2).__add__(3)`  
> Har operator ke peeche ek `__method__` hota hai.  
> Agar tu apni class mein ye methods define kare — tu bhi `+`, `-`, `>` etc. use kar sakta hai!

```python
# Ye sab same hain:
2 + 3          →   (2).__add__(3)
2 - 3          →   (2).__sub__(3)
2 * 3          →   (2).__mul__(3)
2 / 3          →   (2).__truediv__(3)
2 ** 3         →   (2).__pow__(3)
2 // 3         →   (2).__floordiv__(3)
2 % 3          →   (2).__mod__(3)
2 > 3          →   (2).__gt__(3)
2 < 3          →   (2).__lt__(3)
2 == 3         →   (2).__eq__(3)
len([1,2,3])   →   [1,2,3].__len__()
```

---

## 📌 `__repr__` aur `__str__` — Object print karna

> **Tera confusion:** "nahi samjha"
>
> **Feel pehle:**  
> Tu `print(emp_1)` karta hai — `<Employee object at 0x...>` aata hai. Kuch kaam ka nahi.  
> Agar tu chahta hai ki print karo toh kuch meaningful aaye — `__str__` define karo.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    # Bina kuch define kiye
    # print(emp) → <__main__.Employee object at 0x...>  ← useless

    # __repr__ — developer ke liye, debugging ke liye
    # ideally aisa string hona chahiye jisse object recreate ho sake
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    # __str__ — user ke liye, readable format
    def __str__(self):
        return f"{self.first} {self.last} - Rs.{self.pay}"

emp_1 = Employee("Arnav", "Gupta", 50000)

print(repr(emp_1))   # → Employee('Arnav', 'Gupta', 50000)  ← __repr__
print(str(emp_1))    # → Arnav Gupta - Rs.50000              ← __str__
print(emp_1)         # → Arnav Gupta - Rs.50000  (print() __str__ use karta hai)
```

> **Simple rule:**
>
> - `__repr__` → developer/debugging ke liye — object recreate ho sake aisi string
> - `__str__`  → user ke liye — readable, clean output
> - Agar sirf `__repr__` define kiya → `print()` bhi wahi use karega
> - **DSA mein** `__repr__` zyada useful hai debugging ke time

---

## 📌 Operator Overloading — Apni class pe `+`, `>` etc. use karna

> **Tera documented mistake `__gt__`:**
>
> ```python
> # ❌ GALAT — other nahi diya, aur syntax bhi galat tha
> def __gt__(self):
>     if self.price of order1 > self.price of order2:  # ye valid Python nahi hai
>
> # ✅ SAHI — left side = self, right side = other
> def __gt__(self, other):
>     return self.price > other.price
> ```

```python
class Order:
    def __init__(self, item, price):
        self.item  = item
        self.price = price

    # __gt__ → > operator
    def __gt__(self, other):            # self = left side, other = right side
        return self.price > other.price

    # __add__ → + operator
    def __add__(self, other):
        return self.price + other.price

    # __eq__ → == operator
    def __eq__(self, other):
        return self.price == other.price

    # __len__ → len() function
    def __len__(self):
        return len(self.item)

    # __str__ → print()
    def __str__(self):
        return f"{self.item}: Rs.{self.price}"

order1 = Order("Pizza", 500)
order2 = Order("Burger", 300)

print(order1 > order2)     # → True   (__gt__ call hua)
print(order1 + order2)     # → 800    (__add__ call hua)
print(order1 == order2)    # → False  (__eq__ call hua)
print(len(order1))         # → 5      (__len__ call hua — "Pizza" ki length)
print(order1)              # → Pizza: Rs.500  (__str__ call hua)
```

---

## 📌 `__init__` bhi ek Dunder hai

```python
# Ye sab dunders hain jo ab tak use kiye:
__init__    # constructor — object bante waqt
__repr__    # repr(obj) aur debugging
__str__     # print(obj) aur str(obj)
__add__     # obj1 + obj2
__sub__     # obj1 - obj2
__mul__     # obj1 * obj2
__gt__      # obj1 > obj2
__lt__      # obj1 < obj2
__eq__      # obj1 == obj2
__len__     # len(obj)
```

---

## 🎯 DSA Section — Dunder methods kahan aate hain

### 1. Custom sorting — `__lt__` se

```python
class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks   # marks ke basis pe compare

    def __repr__(self):
        return f"{self.name}({self.marks})"

students = [
    Student("Karan", 85),
    Student("Arnav", 92),
    Student("John",  78),
]

students.sort()          # __lt__ use karega sort karne ke liye
print(students)          # → [John(78), Karan(85), Arnav(92)]
```

### 2. `__eq__` — set/dict mein use hota hai

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)   # → True   (__eq__ call hua)
print(p1 == p3)   # → False
```

### 3. `__len__` aur `__repr__` — debugging mein

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def __len__(self):
        return len(self.items)       # len(stack) directly call kar sakte ho

    def __repr__(self):
        return f"Stack({self.items})"  # print(stack) clean output dega

s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(len(s))   # → 3       (__len__)
print(s)        # → Stack([1, 2, 3])  (__repr__)
```

---

## 📌 Quick Reference

```
4 PILLARS:
Encapsulation  → data + methods ek unit mein band, sensitive data private
Abstraction    → complexity hide, sirf essential dikhao
Inheritance    → parent se attributes/methods inherit karo (File 3)
Polymorphism   → same naam, alag kaam — context ke hisaab se

DUNDER METHODS:
__init__    → constructor
__repr__    → developer/debug ke liye string
__str__     → user ke liye readable string
__add__     → + operator
__sub__     → - operator
__mul__     → * operator
__gt__      → > operator  (self=left, other=right)
__lt__      → < operator
__eq__      → == operator
__len__     → len() function

OPERATOR OVERLOADING RULE:
def __gt__(self, other):      ← other ZAROORI hai
    return self.val > other.val

PRINT:
print(obj)     → __str__ use karta hai
repr(obj)      → __repr__ use karta hai
```

---

*Source: Corey Schafer OOP #5 + Apna College | DSA focus*
