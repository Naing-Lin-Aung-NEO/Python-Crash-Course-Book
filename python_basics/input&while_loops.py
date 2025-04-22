# User Input And While Loops

# How the input() Function Works

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# Writing Clear Prompts 

# name = input("Please enter your name: ")
# print(f"Hello, {name}!")

# prompt = "If you share your name, we can personalize the messages your see."
# prompt += "\nWhat is your first name?"

# name = input(prompt)
# print(f"\nHello, {name}!")


# Using int() Accept Numerical Input 

# age = input("How old are you? ")
# if age < 18:
#     print("Hello") ---> error 

# height = input("How tall are you in, inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou are tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")


# The Modulo Operator 

# number = input("Enter a number, I'll tell you if it's even or odd: ")
# number = int(number)

# if (number % 2) == 0:
#     print(f"\nThe number {number} is even!")
# else:
#     print(f"\nThe number {number} is odd!")

# -----------------------------------------------------------------------------

# Exericses

# 7.1 Rental Car 

# car = input("Which car do you like to rent for the vacation? ")
# print(f"\nLet me see if I can find you a {car.title()}!")


# 7.2 Restaurant Seating

# people = input("How many people are in your group, Sir? ")
# people = int(people)

# if people < 8:
#     print("\nYour table is ready, Sir!")
# else:
#     print("\nYou'll have to wait for a table, Sir!")


# -----------------------------------------------------------------------------

# Introducing while Loops 


# The while Loop in Action 

# current_number = 1

# while current_number <= 5:
#     print(current_number)
#     current_number += 1


# Letting the User Choose when to quit

# prompt = "\nTell me something, and I will repeat if back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)


# Using a Flag 


# prompt = "\nTell me something, and I will repeat if back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:

#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)


# Using break to Exit a Loop 

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit; when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")


# Using continue in a Loop 

# current_number = 0

# while current_number < 10:
#     current_number += 1
#     if current_number % 2 != 0:
#         continue

#     print(current_number)


# Avoiding Infinite Loops 


# -----------------------------------------------------------------------------

# 7.4 Pizza Toppings 

# prompt = "\nTell me which toppings do you want for your pizza?"
# prompt += "\n(Enter 'quit' to exit the program!) "

# while True:
#     toppings = input(prompt)
#     if toppings == 'quit':
#         break
#     else:
#         print(f"\nAdding {toppings.title()}!")


# 7.5 Movie Tickets 

# prompt = "How old are you? (Enter 'quit' to exit the program!) "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break 
    
#     age = int(age)
#     if age < 3:
#         price = 0 
#     elif age <= 12:
#         price = 10
#     elif age > 12:
#         price = 15

#     print(f"Your ticket costs ${price}!")


# 7.6 Three Exists 


# prompt = "How old are you? (Enter 'quit' to exit the program!) "
# active = True 

# while active:
#     age = input(prompt)
#     if age == 'quit':
#         active = False 
    
#     age = int(age)
#     if age < 3:
#         price = 0 
#     elif age <= 12:
#         price = 10
#     elif age > 12:
#         price = 15

#     print(f"Your ticket costs ${price}!")


# prompt = "How old are you? (Enter 'quit' to exit the program!) "
# age = ""

# while age != 'quit':
#     age = input(prompt)    
#     if age == 'quit':
#         continue

#     age = int(age)

#     if age < 3:
#         price = 0 
#     elif age <= 12:
#         price = 10
#     elif age > 12:
#         price = 15

#     print(f"Your ticket costs ${price}!")


# 7.7 Infinity 

# num = 0 
# while num  < 10:
#     print("I Love You!") ---> infinity error

# -----------------------------------------------------------------------------

# Using a while Loop with Lists and Dictionaries 

# Moving Items from One List to Another 


# # Start with users that need to be verified, 
# # and an empty list to hold confirmed users.

# unconfirmend_users = ['neo', 'lin', 'aung']
# confirmed_users = []

# # Verify each user until there are no more unconfirmed users 
# # Move each verified user into the list of confirmed users 
# while unconfirmend_users:
#     current_user = unconfirmend_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Display all confirmed users 
# print("\nThe following users have been confired:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# Removing All Instances of Specific Value from a List 

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)


# Filling a Dictionary with User Input 

# responses = {}
# # Set a flag to indicate the polling is active.
# polling_active = True

# while polling_active:
#     # Prompt for the person's name and repsons.
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")

#     # Store the response in the dictionary.
#     responses[name] = response

#     # Find out if anyone else is going to take the poll.
#     repeat = input("\nWould you like to let another person respond? (yes/no) ")
#     if repeat.lower() == 'no':
#         polling_active = False

# # Polling is complete. Show the results.
# print("\n---Poll Results---")
# for name,response in responses.items():
#     print(f"{name.title()} would like to climb {response.title()}.")

# -----------------------------------------------------------------------------

# Exercises

# 7.8 Deli 

# sandwich_orders = ['club sandwich', 'ham sandwich', 'grilled sandwich']
# finished_sandwich = []

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f"Making {sandwich.title()}!")
#     finished_sandwich.append(sandwich)

# print("\nThe finished sandwiches are:")
# for sandwich in finished_sandwich:
#     print(sandwich.title())


# 7.9 No Pastrami 

# sandwich_orders = ['club sandwich', 'pastrami sandwich', 'grilled sandwich',
#                     'pastrami sandwich', 'cheese sandwich', 'pastrami sandwich'
#                     ]
# finished_sandwich = []

# print("We are out of pastrami sandwich!")
# while 'pastrami sandwich' in sandwich_orders:
#     sandwich_orders.remove('pastrami sandwich')

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f"Making {sandwich.title()}!")
#     finished_sandwich.append(sandwich)

# print("\nThe finished sandwiches are:")
# for sandwich in finished_sandwich:
#     print(sandwich.title())


# 7.10 Dream Vacation

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("\nWould you like to let another person respond? (yes or no) ")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results---")
for name,place in responses.items():
    print(f"{name.title()}'s dream vacation is {place.title()}.")
