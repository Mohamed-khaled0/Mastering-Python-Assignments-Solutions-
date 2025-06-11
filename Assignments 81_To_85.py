# 1
def reverse_string(my_string):  #Decorator
 for char in reversed(my_string):
        yield char
       
# Reverse The String
for c in reverse_string("Elzero"):
  print(c)

print('-' *120)

# 2



def myDecorator(func):
    def wrapper():
      print("Sugar Added From Decorators")
      func()
      print("#" *50)
    return wrapper

@myDecorator
def make_tea():
  print("Tea Created")
  
@myDecorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()
