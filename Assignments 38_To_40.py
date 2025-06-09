# 1

# Input
#"     osAmA   "

# Needed Output
#"Hello Osama, Happy To See You Here."

name  = input('Add Your Name :').strip().capitalize()
print(f"Hello {name} , Happy To See You Here.")



print("-" * 100)



# 2

# Inputs
#16 # Input One
#24 # Input Two

# Needed Output
#"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
#"Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+

age = int(input("Please enter your age: "))

message_parts = [
    "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You",
    f"Hello Your Age Is {age}, All Articles Is Suitable For You"
]

print(message_parts[age >= 16])



print("-" * 100)



# 3

# Inputs
#"Osama" # First Name
#"Mohamed" # Second Name

# Needed Output
#"Hello {First_Name} {First_Letter_From_Second_Name}." # Example "Osama M."


first_name = input('Add Your First Name :').strip().capitalize()
second_name = input('Add Your Second Name :').strip().capitalize()
print(f" Hello {first_name} {second_name[0]}.")


print("-" * 100)



# 4

email = input('Your Email : ').strip().lower()
userNme  = email[:email.index("@")].capitalize()
emailServiceProvider = email[email.index("@")+1:email.index(".")]
domain  = email[email.index(".") +1:]


print(f"Your Name is: {userNme}\nEmail Service Provider Is: {emailServiceProvider}\nTop Level Domain Is: {domain}")
