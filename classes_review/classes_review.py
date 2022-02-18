# 2/7/2022
# Review of classes theory to prep for Hacker rank testing.
#Notes:
# Chapter 9, pg 158
#Making an object from a class is called instantiation.


class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age, breed):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.breed = breed

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} has rolled over!")

    def bark(self):
        """Simulate dog barking."""
        print(f"{self.name} is barking!")

    def walk_dog(self):
        """Simulate the action of taking the dog for a walk."""
        walks = [9, 1, 6, 9]
        for walk in walks:
            if walks[0:2]:
                walk = str(walk) + " am"
                print(f"It is {walk}. Taking {self.name} for a walk.")
            elif walks[2:4]:
                walk = str(walk) + 'pm'
                print(f"It is {walk} o'clock. Taking {self.name} for a walk.")


# Making an instance of the class Dog.
pooch = Dog("Rocket", 10, "Chiuahua Pitbull mix")

# print(pooch.name, pooch.age, pooch.breed)
print(f"My dog's name is {pooch.name}, she is a {pooch.breed}, and is {pooch.age} years old.\n")
# pooch.sit()
# pooch.roll_over()
# pooch.bark()
# pooch.walk_dog()

# Class method:
pooch.walk_dog()
