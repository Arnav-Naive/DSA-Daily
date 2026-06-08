# `*args` and `**kwargs`

## `*args` — Variable Positional Arguments

Accepts any number of positional arguments as a **tuple**.  
The `*` tells Python to collect all extra positional arguments into `args`.

```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))           # Output: 15
print(sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Output: 55
```

---

## `**kwargs` — Variable Keyword Arguments

Accepts any number of keyword arguments as a **dictionary**.  
The `**` tells Python to collect all extra keyword arguments into `kwargs`.

> **Note:** `kwargs` is not a reserved name — any name works as long as it's preceded by `**`. But using `kwargs` is the common convention.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_info(name="Arnav", age=21, city="Delhi")
# Output: name Arnav  age 21  city Delhi
```

---

## Using Both Together

```python
def example_func(*args, **kwargs):
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

example_func(1, 2, 3, name="Arnav", age=21, city="Delhi")
```

**Output:**

```
Positional arguments (*args): (1, 2, 3)
Keyword arguments (**kwargs): {'name': 'Arnav', 'age': 21, 'city': 'Delhi'}
```
