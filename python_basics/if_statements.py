# If Statements

# A Simple Example

cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())


# Conditional Tests

# Checking for Equality

# car = 'bmw'
# if car == 'bmw':
#     print("True")
# else:
#     print("False")


# car = 'audi'
# if car == 'bmw':
#     print("True")
# else:
#     print("False")


# Ignoring Case When Checking for Euqality

# car = 'Audi'
# if car == 'audi':
#     print("True")
# else:
#     print("False")


# car = 'Audi'
# if car.lower() == 'audi':
#     print(True)


# Checking for Ineuqality

# reuquested_toppiing = 'mushrooms'

# if reuquested_toppiing != 'anchovies':
#     print("Hold the achovies!")


# Numberical Comparisons

# age = 18
#     print(True)

# answer = 17
# if answer != 42:
#     print("That is not the correct answer. Please try again!")

# age = 19
# if age < 21:
#     print(True)

# if age <= 21:
#     print(True)

# if age > 21:
#     print(True)
# else:
#     print(False)

# if age >= 21:
#     print(True)
# else:
#     print(False)


# Checking Multiple Conditions

# Using and to Check Multiple Conditions

# age_0 = 22
# age_1 = 18
# if age_0 >= 21 and age_1 >= 21:
#     print(True)
# else:
#     print(False)

# age_1 = 22 
# if age_0 >= 21 and age_1 >= 21:
#     print(True)
# else:
#     print(False)


# Using or to Check Multiple Conditions

# age_0 = 22
# age_1 = 18

# if age_0 >= 21 or age_1 >= 21:
#     print(True)
# else:
#     print(False)

# age_0 = 18
# if age_0 >= 21 or age_1 >= 21:
#     print(True)
# else:
#     print(False)


# Checking Whether a Value Is in a List 

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# if 'mushrooms' in requested_toppings:
#     print(True)
# else:
#     print(False)

# if 'pepperoni' in requested_toppings:
#     print(True)
# else:
#     print(False)


# Checking Whether a Value Not Is in a List 

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish!")


# Boolean Expressions

# True
# False

# -----------------------------------------------------------------------------

# Exercises

# 5.1 Conditional Tests 

# car = 'subaru'

# if car == 'subaru':
#     print("I predict True!")

# if car == 'audi':
#     print("I predict False!")


# 5.2 More Conditional Tests 

# Equality
# car = 'bmw'
# if car == 'bmw':
#     print("You're correct!")
# else:
#     print(False)

# Ineuqality
# if car != 'audi':
#     print("You're wrong!")
# else:
#     print(False)

# lower() method 
# car = 'Audi'
# if car.lower() == 'audi':
#     print(True)
# else:
#     print(False)


# Numerical Tests 

# age = 18
# if age == 18:
#     print("You're approved!")
# else:
#     print("Go away!")

# age = 17
# if age != 18:
#     print("Go away!")
# else:
#     print("You're approved!")

# age = 20
# if age < 21:
#     print(True)
# else:
#     print(False)

# if age > 21:
#     print(True)
# else:
#     print(False)

# if age >= 18:
#     print(True)
# else:
#     print(False)

# if age <= 21:
#     print(True)
# else:
#     print(False)

# age_0 = 18
# age_1 = 21

# if age_0 < 20 and age_1 < 20:
#     print(True)
# else:
#     print(False)

# if age_0 < 20 or age_1 < 20:
#     print(True)
# else:
#     print(False)


# people = ['neo', 'lg', 'tv', 'crazy']
# person = 'lin'

# if person in people:
#     print("You are approved!")
# else:
#     print("You can't access to this area!")


# banned_people = ['neo', 'chou', 'ling']
# person = 'messi'

# if person not in banned_people:
#     print("You are not the wantend person!")
# else:
#     print("Come with me!")


# -----------------------------------------------------------------------------

# If Statement

# Simple if Statement

# age = 19
# if age >= 18:
#     print("You're old enough to vote!")
#     print("Have you registered to vote yet?")


# if-else Statement

# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")


# if-elif-else statement

# age = 12
# if age < 4:
#     print("Your admission cost is 0$.")
# elif age < 18:
#     print("Your admission cost is 25$.")
# else:
#     print("Your admission cost is 40$.")


# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40

# print(f"Your admission cost is {price}$.")


# Using Multiple elif Blocks

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20

# print(f"Your admission cost is {price}$.")


# Omitting the else Block 

# age = 12

# if age < 4:
#     price = 0 
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age >= 65:
#     price = 20 

# print(f"Your admission cost is {price}$.")


# Testing Multiple Conditions

# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms!")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni!")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese!")

# print("\nFinished Making Your Pizza!")

# -----------------------------------------------------------------------------

# Exercises

# 5.3 Alien Colors #1

# alien_color = 'green'

# if alien_color == 'green':
#     point = 5

# print(f"You just earned {point} points!")
# # pass 

# alien_color = 'yellow'

# if alien_color == 'green':
#     point = 5

# print(f"You just earned {point} points!")
# # fail


# 5.4 Alien Colors #2

# alien_color = 'green'

# if alien_color == 'green':
#     point = 5
# else:
#     point = 10

# print(f"You just earned {point} points!")

# # run if block 

# alien_color = 'yellow'

# if alien_color == 'green':
#     point = 5
# else:
#     point = 10

# print(f"You just earned {point} points!")

# #run else block 


# 5.5 Alien Colors #3

# alien_color = 'green'

# if alien_color == 'green':
#     point = 5
# elif alien_color == 'yellow':
#     point = 10
# elif alien_color == 'red':
#     point = 15

# print(f"You just earned {point} points!")
# # green 

# alien_color = 'yellow'

# if alien_color == 'green':
#     point = 5
# elif alien_color == 'yellow':
#     point = 10
# elif alien_color == 'red':
#     point = 15

# print(f"You just earned {point} points!")
# # yellow 

# alien_color = 'red'

# if alien_color == 'green':
#     point = 5
# elif alien_color == 'yellow':
#     point = 10
# elif alien_color == 'red':
#     point = 15

# print(f"You just earned {point} points!")
# # red 


# 5.6 Stages of Life 

# age = 50

# if age < 2:
#     stage = 'baby'
# elif age < 4:
#     stage = 'toddler'
# elif age < 13:
#     stage = 'kid'
# elif age < 20:
#     stage = 'teenager'
# elif age < 65:
#     stage = 'adult'
# elif age >= 65:
#     stage = 'elder'

# if stage == 'adult' or stage == 'elder':
#     print(f"You are an {stage}!")
# else:
#     print(f"You are a {stage}!")


# 5.7 Favorite Fruit

# fav_fruits = ['banana', 'grape', 'apple']

# if 'banana' in fav_fruits:
#     print("You really like bananas!")
# if 'orange' in fav_fruits:
#     print("You really like oranges!")
# if 'apple' in fav_fruits:
#     print("You really like apples!")
# if 'grape' in fav_fruits:
#     print("You really like grapes!")
# if 'lime' in fav_fruits:
#     print("You really like limes!")

# -----------------------------------------------------------------------------

# Using if Statement with Lists

# Checking for Special Items 

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")


# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now!")
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")


# Checking That a List Is Not Empty

# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
# else:
#     print("Are you sure you want a plain pizza?")


# Using Multiple Lists

# available_topping = ['mushrooms', 'olives', 'green peppers',
#                      'pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_topping:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we are out of {requested_topping}.")

# print("\nFinished making your pizza!")

# -----------------------------------------------------------------------------

# Exercises

# 5.8 Hello Admin 

# users = ['neo', 'lin', 'aung', 'jhon', 'admin', 'eun']

# for user in users:
#     if user == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {user.title()}, thank you for logging in again!")


# 5.9 No Users 

# users = ['neo', 'lin', 'aung', 'jhon', 'admin', 'eun']
# users = []

# if users:
#     for user in users:
#         if user == 'admin':
#             print("Hello admin, would you like to see status report?")
#         else:
#             print(f"Hello {user.title()}, thank you for logging in again!")
# else:
#     print("We need to find some users!")


# 5.10 Checking Usernames

# current_users = ['neo', 'lin', 'aung', 'jhon', 'eun']
# new_users = ['Lin', 'boy', 'tang', 'Neo', 'eun', 'yin']


# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print("You will need to enter a new username!")
#     else:
#         print("The username is available!")


# 5.11 Ordinal Numbers

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in numbers:
#     if number == 1:
#         print("First\n")
#     elif number == 2:
#         print("Second\n")
#     elif number == 3:
#         print("Third\n")
#     elif number == 4:
#         print("Fourth\n")
#     elif number == 5:
#         print("Fifth\n")
#     elif number == 6:
#         print("Sixth\n")
#     elif number == 7:
#         print("Seventh\n")
#     elif number == 8:
#         print("Eighth\n")
#     elif number == 9:
#         print("Ninth\n")

# Styling Your if Statements


# -----------------------------------------------------------------------------

# Exercises

# 5.12 Styling if Statement

# 5.13 Your Ideas

# Calculator

# -----------------------------------------------------------------------------

