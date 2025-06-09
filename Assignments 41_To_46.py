# 1

# Inputs

num1 = int(input('add your num1:').strip())
operation = (input('add your operation sign:')).strip()
num2 = int(input('add your num1:').strip())

#operation = "+" Or "-" Or "*" Or "/" Or "%"

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800

if operation == "+" :
    print (f"{num1 + num2} ")
elif operation == "*" :
    print (f"{num1 * num2} ")
elif operation == "/" :
    print (f"{num1 / num2} ")
elif operation == "%" :
    print (f" {num1 % num2} ")


print("-" * 100)



# 2

age = 17

# Needed Output

"App Is Suitable For You" # If Age Larger Than 6
"App Is Not Suitable For You" # if Age Smaller Than 16

print("App Is Suitable For You" if age>6 else  "App Is Not Suitable For You")



print("-" * 100)



# 3


# Input Example 38

# Needed Output
"Your Age In Months Is 456 Months" # Months Example
"Your Age In Weeks Is 1824 Weeks" # Weeks Example

age = int(input('Add your Age :'))
if age>10 and age<100 :
    print(f"Your Age In Months Is {age *12} Months. \nYour Age In Weeks Is {age *12 *7} Weeks ")
else :
    print('Your Age is Out of range')


print("-" * 100)



# 4

# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country : ").capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

# Needed Output
"Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
"Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example


if country in countries :
    print(f"Your Country Eligible For Discount And The Price After Discount Is {price - discount}")
else :
    print(f"Your Country Eligible For Discount And The Price Is {price }")


