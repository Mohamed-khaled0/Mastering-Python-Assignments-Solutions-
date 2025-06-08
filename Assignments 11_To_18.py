# 1
myName = 'Mohamed'
myAge = '24'
myCountry = 'Egypt'

print("Hello " + "'" + myName + "'" + " , How You Doing \\ \"\"\" Your Age Is " + myAge + "Your Country Is: " + myCountry)
print("-----------------------------------------------------------")

# 2
print("Hello " + "'" + myName + "'" + " , How You Doing \\ \n \"\"\"  + Your Age Is " + myAge + " + \n And Your Country Is: " + myCountry)
print("-----------------------------------------------------------")

# 3
# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
name = 'Elzero'

print(name[1])
print(name[2])
print(name[-1])
print("-----------------------------------------------------------")

# 4
# Needed Output
# "lze"
# "Ezr"
# "rzE"
name = 'Elzero'

print(name[1:4])
print(name[::2])
print(name[-2] + name[-4] + name[-6])
print("-----------------------------------------------------------")

# 5
name = "#@#@Elzero#@#@"
# Needed Output
# Elzero

print(name.strip("#@"))
print("-----------------------------------------------------------")

# 6
num = "9"
num = "15"
num = "130"
num = "950"
num = "1500"

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500
numbers = ["9", "15", "130", "950", "1500"]

for num in numbers:
    if len(num) <= 4:
        print(num.zfill(4))

print("-----------------------------------------------------------")

# 7
name_one = "Osama"
name_two = "Osama_Elzero"

# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
print("-----------------------------------------------------------")

# 8
name_one = "OSamA"
name_two = "osaMA"

# Needed Output
# osAMa
# OSAma

print(name_one.swapcase())
print(name_two.swapcase())
print("-----------------------------------------------------------")

# 9
msg = "I Love Python And Although Love Elzero Web School"

# Needed Output
# 2

print(msg.count("Love"))
print("-----------------------------------------------------------")

# 10
name = "Elzero"

print(name.index("z"))
print("-----------------------------------------------------------")

# 11
msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although <3 Elzero Web School

print(msg.replace("<3", "Love", 1))
print("-----------------------------------------------------------")

# 12
msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although Love Elzero Web School

print(msg.replace("<3", "Love", 2))
print("-----------------------------------------------------------")

# 13
name = "Mohamed"
age = 24
country = "Egypt"

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
