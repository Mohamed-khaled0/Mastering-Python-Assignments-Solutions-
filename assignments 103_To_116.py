# 1
class Game:
  def __init__(self,n,d,y,p):
    self.name = n
    self.developer = d
    self.year = y
    self.price = p

  def price_in_pounds(self) :
     price_in_pounds = float(self.price)
     return f"{price_in_pounds}"
  
game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"


print('1' * 120)

# 2

class User:
 def __init__(self,f_name,second_name,age,gender):
    self.fname= f_name
    self.sname= second_name    
    self.age= age    
    self.gender= gender


 def full_details(self):
    title = f"Mr"  if self.gender == "Male" else "Ms"
    age_to_40 = 40 - self.age
    return(f"Hello {title} {self.fname} {self.sname[0]}. [{age_to_40}] Years To Reach 40 ")

user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40




print('-' * 120)

# 3 - 

class Message:
    @staticmethod
    def print_message():
      return("Hello From Class Message")

print(Message.print_message())

# Output
# Hello From Class Message



print('-' * 120)

# 4 - 
class Games:
    def __init__(self, data):
        self.data = data

    def show_games(self):
        if isinstance(self.data, str):
            print(f'I Have One Game Called "{self.data}"')
        elif isinstance(self.data, list):
            print("I Have Many Games:")
            for game in self.data:
                print(f"-- {game}")
        elif isinstance(self.data, int):
            print(f"I Have {self.data} Game.")

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.




print('-' * 120)




# 5 - 
# Main Class
class Members:

  def __init__(self, n, p):

    self.name = n

    self.permission = p

  def show_info(self):

    return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here
class Admins(Members):
    pass
   
# Create Moderators Class Here
class Moderators(Members):
   def __init__(self, n, p):
      super().__init__(n,p)
   
member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator

print('-' * 120)




# 6 - 
class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C:

  def __init__(self, three):

    self.three = three

class Text(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)

    def show_name(self):
        return f"The Name Is {self.one}{self.two}{self.three}"
    
the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero