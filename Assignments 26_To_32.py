# 1
my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
print(unique_list[:4])
print("-" * 100)

# 2
nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

merged = set(list(nums) + list(letters))
print(merged)
print(nums.union(letters))
print(nums | letters)
print("-" * 100)

# 3
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3}
# set()
# {"A", "B"}
print(my_set)
my_set.clear()
print(my_set)
print(my_set.union("BA"))

print("-" * 100)

# 4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Needed Output
#True

print(set_one.issubset(set_two))
print("-" * 100)

# 5
# Create Dictionary Here

# Needed Output

"HTML Progress Is 90%"
"CSS Progress Is 80%"
"Python Progress Is 30%"
"AI Progress Is 20%"

mySkills = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%"
}

print(f"HTML Progress Is {mySkills['HTML']}")
print(f"CSS Progress Is {mySkills['CSS']}")
print(f"Python Progress Is {mySkills['Python']}")

mySkills["AI"] = "20%"
print(f"AI Progress Is {mySkills['AI']}")