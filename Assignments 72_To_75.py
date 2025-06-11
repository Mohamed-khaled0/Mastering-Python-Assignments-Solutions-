# 1

from functools import reduce


def remove_chars(name):
    return name[1:-1]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list = map(remove_chars , friends_map)
# Normal Way
for friend in cleaned_list  :
    print(friend)

print('-' *20)
# Using Lambda Function
for friend in map(lambda name:name[1:-1] ,friends_map):
    print(friend)


print('-' *120)
# 2
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# Output
"Wessam"
"Essam"

def get_names(name):
        return name[-1] == "m"

names = filter(get_names,friends_filter)
for name in names :
    print(name)

print('-' *120)

# 3

def multiply(nums):
    result = 1
    for num in nums :
        result *= num
    return result
    
# Solve using Reduce

nums = [2, 4, 6, 2]
print(multiply(nums))

def multiply1(num1 , num2):
    return num1 * num2
    

nums1 = [2, 4, 6, 2]
# ((((2*4) *4 ) *6)*2 )
result = reduce(multiply1 ,nums1)
print(result)
print("-" * 100)

# Using Lambda Function
result1 = reduce(lambda num1,num2: num1*num2 ,nums1)
print(result1)


print("-" * 100)

# 4

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
index = 50
for item in reversed(skills):
    if isinstance(item, str):
        print(f"{index} - {item}")
    index += 1