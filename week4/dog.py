
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


buddy = Dog("Buddy", 9, "poodle")
miles = Dog("Miles", 4, "german shepard")

print(buddy.name)
print(buddy.age)
print(buddy.breed)
print(buddy.species)


#Values can be changed dynamically
buddy.age = 10
print(buddy.age)

#Instance method
def description(self):
    return f"{self.name} is {self.age} years old"

#Another instance method
def speak(self, sound):
    return f"{self.name} says {sound}"





