# 1
import random
print(f"Random Number Between 10 And 50 => {random.randint(10,50)}")
print(f"Random Number Between 2 And 10 => {random.randrange(2,11,2)}")
print(f"Random Number Between 1 And 9 => {random.randrange(1,10,2)}")
print(dir(random))

print('-' *120)

# 2
#Solution at main.py and my_mode.py
import my_mod
print(my_mod.say_hello('Mohamed'))
print(my_mod.say_welcome('Mohamed'))

print('-' *120)

# 3
from my_mod import say_welcome as new_welcome
print(new_welcome('Mohamed'))

print("-" * 100)

# 4
from my_mod import say_hello 

