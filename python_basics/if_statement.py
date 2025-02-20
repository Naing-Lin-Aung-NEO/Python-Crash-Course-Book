# cars = ['audi', 'bmw', 'mercedes', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
    
# requested_topping = 'mushrooms'

# if requested_topping != 'chilles':
#     print("Hold the chilles!")

# answer = 15 

# if answer != 18:
#     print("This is not the correct answer.Plz try again!")

# banned_users = ['ni ni', 'ki ki', 'chi chi', 'li li']
# user = 'mary'

# if user not in banned_users:
#     print(f"{user.title()}, you can post a response you wish.")

# -----------------------------------------------------------------

# Exercise 

# car = 'audi'

# if car != 'ferria':
#     print("I predict False")
# print(f"{car.title()} is true!")

# car = 'subaru'
# if car == 'subaru':
#     print(f"\nI predict true!, The cars is {car.title()}.")

# name = 'neo'
# if name != 'li li':
#     print(f"\nI predict false! The name is {name.upper()}.")

# animal = 'bee'
# if animal == 'bee':
#     print(f"\nI predict true. The anmial is {animal.title()}.")

# student = 'james'
# if student != 'neo':
#     print(f"\nI predict false, The student is {student.title()}.")

# car = 'lambo'
# if car == 'lambo':
#     print('\nGo buy it now!')

# car = 'bmw'
# if car != 'lambo':
#     print("Don't buy it!")

# car = 'Audi'
# if car.lower() == 'audi':
#     print("True")

# num = 10

# if num == 10:
#     print("Yes,num is 10!")

# if num != 11:
#     print("No, num is not 11, it's 10!")

# if num > 5:
#     print("Yes, num is greater than 5")

# if num >= 10:
#     print("yes! num is 10!")

# if num < 11:
#     print("No, it's true! num is less than 11!")

# if num <= 19:
#     print("No,it's true! num is less than 19!")

# if num == 10 and num < 19:
#     print("True")

# if num < 9 or num == 11:
#     print("False")

# cars = ['audi', 'mercedes', 'volk', 'lambo']
# car = 'Tesla'

# if car not in cars:
#     print("Don't Go to the market!")

# car = 'audi'
# if car in cars:
#     print("Let's go and buy it!")


# -----------------------------------------------------------------

# Simple if statement 

# age = 19
# if age >= 18:
#     print(f"You are {age} years old now, you're old enough to vote!")
#     print("Have you registered to vote yet?")

# -----------------------------------------------------------------

# if-else statement 

# age = 17
# if age >= 18:
#     print(f"You are {age} years old now, you're old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("You are too young to vote!")
#     print("Please register to vote as soon as you turn 18!")

# -----------------------------------------------------------------

# if-elif-else statements

# age = 12

# if age < 4:
#     print("Your admission cost is 0$.")
# elif age < 18:
#     print("Your admission cost is 25$")
# else:
#     print("Your admission cost is 45$.")

# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 45

# print(f"Your admission cost is ${price}.")

# age = 80 

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20

# print(f"Your admission cost is ${price}.")

# age = 70 

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age >= 65:
#     price = 20

# print(f"Your admission cost is ${price}")

# Testing Multiple Conditions 

requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")

# ----------------------------------------------------------------------------------------------------------------------------------

# Exercise 

alien_color = 'green'

# if alien_color == 'green':
    # print("You earend 5 points!") 
    # passed

# if alien_color == 'yellow':
#     print("You earned 7 points!") 
#     fialed

# -------

alien_color = 'red'

# if alien_color == 'green':
#     print("You earned 5 points!")
# else:
#     print("You earned 10 points!")
#     else - passed

# if alien_color == 'red':
#     print("You earned 5 points!")
# else:
#     print("You earned 10 points!") 
#     if - passed

# -----

alien_color = 'yellow'

# if alien_color == 'green':
#     print("You earned 5 points!")
# elif alien_color == 'yellow':
#     print("You earned 10 points!")
# elif alien_color == 'red':
#     print("You earned 15 points!")


alien_color = 'red'

# if alien_color == 'green':
#     score = 5
# elif alien_color == 'yellow':
#     score = 10
# elif alien_color == 'red':
#     score = 15 

# print(f"You earned {score} points!")

# --------

# age = 18 

# if age < 2:
#     stage = 'a baby'
# elif age < 4:
#     stage = 'a toddler'
# elif age < 13:
#     stage = 'a kid'
# elif age < 20:
#     stage = 'a teenager'
# elif age < 65:
#     stage = 'an adult'
# elif age >= 65:
#     stage = 'an elder'

# print(f"The person is {stage}.")

# ------------------

# fav_fruits = ['bananas', 'mangoes', 'grapes']

# if 'bananas' in fav_fruits:
#     print("I really like bananas!")

# if 'apples' in fav_fruits:
#     print("I really like apples!")

# if 'mangoes' in fav_fruits:
#     print("I really like mangoes!")

# if 'oranges' in fav_fruits:
#     print("I really like oranges!")

# if  'grapes' in fav_fruits:
#     print("I really like grapes!")

# print("\nFinished!")

# ------------------------------------------------------------------------------------------

# Using if Statement with Lists

# Checking for special item 

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print(f"Sorry, we are out of {requested_topping} right now.")
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")

#------------------------------------------------------------------------------------------

# Checking That a List is not Empty 

# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# ------------------------------------------------------------------------

# Using Multiple Lists

# available_toppings = ['mushrooms', 'olives', 'green peppers'
#                        'pepperoni' , 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we don't have {requested_topping}.")
# print("\nFinished making your pizza!")

# ------------------------------------------------------------------------

# Exercises

# names = ['ko ko', 'mg mg', 'neo', 'lwin lwin', 'aung aung']
# for name in names:
#     if name == 'neo':
#         print(f"Hello admin Neo, would you like to see a status report?")
#     else:
#         print(f"Hello {name.title()}, thank you for logging in again!")
        
#-----------------------

# users = []
# if users: 
#     for user in users:
#         print("Good job!")
# else:
#     print("We need to find some users!")

#-----------------------

# current_users = ['ko ko', 'mg mg', 'neo', 'lwin lwin', 'aung aung']
# new_users = ['neo', 'kyaw kyaw', 'ko ko', 'li li', 'aye aye']

# for new_user in new_users:
#     if new_user in current_users:
#         print(f"{new_user.title()} is not available, you will need to enter a new username!")
#     else:
#         print(f"{new_user.title()} is available!")

#-----------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in numbers:
#     if number == 1:
#         print("1st")
#     elif number == 2:
#         print("2nd")
#     elif number == 3:
#         print("3rd")
#     elif number == 4:
#         print("4th")
#     elif number == 5:
#         print("5th")
#     elif number == 6:
#         print("6th")
#     elif number == 7:
#         print("7th")
#     elif number == 8:
#         print("8th")
#     elif number == 9:
#         print("9th")

# print("\nFinished")

# ------------------------------------------------------------------------




