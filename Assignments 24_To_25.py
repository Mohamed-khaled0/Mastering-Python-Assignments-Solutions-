# 1
myName = "Mohamed",
print(myName[0])
print(type(myName))

print("-----------------------------1------------------------------")

# 2
friends = ("Osama", "Ahmed", "Sayed")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements
friends = ("Osama", "Ahmed", "Sayed")

friends_list = list(friends)
friends_list[0] = "Elzero"

friends = tuple(friends_list)
print(friends)
print(type(friends))
print(f"{len(friends)}  Elements")

print("-----------------------------2------------------------------")

# 3
nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements

nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(f"{len(nums_and_letters_one)}  Elements")
print("-----------------------------3------------------------------")

# 4
my_tuple = (1, 2, 3, 4)

# Needed Output

# 1
# 2
# 4

a,b,_,c = my_tuple
print(a)
print(b)
print(c)
