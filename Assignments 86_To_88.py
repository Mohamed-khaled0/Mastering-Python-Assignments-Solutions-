"""Assignments 86 To 88 Solutions."""

from PIL import Image

# 1
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    my_data.extend(data)

final_string_one = ''
for char in my_data:
    if isinstance(char, str):
        final_string_one += char

print(final_string_one.capitalize())  # Elzero
print('-' * 120)

# 2
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple2 = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data_two = []

for item1, item2, item3 in zip(my_list1, my_tuple2, my_list2):
    if isinstance(item1, str):
        my_data_two.append(item1)

final_string_two = ''.join(my_data_two).capitalize()
print(final_string_two)  # Elzero
print('-' * 120)

# 3 - Image Processing

image = Image.open(r'C:\Users\dell\Desktop\elzero-pillow.png')

# First image - cut "L" and convert to grayscale
box_one = (400, 0, 800, 400)
new_image_one = image.crop(box_one)
gray_image_one = new_image_one.convert("L")
gray_image_one.save(r'C:\Users\dell\Desktop\elzero_output1.png')  # Save it

# Second image - cut second row and rotate
box_two = (0, 400, 1200, 800)
new_image_two = image.crop(box_two)
gray_image_two = new_image_two.convert("L")
rotated_image_two = gray_image_two.rotate(180)
rotated_image_two.save(r'C:\Users\dell\Desktop\elzero_output2.png')  # Save it
print("-" * 120)

# 4 - Function With Docstring
def say_hello_to(name):
    """
    parameter(someone) => Person Name
    Function To Say Hello To Anyone
    """
    return f"Hello {name}"


print(say_hello_to("Osama"))  # "Hello Osama"
print(say_hello_to.__doc__)
print("-" * 120)

# 5 - Say Hello Function
my_friends = ["Ahmed", "Osama", "Sayed"]


def say_hello(some_people):
    """Say Hello To Each Person In The List."""
    for someone in some_people:
        print(f"Hello {someone}")


say_hello(my_friends)
