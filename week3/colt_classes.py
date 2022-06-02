# #DEFINING THE SIMPLEST POSSIBLE CLASS

# from unicodedata import name


# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

# user1 = User("Joe", "Thomas", 36)
# user2 = User("Blanca", "Garcia", 4)

# print(user1.first)
# print(user2.age)

# class Comment:
#     def __init__(self, username, text, likes = 0):
#         self.username = username
#         self.text = text
#         self.likes = likes

# c = Comment("davey123", "lol you're so silly, 3")
# print(c.username)
# print(c.text)
# print(c.likes)

# class BankAccount:
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0.0
    
#     def getBalance(self):
#         return self.balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    
#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance
class Pet:
    allowed = ["cat", "dog", "fish", "rat"]
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")





        

