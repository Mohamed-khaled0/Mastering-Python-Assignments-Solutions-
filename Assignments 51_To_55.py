# 1
# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
# Needed Output
"1 => 20"
"2 => 15"
"3 => 5"
"All Numbers Printed"

my_nums.sort(reverse=True)
count = 0
for number in my_nums :
    if number %5 ==0 :
        count+=1
        print(f"{count} => {number}")
print('All Numbers Printed')




# 2
# Needed Output
"01"
"02"
"03"
"04"
"05"
"07"
"09"
"10"
"11"
"13"
"14"
"15"
"16"
"17"
"18"
"19"
"20"
"All Numbers Printed"

my_nums1 = range(1,21)

for num in my_nums1:
    if num == 6 or num == 8 or num == 12:
        continue
    elif num <10 :
        print(f"0{num}")
    else : 
        print(num)

print('Done')

print("-" * 100)



# 3
# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

# Needed Output
"My Rank in Math Is A And This Equal 100 Points"
"My Rank in Science Is B And This Equal 80 Points"
"My Rank in Drawing Is A And This Equal 100 Points"
"My Rank in Sports Is C And This Equal 40 Points"
"Total Points Is 320"

# points_mapping = {
#     "A": 100,
#     "B": 80,
#     "C": 40,
#     "D": 20,
#     "F": 0
# }

# total_points = 0
# for subject, grade in my_ranks.items():
#     points = points_mapping[grade]
#     print(f"My Rank in {subject} Is {grade} And This Equal {points} Points")
#     total_points += points

# print(f"Total Points Is {total_points}")

print("-" * 100)



# 4
points_mapping = {
    "A": 100,
    "B": 80,
    "C": 40,
    "D": 20,
    "F": 0
}

# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}


# Needed Output
"------------------------------"
"-- Student Name => Ahmed"
"------------------------------"
"- Math => 100 Points"
"- Science => 20 Points"
"- Draw => 80 Points"
"- Sports => 40 Points"
"- Thinking => 100 Points"
"Total Points For Ahmed Is 340"
"------------------------------"
"-- Student Name => Sayed"
"------------------------------"
"- Math => 80 Points"
"- Science => 80 Points"
"- Draw => 80 Points"
"- Sports => 20 Points"
"- Thinking => 100 Points"
"Total Points For Sayed Is 360"
"------------------------------"
"-- Student Name => Mahmoud"
"------------------------------"
"- Math => 20 Points"
"- Science => 100 Points"
"- Draw => 100 Points"
"- Sports => 80 Points"
"- Thinking => 80 Points"
"Total Points For Mahmoud Is 380"

# Solution 
for student, subjects in students.items():
    print("-" * 30)
    print(f"-- Student Name => {student}")
    print("-" * 30)

    total_points = 0
    
    for subject, grade in subjects.items():
        points = points_mapping[grade]
        print(f"- {subject} => {points} Points")
        total_points += points
    print(f"Total Points For {student} Is {total_points}")