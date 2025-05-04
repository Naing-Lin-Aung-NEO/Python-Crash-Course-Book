# Car Class 

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initilize attributes to describe a car."""
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        fullname = f"{self.year} {self.make} {self.model}"
        return fullname.title()

    def read_odometer(self):
        """PRint a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading}-miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car don't have a gas tank.")

# Class Restaruant 

class Restaurant:
    """Simply attempt to decribe a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display the information about the restaurant."""
        print(f"This restaurant's name is {self.restaurant_name.title()}.")
        print(f"This is {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Display the restaurant is opening."""
        print("This restauarant is open now!")

    def display_number_served(self):
        """Display number served today."""
        print(f"We've served {self.number_served} customers today.")

    def set_number_served(self, customers):
        """Update the number served."""
        self.number_served = customers
    
    def increment_number_served(self, new_customers):
        """Add new customers to the number served."""

        self.number_served += new_customers

# Class User 

class User:
    """Simple attempt to model a user."""

    def __init__(self, first_name, last_name):
        """Initilize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Display user's name formatted in neatly."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"The user's name is {full_name.title()}.")

    def greet_user(self):
        """Greeting to the user by name."""
        print(f"Hello, {self.first_name.title()}!")
    
    def display_login_attempts(self):
        """Display the login attempts."""
        print(f"Your login attempts: {self.login_attempts}")

    def increment_login_attempts(self):
        """Increase login attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0

class Privileges:
    """A Simple attempt to make privileges for admin."""

    def __init__(self, privileges = [
                            "can add post",
                            "can delete post",
                            "can ban user",
                            "can change channel's name"
    ]):
        self.privileges = privileges
    
    def show_privileges(self):
        """Display privileges of an admin."""
        print("Admin can do these privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")
            

class Admin(User):
    """Simple attempt to represent an admin."""

    def __init__(self, first_name, last_name):
        """
        Initialize the attributes of the parents class.
        Then initialize new attributes for the child class.
        """
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
