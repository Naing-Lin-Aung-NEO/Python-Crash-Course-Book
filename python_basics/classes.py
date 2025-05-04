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

# -----------------------------------------------------------------------------

# Inheritance 

# The __init__() Method for a Child Class 

# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initilize attributes to describe a car."""
#         self.make = make 
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         fullname = f"{self.year} {self.make} {self.model}"
#         return fullname.title()

#     def read_odometer(self):
#         """PRint a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading}-miles on it.")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
    
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())


# Defining Attributes and Methods for the Child Class, Overriding Methods 

# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initilize attributes to describe a car."""
#         self.make = make 
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         fullname = f"{self.year} {self.make} {self.model}"
#         return fullname.title()

#     def read_odometer(self):
#         """PRint a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading}-miles on it.")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
    
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 40

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")
    
#     def fill_gas_tank(self):
#         """Electric cars don't have gas tanks."""
#         print("This car don't have a gas tank.")

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# my_leaf.describe_battery()
# my_leaf.fill_gas_tank()


# Instances as Attributes 

# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initilize attributes to describe a car."""
#         self.make = make 
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         fullname = f"{self.year} {self.make} {self.model}"
#         return fullname.title()

#     def read_odometer(self):
#         """PRint a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading}-miles on it.")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
    
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
    
# class Battery:
#     """A simple attempt to model a battery for an Electric Car."""

#     def __init__(self, battery_size = 40):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")
    
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225
        
#         print(f"This car can go about {range} miles on a full charge.")

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then Initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = Battery()

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# my_leaf.battery_size.describe_battery()
# my_leaf.battery_size.get_range()


# Modeling Real-World Objects 

# -----------------------------------------------------------------------------

# Exercises 

# 9.6 Ice Cream Stand 

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

# class IceCreamStand(Restaurant):
#     """Represent aspects of a restaurant, specifically ice cream stand."""

#     def __init__(self, restaurant_name, cuisine_type):
#         """
#         Initialize attributes of the parent class.
#         Then Initialize attributes for child class.
#         """
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['strawberry', 'banana', 'chocolate', 'vanilla']

#     def display_flavors(self):
#         """Display flavors that can get from the restaruant."""
#         print("\nYou can get these flavors from Ice Cream Stand:")
#         for flavor in self.flavors:
#             print(f"- {flavor.title()}")

# ice_cream = IceCreamStand("Sweety", 'ice-cream')
# ice_cream.display_flavors()
# ice_cream.describe_restaurant()


# 9.7 Admin 

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

# class Admin(User):
#     """Simple attempt to represent an admin."""

#     def __init__(self, first_name, last_name):
#         """
#         Initialize the attributes of the parents class.
#         Then initialize new attributes for the child class.
#         """
#         super().__init__(first_name, last_name)
#         self.privileges = [
#                             "can add post",
#                             "can delete post",
#                             "can ban user",
#                             "can change channel's name"
#                           ]
        
#     def show_privileges(self):
#         """Display privileges of an admin."""
#         print("Admin can do these privileges:")
#         for privilege in self.privileges:
#             print(f"- {privilege.title()}")

# admin = Admin('Naing', 'Aung')
# admin.show_privileges()


# 9.8 Privileges 

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

# class Privileges:
#     """A Simple attempt to make privileges for admin."""

#     def __init__(self, privileges = [
#                             "can add post",
#                             "can delete post",
#                             "can ban user",
#                             "can change channel's name"
#     ]):
#         self.privileges = privileges
    
#     def show_privileges(self):
#         """Display privileges of an admin."""
#         print("Admin can do these privileges:")
#         for privilege in self.privileges:
#             print(f"- {privilege.title()}")
            

# class Admin(User):
#     """Simple attempt to represent an admin."""

#     def __init__(self, first_name, last_name):
#         """
#         Initialize the attributes of the parents class.
#         Then initialize new attributes for the child class.
#         """
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges()


# admin = Admin('Naing', 'Aung')
# admin.privileges.show_privileges()


# 9.9 Battery Upgrade 

# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initilize attributes to describe a car."""
#         self.make = make 
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         fullname = f"{self.year} {self.make} {self.model}"
#         return fullname.title()

#     def read_odometer(self):
#         """PRint a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading}-miles on it.")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
    
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
    
# class Battery:
#     """A simple attempt to model a battery for an Electric Car."""

#     def __init__(self, battery_size = 40):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")
    
#     def upgrade_battery(self):
#         """Upgrade battery if battery size is 40 kWh."""
#         if self.battery_size != 65:
#             self.battery_size = 65
    
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225
        
#         print(f"This car can go about {range} miles on a full charge.")

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then Initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = Battery()

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# my_leaf.battery_size.describe_battery()
# my_leaf.battery_size.get_range()

# my_leaf.battery_size.upgrade_battery()
# my_leaf.battery_size.describe_battery()
# my_leaf.battery_size.get_range()

# -----------------------------------------------------------------------------

# Importing Classes 

# from class_modules import Car 

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())


# Importing Multiple Classes from a Module 

# from class_modules import Car, ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())


# Improting an Entire Module 

# import class_modules

# my_mustang = class_modules.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = class_modules.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())


# Importing All classes from a Module 

# from class_modules import *


# Importing a Module into a Module 



# Using Aliases 

# Aliaes = nickname for function, class, ... 

# from class_modules import ElectricCar as EC 

# -----------------------------------------------------------------------------

# Exercises 

# 9.10 Imprted Restaurant

# from class_modules import Restaurant

# restaurant = Restaurant('Neo', 'ice cream')
# restaurant.describe_restaurant()

# 9.11 Imported Admin 

# from class_modules import User, Privileges, Admin

# admin = Admin('Naing', 'Aung')
# admin.privileges.show_privileges()


# 9.12 Multiple Modules 

# -----------------------------------------------------------------------------

# Python Standard Library

# from random import randint

# print(randint(1, 6))

# from random import choice

# players = ['neo', 'lin', 'aung', 'khaing']
# firt_up = choice(players)
# print(firt_up)

# -----------------------------------------------------------------------------

# Exercises 

# 9.11 Dice 

from random import randint

# class Dice:
#     """A simple attempt to represent a dice."""

#     def __init__(self, sides=6):
#         """Initialize attributes for a dice."""
#         self.sides = sides

#     def roll_dice(self):
#         """Roll a dice randomly to choose a number 1 to numbers of sides."""
#         side = randint(1, self.sides)
#         print(side)


# dice = Dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()

# dice = Dice(10)
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()

# dice = Dice(20)
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()
# dice.roll_dice()


# 9.14 Lottery 

# from random import choice

# numbers = list(range(0,10))
# letters = ['A', 'B', 'C', 'D', 'E']
# ticket = []

# letter = choice(letters)
# ticket.append(letter)
# # print(ticket)

# while len(ticket) < 6:
#     number = choice(numbers)
#     ticket.append(number)

# print("This ticket win the lottery!")
# print(ticket)


# 9.15 Lottery Analysis 

# from random import choice

# numbers = list(range(0,10))
# letters = ['A', 'B', 'C', 'D', 'E']
# ticket = []
# my_ticket = []
# count = 0

# letter = choice(letters)
# ticket.append(letter)

# while len(ticket) < 6:
#     number = choice(numbers)
#     ticket.append(number)

# while True:
#     while len(my_ticket) < 1:
#         letter = choice(letters)
#         my_ticket.append(letter)

#     while len(my_ticket) < 6:
#             number = choice(numbers)
#             my_ticket.append(number)
    
#     count += 1 

#     if my_ticket == ticket:
#         break
#     else: 
#         while my_ticket:
#             for element in my_ticket:
#                 my_ticket.remove(element)
#         continue

# print(f"You can win the lottery at {count} times!")


# 9.16 Python Module of the Week

# https://pymotw.com 

# -----------------------------------------------------------------------------
