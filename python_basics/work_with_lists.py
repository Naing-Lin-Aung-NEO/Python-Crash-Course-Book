# Looping Through an Entire List 

magicians = ['nana', 'alice', 'harley']
# for magician in magicians:
#     print(magician)

# for magician in magicians:
#     print(f'{magician.title()}, that was a great trick!')
#     print(f"I can't wait to see your next trick, {magician.title()}\n")
# print("Thank you, everyone. That was agreat magic show!")

# Exercise

pizzas = ['greek pizza', 'italian pizza', 'cheese pizza']
# for pizza in pizzas:
#     # print(pizza.title())
#     print(f"I like {pizza.title()}\n")
# print('I really like pizza!')

animals = ['cat', 'dog', 'fish']
# for animal in animals:
#     # print(animal.title())
#     print(f'{animal.title()} would be make a great pet.')
# print("Any of these animals would make a great pet!")

# Making Numerical Lists 

# Using the range() Function 

# for value in range(1, 5):
#     print(value)

# for value in range(6):
#     print(value)

# Using range() to Make a List of Numbers 

# numbers = list(range(1, 6))
# print(numbers)

# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# odd_numbers = list(range(1, 11, 2))
# print(odd_numbers)

# squares = []
# for value in range(1, 11):
#     square = value ** 2 
#     squares.append(square)
# print(squares)

# Simple Statistic with a List of Number 

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# Advanced Level Making List 
# squares = [value **2 for value in range(1, 11)]
# print(squares)


# -------------------------------------------------------------------

# Exercise 

# for value in range(1, 21):
#     print(value)

# numbers = list(range(1, 1000001))
# print(numbers)
# for number in numbers:
#     print(number)

# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# odd_numbers = list(range(1, 21, 2))
# print(odd_numbers)
# for odd_number in odd_numbers:
#     print(odd_number)

# multiples_of_3 = list(range(3, 31, 3))
# for multiple_of_3 in multiples_of_3:
#     print(multiple_of_3)

# cubes = []
# for value in range(1, 11):
#     cube = value ** 3 
#     print(cube)

# cubes = [value ** 3 for value in range(1, 11)]
# for cube in cubes:
#     print(cube)

# ------------------------------------------------------------------- 

# Working with Part of a List 

# Slicing a List

players = ['ni ni', 'chi chi', 'li li', 'pi pi', 'ti ti', 'nyi nyi']
# print(players[0:3])

# print(players[1:4])

# print(players[:4])

# print(players[1:])

# print(players[-1: ])

# Looping Through a Slice 
# players = ['ni ni', 'chi chi', 'li li', 'pi pi', 'ti ti', 'nyi nyi']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

# Copying A List 

# my_foods = ['cake', 'sweet', 'pizza']
# friend_foods = my_foods[:]

# my_foods.append('waffer')
# friend_foods.append('rice')

# print('My favorite foods are:')
# for my_food in my_foods:
#     print(my_food.title())

# print("\nMy friend's favorite foods are:")
# for friend_food in friend_foods:
#     print(friend_food.title())

# -----------------------------------------------------------------

# Exercise 

# student_names = ['ni ni', 'thi thi', 'mi mi', 'aung aung', 'kyaw kyaw', 'mg mg', 'nyi nyi']
# print("The First three students in the list are:")
# for student_name in student_names[:3]:
#     print(student_name.title())

# print("\nThree students from the middle of the list are:")
# for student_name in student_names[2:5]:
#     print(student_name.title())

# print("\nThe last three students in the list are:")
# for student_name in student_names[-3:]:
#     print(student_name.title())

# my_pizzas = ['greek pizza', 'italian pizza', 'cheese pizza']
# friend_pizzas = my_pizzas[:]

# my_pizzas.append('meat pizza')
# friend_pizzas.append('veggie pizza')

# print("My favortie pizzas are:")
# for my_pizza in my_pizzas:
#     print(my_pizza.title())

# print("\nMy friend's favorite pizzas are:")
# for friend_pizza in friend_pizzas:
#     print(friend_pizza.title())

# Tuple 

# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# Looping Thorugh All Value in a Tuple 

# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

# Writing Over a Tuple 

# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# ------------------------------------------------

# Exercise 

# buffet_items = ('salad', 'chicken','potatoe', 'pasta', 'bread')
# print("Five basic buffet items are:")
# for buffet_item in buffet_items:
#     print(buffet_item.title())

# # buffet_items[0] = 'duck' - Error 

# new_buffet_items = ('duck', 'soup', 'chicken', 'pasta', 'bread')
# print("\nNew five basic buffet itmes are:")
# for new_buffet_item in new_buffet_items:
#     print(new_buffet_item.title())