# Function 

# Defining a Function 

# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")

# greet_user()


# Passing Information to a Function 

# def greet_user(username):
#     """Display a simple greeting by name."""
#     print(f"Hello, {username.title()}!")

# greet_user('neo')
# greet_user('lin')


# Arguments and Parameters 

# -----------------------------------------------------------------------------

# Exercises 

# 8.1 Messages 

# def display_message():
#     """Dispaly what I am learning in this chapter."""
#     print("I'm learning how to work with functions in this chapter.")

# display_message()


# 8.2 Favorite Book 

# def favorite_book(title):
#     """Display my favorite name."""
#     print(f"One of my favorite books is {title}.")

# favorite_book("Cinderella")

# -----------------------------------------------------------------------------

# Passing Arguments 

# Positional Arguments , Multiple Function call

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'whillie')


# Order Matters in Positional Arguments

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('harry', 'hamster')


# Keyword Arguments 

# def describe_pet(animal_type, pet_name):
#     """Describe information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='harry')

# describe_pet(pet_name='harry', animal_type='hamster')


# Default Values 

# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='whillie')

# describe_pet(pet_name='harry', animal_type='hamster')


# Equivalent Function Calls 

# A dog named Whillie 
# describe_pet('whillie')
# describe_pet(pet_name='whillie')

# A hamster named Harry 
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')


# Avoiding Arguments Errors 

# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet()

# -----------------------------------------------------------------------------

# Exercises 

# 8.3 T-shirt

# def make_shirt(size, message):
#     """Making a different size shirt with customize message."""
#     print(f"\nI've made a {size.upper()}-size shirt with this text:")
#     print(f"\t{message.title()}")

# make_shirt('m', 'i love you')
# make_shirt(size='xl', message='i hate you')

