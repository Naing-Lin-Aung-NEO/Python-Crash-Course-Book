# How the input() Function Works

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# ------------------------------------------------

# Writing Clear Prompts 

# name = input("Please enter your name: ")
# print(f"\nHello, {name.title()}!")

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello, {name.title()}!")

# ------------------------------------------------

# Using int() to Accept Numerical Input 

# age = input("How old are you? ")
# age = int(age)
# if age >= 18:
#     print("You can vote now!")
# else:
#     print("Wait to vote unitl 18!")


# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older!")

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"The number {number} is odd.")

# ------------------------------------------------

# Exercises 

# Rental car 

# car = input("What kind of rental car would you like, sir? ")
# rental_car = f"Let me see if I can find you a {car}."

# print(rental_car)

# -----------------------

# Resturant Seating

# people = input("How many people are in your dinner group,Sir? ")
# people = int(people)

# if people > 8:
#     print("You'll have to wait for a table!")
# else:
#     print("Your table is ready!")

# ---------------------

# Multiples of Ten 

# number = input("Enter a number, I'll tell you if it's a multiple of 10 or not: ")
# number = int(number)

# if number % 10 == 0:
#     print(f"The number {number} is a multiple of 10.")
# else:
#     print(f"The number {number} is not a multiple of 10.")

# ----------------------------------------------------------------------------

# Introducing while loops 

# The while loop in Action 

# current_number = 1

# while current_number <= 5:
#     print(current_number)
#     current_number += 1 

# Letting the User Choose when to Quit 

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

# -----------------------------------------------------

# Using a flag 

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# -----------------------------------------------------

# Using break to Exit a Loop 

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)
    
#     if city == 'quit':
#         break
#     else: 
#         print(f"I'd love to go to {city.title()}!")

# -----------------------------------------------------

# Using continue in a Loop 

# current_number = 0
# while current_number < 10:
#     current_number += 1 
#     if current_number % 2 == 0: 
#         continue
#     print(current_number)

# -----------------------------------------------------

# Exercise 

# Pizza Toppings (ver 1 ---> break)

# prompt = "\nWhich topping would you like to add to your pizza:"
# prompt += "\n (Enter 'quit' if you are done!) "

# while True:
#     message = input(prompt)

#     if message == 'quit':
#         print("\n\tYour pizza will be done in a minute!")
#         break
#     else:
#         print(f"\n\tI'm adding {message}!")

# --------------------

# Movie Tickets 

# prompt = "\nHow old are you? "

# while True:
#     age = input(prompt)
#     age = int(age)

#     if age < 3:
#         print("\nYour ticket costs $0.")
#         break
#     elif age <= 12:
#         print("\nYour ticket costs $10.")
#         break
#     else:
#         print("\nYour ticket costs $15.")
#         break

# --------------------

# Pizza Toppings  (ver 2 --> active)

# prompt = "\nWhich topping would you like to add to your pizza:"
# prompt += "\n (Enter 'quit' if you are done!) "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         print("\n\tYour pizza will be done in a minute!")
#         active = False
#     else:
#         print(f"\n\tI'm adding {message}!")

# --------------------

# Pizza Toppings  (ver 3 --> conditional test)

# prompt = "\nWhich topping would you like to add to your pizza:"
# prompt += "\n (Enter 'quit' if you are done!) "

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message == 'quit':
#         print("\n\tYour pizza will be done in a minute!")
#     else:
#         print(f"\n\tI'm adding {message}!")

# --------------------

# infinity loop (Fixing error)

# x = 1 

# while x < 5:
#     print(x) --------> common error 

# ----------------------------------------------------------------------------

# Using a while loop with Lists and Dictionaries 

# Moving Items from One List to Another 

# # Start with users that need to be verified,
# # and an empty list to hold confirmed users.
# unconfirmed_users = ['alice', 'brian', 'candance']
# confirmed_users = []

# # Verify each user until there are no more unconfirmed users.
# #  Move each verified user into the list of confirmed users. 
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Display all confirmed users.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# ----------------------------------------------------------------------------

# Removing All Instances of Specific Values from a List 

# pets = ['dog', 'cat', 'fish', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# ----------------------------------------------------------------------------

# Filling a Dictionary with User Input 

# responses = {}

# # Set a flag to inicate that polling is active.
# polling_active = True 
# while polling_active:
#     # Prompt fro the person's name and respnse.
#     name = input("\nWhat is your name? ")
#     response = input("Which city would you like to visit someday? ")

#     # Store the response in a dictionary 
#     responses[name] = response 

#     # Find out if anyone else is going to take the poll.
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False

# # Polling is complete. Show the results.
# print("\n----- Poll Results -----")
# for name, response in responses.items():
#     print(f"{name} would like to visit {response}.")

# ----------------------------------------------------------------------------

# Exercises 

# Deli 

# sandwich_orders = ['chicken sandwich', 'tuna sandwich', 'egg sandwich', 'seafood sandwich']
# finished_sandwiches = []

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()

#     print(f"I made your {sandwich}.")
#     finished_sandwiches.append(sandwich)

# print("\nThe finished sandwiches are:")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

# -----------------

# No Pastrami 

# sandwich_orders = [
#     'chicken sandwich', 'pastrami sandwich', 'tuna sandwich', 'pastrami sandwich', 
#     'seafood sandwich', 'pastrami sandwich', 'egg sandwich'
# ]
# finished_sandwiches = []
# print("The deli has run out of pastrami sandwich!")

# while sandwich_orders:
#     while 'pastrami sandwich' in sandwich_orders:
#         sandwich_orders.remove('pastrami sandwich')

#     sandwich = sandwich_orders.pop()
#     print(f"I made your {sandwich}.")
#     finished_sandwiches.append(sandwich)

# print("\nThe finished sandwiches are:")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())


# -----------------

# Dream vacation 

# dream_vacation = {}

# while True:
#     name = input("\nWhat is your name? ")
#     place = input("If you could visit one place in the world, where would you go? ")

#     dream_vacation[name] = place

#     repeat = input("\nWould you like to let another person response? (yes/ no) ")
#     if repeat == 'no':
#         break

# print("--- Poll Result ---")
# for name, place in dream_vacation.items():
#     print(f"{name} would like to visit {place}.")

