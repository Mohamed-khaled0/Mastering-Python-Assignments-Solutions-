# 1

values = (0, 1, 2)

if any(values):

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good")

else:

  print("Bad")

# 2

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

print("-" * 100)


# 3

n = 20

l = list(range(n))               # max  = 10
if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

# Output => Good


print("-" * 100)

# 4

def my_all(iterable):
    for item in iterable:
        if not item:
            return False
    return True

def my_any(iterable):
    for item in iterable:
        if item:
            return True
    return False

def my_min(iterable):
    min_val = iterable[0]
    for item in iterable[1:]:
        if item < min_val:
            min_val = item
    return min_val

def my_max(iterable):
    max_val = iterable[0]
    for item in iterable[1:]:
        if item > max_val:
            max_val = item
    return max_val

# my_all
print(my_all([1, 2, 3]))           # True
print(my_all([1, 2, 3, []]))       # False

# my_any
print(my_any([0, 1, [], False]))   # True
print(my_any([(), 0, False]))      # False

# my_min
print(my_min([10, 100, -20, -100, 50]))     # -100
print(my_min((10, 100, -20, -100, 50)))     # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700]))   # 700
print(my_max((10, 100, -20, -100, 50, 700)))   # 700
