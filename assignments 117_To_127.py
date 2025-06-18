# 1
# INTEGER , TEXT ,VARCHAR(n) , CHAR , FLOAT , DATE
import sqlite3

print('-' * 120)

# 2. 
db = sqlite3.connect("elzero.db")
cr = db.cursor()

cr.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY UNIQUE,
    name TEXT UNIQUE,
    birthdate TEXT,
    user_email TEXT UNIQUE
)
''')
db.commit()

print('-' * 120)

# 3
users_data = [
    (1, "Ahmed", "1990-01-15", "ahmed@example.com"),
    (2, "Sara", "1992-07-23", "sara@example.com"),
    (3, "Mona", "1995-03-10", "mona@example.com"),
    (4, "Ali", "1988-12-05", "ali@example.com"),
    (5, "Omar", "1993-09-30", "omar@example.com")
]

for user in users_data:
    cr.execute('''
    INSERT OR IGNORE INTO users (user_id, name, birthdate, user_email)
    VALUES (?, ?, ?, ?)
    ''', user)

db.commit()


print('-' * 120)



#4-
cr.execute("SELECT * FROM users WHERE user_id=5")
rows = cr.fetchall()

for row in rows:
    print(row)


# 5 
try:
    user_id = int(input("Enter User ID To Delete: "))
except ValueError:
    print("Invalid ID.")
    db.close()
    exit()

cr.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
user = cr.fetchone()

if user:
    cr.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    db.commit()

    print("User Deleted.")
    print("Show Other Data:")

    cr.execute("SELECT * FROM users ORDER BY user_id")
    rows = cr.fetchall()

    for row in rows:
        print(f"ID => {row[0]}, Name => {row[1]}, Date Of Birth => {row[2]}, Email => {row[3]}")

else:
    print("User Not Found.")
