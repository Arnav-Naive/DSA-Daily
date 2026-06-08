
# # guessing game
# import random

# target = random.randint(1, 10)


# while True:
#     choice = int(input("Ente your no. : ")) 
#     if choice == target:
#         print(f"Correct the no. was {target}")
#         break
#     if choice > target:
#         print("Guess lower..")
#     else:
#         print("Guess higher..")
        
# ____________________________________________________________________________________________
# ____________________________________________________________________________________________
#Random password generator

import random
import string

# pass_len = 12
# char = string.ascii_letters + string.digits + string.punctuation

# password = ""

# for i in range(int(pass_len)):
#     password += random.choice(char)

# print(password)
# _________________________________________________
### List comprehension [function for i in range(n)]

pass_len = 12
char = string.ascii_letters + string.digits + string.punctuation

password = [random.choice(char) for i in range(0,pass_len)]
print("".join(password))