# 1


def calculate (n1,n2,operation) :
  op = operation.lower()
  if op == "+" or "A" or "a" or "AdD" :
    return(n1+n2)
  elif op == "-" or "S" or "subTRACT" :
    return(n1-n2)
  elif op == "/" or "Multiply" or "m":
    print(n1/n2)
  else :
    return('Invalid  Operation ')

print("-" * 100)



# 2

def addition(*nums):
  result = 0
  for num in nums :
   if num == 10:
    continue
   elif num == 5 :
     result -=5
   else :
     result+=num
  return result


# print(addition(10, 20, 30, 10, 15)) 
# print(addition(10, 20, 30, 10, 15, 5, 100))

print("-" * 100)



# 3

def skills(name,*skills):
  print(f'Hello {name} Your Skills Is')
  for skill in skills :
    return skill
  else:
    print(f"Hello {name} You Have No Skills To Show")

# print(skills('Mohamed','Py','PHP'))



print("-" * 100)



# 4
def say_hello(name ="Unknown" , age ="Unknown", country="Unknown") :
  return (f"Hello {name} Your Age Is {age} And You Live In {country}")

print(say_hello('Mohamed','24','Egypt'))
print(say_hello('Mohamed','24'))