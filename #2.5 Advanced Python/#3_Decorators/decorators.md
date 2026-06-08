# Decorators

## What is a Decorator?

A decorator ek function hota hai jo **doosre function ko wrap karta hai** — matlab uske kaam karne se pehle ya baad mein kuch extra kaam kar sakta hai, bina us original function ko touch kiye.

Simple analogy: Socho tumhara function ek plain chai ka cup hai. Decorator us cup ke upar ek fancy wrapper lagata hai — chai wahi rehti hai, bas presentation better ho jaati hai.

---

## Basic Syntax

```python
def my_decorator(base_fn):
    def enhanced_fn(*args, **kwargs):
        # kuch karo pehle
        result = base_fn(*args, **kwargs)   # original function call
        # kuch karo baad mein
        return result
    return enhanced_fn

@my_decorator
def my_function():
    pass
```

> `@my_decorator` likhna exactly yahi hai:
> `my_function = my_decorator(my_function)`

---

## Why `*args` and `**kwargs` in the wrapper?

`enhanced_fn(*args, **kwargs)` isliye use karte hain taaki decorator **kisi bhi function ke saath kaam kare** — chahe uske 0 arguments hon ya 10, positional hon ya keyword.

Agar fixed arguments likhte toh decorator sirf ek specific function ke saath kaam karta.

---

## Real Example: Timer Decorator

Yeh decorator measure karta hai ki koi function kitne time mein complete hota hai.

```python
import time

def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        result = base_fn(*args, **kwargs)   # original function chala do
        end_time = time.time()
        print(f"Task time: {end_time - start_time} seconds")
        return result                        # result wapas karo
    return enhanced_fn


@timer_dec
def brew_tea(tea_type, steep_time):
    print(f"Brewing {tea_type} tea...")
    time.sleep(steep_time)
    print("Tea is ready!")


@timer_dec
def make_matcha():
    print("Making matcha...")
    time.sleep(1)
    print("Matcha is ready!")
    return f"Drink matcha by {datetime.now() + timedelta(minutes=30)}"


brew_tea(tea_type="green", steep_time=1)
print(make_matcha())
```

**Output:**

Brewing green tea...
Tea is ready!
Task time: 1.0003 seconds
Making matcha...
Matcha is ready!
Task time: 1.0003 seconds
Drink matcha by 2025-11-17 16:35:16.28

---

## Important: `return result`

Image 1 mein `return result` **nahi tha** — isliye `make_matcha()` ka return value lost ho jaata.

Image 2 mein `return result` **add kiya** — ab decorator function ka return value bhi preserve karta hai.

> **Rule:** Agar decorated function kuch return karta hai, toh wrapper ke andar `return result` likhna zaroori hai.

---

## Flow Summary

brew_tea("green", 1)
↓
enhanced_fn("green", 1)       ← decorator ka wrapper chala
↓
start_time record karo
↓
base_fn("green", 1)           ← original brew_tea chali
↓
end_time record karo
↓
time print karo
↓
result return karo
