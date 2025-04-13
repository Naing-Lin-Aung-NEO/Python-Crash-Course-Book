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