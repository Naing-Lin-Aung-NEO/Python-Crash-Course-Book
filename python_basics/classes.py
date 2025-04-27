# Classes 

# OOP - Object Oriented Programming 

# Creating and Using a Class 

# Creating the Dog Class 

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} is rolled over!")


# Making an Instance from a Class 

# my_dog = Dog('Whille', 6)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")


# Accessing Attributes 

# my_dog.name


# Calling Methods 

# my_dog = Dog('Whillie', 6)
# my_dog.sit()
# my_dog.roll_over()


# Creating Mutiple Instances 

# my_dog = Dog('Wille', 6)
# your_dog = Dog('Lucy', 3)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()


# print(f"Your dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()