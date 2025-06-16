# 1
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
  my_data.extend(data)

final_string = ''
for char in my_data:
  if isinstance(char, str):
    final_string += char

print(final_string.capitalize())  # Elzero



print('-' *120)

# 2
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
  if isinstance(item1, str):
    my_data.append(item1)

final_string = ''.join(my_data).capitalize()

print(final_string)  # Elzero

print('-' *120)

# 3
from PIL import Image

from PIL import Image

img = Image.open(r'C:\Users\dell\Desktop\elzero-pillow.png')
img.show()



print("-" * 100)

# 4

print("-" * 100)

# 5