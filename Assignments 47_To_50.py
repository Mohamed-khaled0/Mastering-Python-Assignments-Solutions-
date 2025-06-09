# 1

# while True:
    
#         num = int(input("Please enter a number greater than 0: "))
#         if num > 0:
#             break  # Exit the loop if input is valid
#         else:
#             print("Number 0 Is Not Larger Than 0")


# count = 0
# current_num = num - 1 

# print("Counting down:")
# while current_num >= 1:
#     if current_num != 6:
#         print(current_num)
#         count += 1
#     current_num -= 1

# print(f"{count} Numbers Printed Successfully.")

print("-" * 100)



# 2

# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
# ignored_count = 0
# index = 0

# print("Printing friends with capitalized names:")
# while index < len(friends):
#     friend_name = friends[index]
#     # Check if the first character is uppercase
#     if friend_name[0].isupper():
#         print(friend_name)
#     else:
#         ignored_count += 1
#     index += 1 

# print(f"Friends Printed And Ignored Names Count Is {ignored_count}")

# print("-" * 100)



# 3

# Code
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(f"{skills.pop()}")

# Needed Output
# "HTML"
# "CSS"
# "JavaScript"
# "PHP"
# "Python"





print("-" * 100)



# 4


my_friends = []
max_friends_num = 4

while len(my_friends) < max_friends_num:
    friend_name = input(f"Enter friend's name (Names left: {max_friends_num - len(my_friends)}): ").strip()

    # Case 1: Name is entirely in uppercase (e.g., "OSAMA")
    if friend_name.isupper():
        print("Invalid Name")
    # Case 2: Name is entirely in lowercase (e.g., "osama")
    elif friend_name.islower():
        friend_name_capitalized = friend_name.capitalize()
        my_friends.append(friend_name_capitalized)
        print(f"Friend {friend_name_capitalized} Added => 1st Letter Became Capital")
    # Case 3: Name starts with a capital letter (e.g., "Ahmed", "aHMED")
    else:
        # We ensure it's capitalized correctly, in case only the first letter was uppercase
        # and the rest was a mix (e.g., "aHMED" becomes "Ahmed")
        friend_name_corrected = friend_name.capitalize()
        my_friends.append(friend_name_corrected)
        print(f"Friend {friend_name_corrected} Added")

    # Print how many spots are left, only if the list isn't full yet
    if len(my_friends) < max_friends_num:
        print(f"Names Left in List Is {max_friends_num - len(my_friends)}")

print("\nMy Friends List is Full!")
print("Final Friends List:", my_friends)