# Create and Using classes 

# Creating the Dog Class 

class Dog: 
    """A smiple attempt to model a dog."""

    def __init__(self, name, age):
        """Initilize name and age attributes."""
        self.name = name 
        self.age = age 

    def sit(self):
        """Simulate a dog stting in response to a command."""
        print(f"{self.name} is sitting now.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# dog = Dog('Kira', 4)
# dog.roll_over()
# dog.sit()

# print(f"My dog name is {dog.name}.")
# print(f"My dog age is {dog.age}.")

# your_dog = Dog('Willie', 5)
# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog's age is {your_dog.age}.")
# your_dog.sit()

# -----------------------------------------------------------------------------

# Exercise

# Restaurant

class Restaurant:
    """Simple attempt to model a restaurant."""

    def __init__(self, name, type):
        """Intilizing name and type attributes."""
        self.name = name 
        self.type = type 

    def describe_restaurant(self):
        """Just describing the restaruant name and type."""
        print(f"The restaurant's name & type is {self.name} and {self.type}.")

    def open_restaurant(self):
        """Show the resturant is opening."""
        print(f"{self.name} is opening now.")

# restaurant = Restaurant("Hell", "Raman")
# print(f"{restaurant.name}'s {restaurant.type}")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# -----------------------------------------------------------------------------

# Three Restaurants

# my_restaurant = Restaurant("Neo's", "Raman")
# your_restaurant = Restaurant("Cony's", "Steak")
# his_restaurant = Restaurant("Joe's", "Soup")

# my_restaurant.describe_restaurant()
# your_restaurant.describe_restaurant()
# his_restaurant.describe_restaurant()

# -----------------------------------------------------------------------------

# Users 

class User:
    """Simple attempt to model a user."""

    def __init__(self, first_name, last_name):
        """Intilized first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

# user = User("Naing", "Lin")
# user.describe_user()
# user.greet_user()

# user2 = User("Aung", "Lin")
# user.describe_user()
# user.greet_user()

# -----------------------------------------------------------------------------

# Working with Classes and Instances 

# -----------------------------------------------------------------------------

# The Car Class 

# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Intilize attributes to describe a car."""
#         self.make = make 
#         self.model = model
#         self.year = year 
    
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         full_name = f"{self.year} {self.make} {self.model}"
#         return full_name.title()
        
# my_newcar = Car('audi', 'a4', 2024)
# name = my_newcar.get_descriptive_name()
# print(name)

# --------

# Setting a Default Value for an Attribute

# class Car:

#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 
    
#     def get_descriptive_name(self):
#         full_name = f"{self.year} {self.make} {self.model}"
#         return full_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")
    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# -----------------

# Modifying Attribute Values 

# 1 modifying an attribut's value directly 

# class Car:

#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 
    
#     def get_descriptive_name(self):
#         full_name = f"{self.year} {self.make} {self.model}"
#         return full_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")
    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# 2 modifying an attribute's value through a method 

# class Car:

#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 
    
#     def get_descriptive_name(self):
#         full_name = f"{self.year} {self.make} {self.model}"
#         return full_name.title()

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
#             print("You can't roll back an odometer.")
    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(23)
# # my_new_car.update_odometer(1)
# my_new_car.read_odometer()

# ----------------

# 3 incrementing an attribute's value through a method 

# class Car:

#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 
    
#     def get_descriptive_name(self):
#         full_name = f"{self.year} {self.make} {self.model}"
#         return full_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")
    
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer.")
    
#     def incremet_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

    
# my_new_car = Car('audi', 'a4', 2024)

# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(23)

# my_new_car.update_odometer(20)

# my_new_car.incremet_odometer(100)
# my_new_car.read_odometer()

# -----------------------------------------------------------------------------

# Exercises 

# Number Served 

# class Restaurant:
#     """Simple attempt to model a restaurant."""

#     def __init__(self, name, type):
#         """Intilizing name and type attributes."""
#         self.name = name 
#         self.type = type 
#         self.number_served = 0 

#     def describe_restaurant(self):
#         """Just describing the restaruant name and type."""
#         print(f"The restaurant's name & type is {self.name} and {self.type}.")

#     def open_restaurant(self):
#         """Show the resturant is opening."""
#         print(f"{self.name} is opening now.")
    
#     def set_number_served(self, new_number_served):
#         self.number_served = new_number_served
    
#     def increment_number_served(self, add_number_served):
#         self.number_served += add_number_served
    

# restaurant = Restaurant("Hell", "Raman")

# customers = restaurant.number_served
# print(customers)

# restaurant.set_number_served(23)
# print(restaurant.number_served)

# restaurant.increment_number_served(100)
# print(restaurant.number_served)

# ---------------------

# Login Attempts 

class User:
    """Simple attempt to model a user."""

    def __init__(self, first_name, last_name):
        """Intilized first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0 

    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1 

    def reset_login_attempts(self):
        self.login_attempts = 0 

# user = User('naing', 'lin')
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# # print(user.login_attempts)

# user.reset_login_attempts()
# print(user.login_attempts)


# -----------------------------------------------------------------------------

# Inheritance 

# The __init__() mehthod for a Child class 

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year 
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading}miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectriceCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

# my_leaf = ElectriceCar('nissian', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# -----------------------------------------------------------------------------
# Defining Attribute and Methods for the Child Class 

# class Car:

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model 
#         self.year = year 
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading}miles on it.")

#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# class ElectriceCar(Car):

#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 40 

#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def fill_gas_tank(self):
#         print("This car doesn't have a gas tank!")
    
# my_leaf = ElectriceCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()

# -----------------------------------------------------------------------------

# Instance as Attribute 

class Car():

    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year 
        self.odometer_reading = 0 

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    
    def __init__(self,battery_size = 40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")
    
class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# print(my_leaf.battery.battery_size)
# my_leaf.battery.get_range()

# -----------------------------------------------------------------------------

# Exercises

# Ice Cream Stand

class Restaurant:
    """Simple attempt to model a restaurant."""

    def __init__(self, name, type):
        """Intilizing name and type attributes."""
        self.name = name 
        self.type = type 
        self.number_served = 0 

    def describe_restaurant(self):
        """Just describing the restaruant name and type."""
        print(f"The restaurant's name & type is {self.name} and {self.type}.")

    def open_restaurant(self):
        """Show the resturant is opening."""
        print(f"{self.name} is opening now.")
    
    def set_number_served(self, new_number_served):
        self.number_served = new_number_served
    
    def increment_number_served(self, add_number_served):
        self.number_served += add_number_served

class IceCreamStand(Restaurant):

    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['strawberry', 'chocolate', 'vinilla', 'mango']
    
    def display_flavors(self):
        print("You can get these flaovors:")
        for flavor in self.flavors:
            print(f"\t-{flavor.title()}")

# ice_cream = IceCreamStand('NEO', 'Ice Cream')
# ice_cream.describe_restaurant()
# ice_cream.display_flavors()

# -------------
# Admin 

class User:
    """Simple attempt to model a user."""

    def __init__(self, first_name, last_name):
        """Intilized first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0 

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"The user's name is {full_name.title()}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1 

    def reset_login_attempts(self):
        self.login_attempts = 0 

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The admin's privileges are:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")
        
# admin = Admin('lin', 'aung')
# admin.describe_user()
# admin.show_privileges()

# ---------------------
# Privileges

class User:
    """Simple attempt to model a user."""

    def __init__(self, first_name, last_name):
        """Intilized first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0 

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"The user's name is {full_name.title()}.")

class Privileges():
    
    def __init__(self, privileges = ['can add post', 'can delete post',
    'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print('The Privileges are:')
# admin = Admin('naing', 'lin')
# admin.privileges.show_privileges()    
        for privilege in self.privileges:
            print(f"\t-{privilege}")

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


# admin = Admin('naing', 'lin')
# admin.privileges.show_privileges()        

# ------------------------
# Battery Upgrade 

class Car():

    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year 
        self.odometer_reading = 0 

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    
    def __init__(self,battery_size = 40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")
    
class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# tesla = ElectricCar('tesla', 'model-S', 2024)
# print(tesla.get_descriptive_name())
# print(tesla.battery.battery_size)
# tesla.battery.get_range()

# tesla.battery.upgrade_battery()
# print(tesla.battery.battery_size)
# tesla.battery.get_range()

# ---------------------------------------------------------

# Importing Classes 

# from class_module import Car 

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# from class_module import ElectricCar

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

# from class_module import Car,ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissian', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# import class_module

# my_mustang = class_module.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = class_module.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# from class_module import ElectricCar as EC 

# my_leaf = EC('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# -----------------------------------------------------------------------------
# Exercies (SKIP)

# -----------------------------------------------------------------------------

# The Python Standard Library 

# from random import randint

# num = randint(1, 10)
# print(num)

# from random import choice 
# players = ['neo', 'leo', 'coco', 'ni ni', 'mi mi']
# first_up = choice(players)
# print(first_up)

# -----------------------------------------------------------------------------

# Dice

from random import randint

class Dice():

    def __init__(self, sides=6):
        self.sides = sides 

    def roll_dice(self):
        random_num = randint(1, self.sides)
        print(random_num)

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

# dice = Dice(sides=10)
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

# -------------------

# Lottery 

# from random import choice

# nums = list(range(0,10))
# letters = ['A', 'B', 'C', 'D', 'E']
# lottery_ticket = []

# selected_letter = choice(letters)
# lottery_ticket.insert(0, selected_letter)

# while True:

#     if len(lottery_ticket) < 5:
#         slected_num = choice(nums)
#         lottery_ticket.append(slected_num)
#     else:
#         break

# print(f"The winning prize ticket is {lottery_ticket}.")

# -------------------

# Lottery Analysis 

# from random import choice

# win_ticket = ['C', 1, 8, 9, 7]

# nums = list(range(0,10))
# letters = ['A', 'B', 'C', 'D', 'E']
# countdown = 0

# while True:
#     lottery_ticket = []
    
#     selected_letter = choice(letters)
#     lottery_ticket.append(selected_letter)

#     while len(lottery_ticket) < 5:
#         selected_num = choice(nums)
#         lottery_ticket.append(selected_num)
    
#     countdown += 1
    
#     if lottery_ticket == win_ticket:
#         break
        
# print(f"At {countdown} times, you will win the lottery!")

# from random import choice

# win_ticket = ['C', 1, 8, 9, 7]

# nums = list(range(0,10))
# letters = ['A', 'B', 'C', 'D', 'E']
# countdown = 0

# while True:
#     lottery_ticket = [choice(letters)] + [choice(nums) for _ in range(4)]
#     countdown += 1

#     if win_ticket == lottery_ticket:
#         break


# print(f"At {countdown} times, you will win the lottery!")

# -----------------------------------------------------------------------------

# Python module of the week 