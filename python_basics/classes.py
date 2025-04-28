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

# -----------------------------------------------------------------------------

# Exercises 

# 9.1 Restaruant 

# class Restaurant:
#     """Simply attempt to decribe a restaurant."""

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """Display the information about the restaurant."""
#         print(f"This restaurant's name is {self.restaurant_name.title()}.")
#         print(f"This is {self.cuisine_type} restaurant.")

#     def open_restaurant(self):
#         """Display the restaurant is opening."""
#         print("This restauarant is open now!")

# restaurant = Restaurant('Suki', 'Raman')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# 9.2 Three Restaurants 


# class Restaurant:
#     """Simply attempt to decribe a restaurant."""

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """Display the information about the restaurant."""
#         print(f"This restaurant's name is {self.restaurant_name.title()}.")
#         print(f"This is {self.cuisine_type} restaurant.")

#     def open_restaurant(self):
#         """Display the restaurant is opening."""
#         print("This restauarant is open now!")

# restaurant = Restaurant('Suki', 'Raman')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# restaurant = Restaurant('Xiao', 'Buffet')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant = Restaurant('Shelby', 'Pizza')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# 9.3 Users 

# class User:
#     """Simple attempt to model a user."""

#     def __init__(self, first_name, last_name):
#         """Initilize attributes."""
#         self.first_name = first_name
#         self.last_name = last_name

#     def describe_user(self):
#         """Display user's name formatted in neatly."""
#         full_name = f"{self.first_name} {self.last_name}"
#         print(f"The user's name is {full_name.title()}.")

#     def greet_user(self):
#         """Greeting to the user by name."""
#         print(f"Hello, {self.first_name.title()}!")

# user = User('Naing', 'Lin')
# user.describe_user()
# user.greet_user()

# user = User('Neo', 'Xiao')
# user.describe_user()
# user.greet_user()

# -----------------------------------------------------------------------------

# Working With Classes and Instances 

# The Car Class 

# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initilize attributes to describe a car."""
#         self.make = make 
#         self.model = model
#         self.year = year 

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())


# Setting a Default Value for an Attribute

# class Car:
#     """A simple attempt to respresent a car."""

#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model
#         self.year = year 
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         """Return a neatly formatted name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()


# Modifying Attribute Values 

# Modifying an Attribute's Value Directly 

# class Car:
#     """A simple attempt to respresent a car."""

#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model
#         self.year = year 
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         """Return a neatly formatted name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23 
# my_new_car.read_odometer()


# Modifying an Attribute's Value Through a Method 


# class Car:
#     """A simple attempt to respresent a car."""

#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model
#         self.year = year 
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         """Return a neatly formatted name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back the odometer.")
    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(100)
# my_new_car.read_odometer()

# my_new_car.update_odometer(20)
# my_new_car.read_odometer()


# Incrementing an Attributes Value Through a Method 

# class Car:
#     """A simple attempt to respresent a car."""

#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model
#         self.year = year 
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         """Return a neatly formatted name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back the odometer.")

#     def increment_odometer(self, miles):
#         """Add the given amout to the odometer reading."""
#         self.odometer_reading += miles


# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# Note - You can use this medthos to control how users of your program update values 

# -----------------------------------------------------------------------------

# Exercises 

# 9.4 Number Served 

# class Restaurant:
#     """Simply attempt to decribe a restaurant."""

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """Display the information about the restaurant."""
#         print(f"This restaurant's name is {self.restaurant_name.title()}.")
#         print(f"This is {self.cuisine_type} restaurant.")

#     def open_restaurant(self):
#         """Display the restaurant is opening."""
#         print("This restauarant is open now!")

#     def display_number_served(self):
#         """Display number served today."""
#         print(f"We've served {self.number_served} customers today.")

#     def set_number_served(self, customers):
#         """Update the number served."""
#         self.number_served = customers
    
#     def increment_number_served(self, new_customers):
#         """Add new customers to the number served."""
#         self.number_served += new_customers


# restaurant = Restaurant('Suki', 'Raman')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# print(restaurant.number_served)

# restaurant.number_served = 10
# print(restaurant.number_served)

# restaurant = Restaurant('Suki', 'Raman')
# restaurant.set_number_served(100)
# print(restaurant.number_served)

# restaurant.increment_number_served(10)
# print(restaurant.number_served)

# restaurant = Restaurant('Suki', 'Raman')
# restaurant.set_number_served(100)
# restaurant.display_number_served()

# restaurant.increment_number_served(10)
# restaurant.display_number_served()


# 9.5 Login Attempts 

# class User:
#     """Simple attempt to model a user."""

#     def __init__(self, first_name, last_name):
#         """Initilize attributes."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0

#     def describe_user(self):
#         """Display user's name formatted in neatly."""
#         full_name = f"{self.first_name} {self.last_name}"
#         print(f"The user's name is {full_name.title()}.")

#     def greet_user(self):
#         """Greeting to the user by name."""
#         print(f"Hello, {self.first_name.title()}!")
    
#     def display_login_attempts(self):
#         """Display the login attempts."""
#         print(f"Your login attempts: {self.login_attempts}")

#     def increment_login_attempts(self):
#         """Increase login attempts by 1."""
#         self.login_attempts += 1
    
#     def reset_login_attempts(self):
#         """Reset the login attempts to 0."""
#         self.login_attempts = 0

# user = User('Naing', 'Lin')
# user.describe_user()
# user.greet_user()

# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.display_login_attempts()

# user.reset_login_attempts()
# user.display_login_attempts()