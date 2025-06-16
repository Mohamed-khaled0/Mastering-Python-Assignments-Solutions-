# 1
# print('Please Enter Only One Character ')
# NUM = input("Add Your Number : ")


# if len(NUM) > 1 :
#     raise IndexError("Only One Character Allowed")
# elif  len(NUM) == 0 :
#     raise ValueError("Number Must Be Larger Than 0")
# elif not NUM.isdigit():
#     raise Exception("Only Numbers Allowed")
# else:
#     print(f" The number is {NUM}")

print('-' * 120)

# 2
# LETTER = input("Add Letter From A to Z :")

# try:
#     if len(LETTER) != 1:
#         raise ValueError("You Must Write One Character Only")
#     if not LETTER.isalpha() or not LETTER.isupper():
#         raise ValueError("The Letter Not In A - Z")

# except ValueError :
#     print(ValueError)
# else :
#     print(f"You Typed {LETTER}")

print('-' * 120)

# 3 - 

def calculate(num1:int, num2:int) -> int :
  return num1 + num2

print(calculate(20, 30))