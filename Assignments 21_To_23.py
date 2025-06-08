# 1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two

print(friends[0])
print(friends.pop(0))
print(friends[-1])
print(friends.pop(-1))

print("-----------------------------------------------------------")

# 2
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"
print(friends[::2])
print(friends[1::2])

print("-----------------------------------------------------------")

# 3
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"
print(friends[1:4])
print(friends[3:6])

print("4-----------------------------------------------------------")

# 4
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
friends[-2:] = ["Elzero", "Elzero"]
print(friends)
print("-----------------------------------------------------------")

# 5
friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.insert(0,"Hamza")
print(friends)
friends.append("Adham")  # APPEND (Last Element)

print(friends)

print("-----------------------------------------------------------")

# 6
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]
friends.remove("Nasser")
friends.remove("Osama")
print(friends)
# ------------------ 
friends.remove("Salem")
print(friends)


print("-----------------------------------------------------------")

# 7
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)
print("-----------------------------------------------------------")

# 8
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

print("-----------------------------------------------------------")

# 9
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# 6
print(len(friends))

print("-----------------------------------------------------------")

# 10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# Needed Output
# Django
# Web

print(technologies[4][0])
print(technologies[4][-1])

