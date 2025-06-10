#1 , 2 , 3
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
python_folder = os.path.join(desktop, "Python")
os.makedirs(python_folder, exist_ok=True)

cwd = os.getcwd()

for i in range(1, 51):
    if i == 25:
        filename = "special-text.txt"
    else:
        filename = f"txt{i}.txt"

    file_path = os.path.join(python_folder, filename)

    with open(file_path, 'w') as f:
        if i != 25:
            f.write(f"Elzero Web School => {i}\n")

# ---------------------------------------------------------

file1_path = os.path.join(python_folder, "txt1.txt")

with open(file1_path, 'a') as f:  
    for _ in range(50):
        f.write("Appended => Elzero Web School\n")

print("-" * 60)

# ---------------------------------------------------------

with open(file1_path, 'r') as f:
    content = f.read()

lines = content.strip().splitlines()
words = content.split()
chars = len(content)
l_count = content.count("l")

print(f'"Number Of Lines Is => {len(lines)}"')
print(f'"Number Of Words Is => {len(words)}"')
print(f'"Number Of Chars Is => {chars}"')
print(f'"Number Of "l" Char Is => {l_count}"')
