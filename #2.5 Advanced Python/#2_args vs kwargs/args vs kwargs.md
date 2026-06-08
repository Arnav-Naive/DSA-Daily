# *args and **kwargs    
- *args -> It accepts any number of positional arguments in the form of tuple
        (  *  ) argument tells pyhton to take any extra positional arguments in the form of tuple in 'args'
        

Example :

def sum_numbers(*args):
    return sum(args)        

print(sum_numbers(1,2,3,4,5))    # Output: 15
print(sum_numbers(1,2,3,4,5,6,7,8,9,10))   # Output: 55 


- **kwargs -> It accepts any number of keyword arguments in the form of dictionary
        * '**kwargs' argument is not compulsory, we can use any other name in place of kwargs but it must be preceded by '**' (better use generic ones i.e kwargs)
        * **kwargs tells python to take any extra keyword arguments in the form of dictionary in '**kwargs'
        
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_info(name="Arnav", age=21, city="Delhi")  # Output: name Arnav age 21 city Delhi 


# What happens if we use both *args and **kwargs in a function?
def example_func(*args, **kwargs):
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

example_func(1, 2, 3, name="Arnav", age=21, city="Delhi")

Output:
Positional arguments (*args): (1, 2, 3)
Keyword arguments (**kwargs): {'name': 'Arnav', 'age': 21, 'city': 'Delhi'}     