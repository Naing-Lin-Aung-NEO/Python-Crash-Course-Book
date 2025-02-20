
class User:
    """Build a model of User profile."""
    def __init__(self, first_name, middle_name, last_name, location):
        """Initilize all attributes."""
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name 
        self.location = location

    def describe_user(self):
        """Summary of the user's information."""
        name = f"{self.first_name} {self.middle_name} {self.last_name}"
        print(f"My name is {name.title()}.")
        print(f"I lived in {self.location.title()}.")

    def greet_user(self):
        """Greet user with his name."""
        print(f"Hello, {self.last_name}!")
