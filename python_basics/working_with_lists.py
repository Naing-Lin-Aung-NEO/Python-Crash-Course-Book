# Working With Lists 

# Looping Through an Entire List 

# magicians = ['neo', 'xiao', 'david']
# for magician in magicians:
#     print(magician)


# Doing More Work Within a for Loop 

# magicians = ['neo', 'xiao', 'david']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")


# Doing Something After a for Loop 

# magicians = ['neo', 'xiao', 'david']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# print("Thank you, everyone. That was a great magic show!")


# Avoiding Indentation Errors 

# Forgetting to Indent 

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician) ---> error 


# Forgetting to Indent Additional Lines 

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
# print(f"I can't wait to see your next trick, {magician.title()}!") --> logical error 


# Indenting Unnecessarily

# message = "Hello Python World!"
#     print(message) --> error 


# Indenting Unnecessarily After the Loop 

# magicians = ['neo', 'xiao', 'david']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
#     print("Thank you, everyone. That was a great magic show!")


# Forgetting the Colon 

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians
#     print(magician)   --> error 


# -----------------------------------------------------------------------------

# Exercises 

# 4.1 Pizzas

# pizzas = ['new york style pizza', 'chicago pizza', 'sicilian pizza']
# for pizza in pizzas:
#     # print(pizza)
#     print(f"I like {pizza.title()}!")

# print("I really love pizza!")


# 4.2 Animals 

# animals = ['dog', 'cat', 'bird']
# for animal in animals:
#     # print(animal)
#     print(f"A {animal} would make a great pet!")

# print("Any of these animals would make a great pet!")

# -----------------------------------------------------------------------------

# Making Numerical Lists 

# Using the range() Function 

# for value in range(1,5):
#     print(value)

# for value in range(1,6):
#     print(value)

# for value in range(6):
#     print(value)


# Using range() to make a list of Numbers 

numbers = list(range(1,6))
# print(numbers)

even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)

# print(squares)


# squares = []
# for value in range(1,11):
#     squares.append(value ** 2)

# print(squares)


# Simple Statistics with a List of Numbers 

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))

# print(max(digits))

# print(sum(digits))


# List Comprehenisons 

# squares = [value**2 for value in range(1,11)]
# print(squares)

# -----------------------------------------------------------------------------

# Exercises 

# 4.3 Counting to Twenty 

# for number in range(1,21):
#     print(number)


# 4.4 One Million

# for number in range(1, 1000_001):
#     print(number)


# 4.5 Suming a Million 

# number = [num for num in range(1, 1000_001)]
# print(sum(number))


# 4.6 Odd Numbers 

# for number in range(1, 21, 2):
#     print(number)


# 4.7 Threes

# numbers = [num for num in range(3, 31, 3)]
# for number in numbers:
#     print(number)


# 4.8 Cubes 

# cubes = []
# for cube in range(1,11):
#     cubes.append(cube**3)

# # print(cubes)

# for cube in cubes:
#     print(cube)


# 4.9 Cube Conprehension

# cubes = [cube**3 for cube in range(1,11)]
# for cube in cubes:
#     print(cube)

# -----------------------------------------------------------------------------

# Working with Part of a List 

# Slicing a List 

players = ['no', 'yes', 'carl', 'harry', 'leo']
# print(players[0:3])

# print(players[1:4])

# print(players[:4])

# print(players[2:])

# print(players[-3:])

# Looping Through a Slice 

players = ['no', 'yes', 'carl', 'harry', 'leo']

# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())


# Copying a List 

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite food are:")
# print(friend_foods)


# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite food are:")
# print(friend_foods)



# my_foods = ['pizza', 'falafel', 'carrot cake']

# # This does not work!
# friend_foods = my_foods

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite food are:")
# print(friend_foods)


# -----------------------------------------------------------------------------


# Exercies

# 4.10 slices 

cubes = [cube**3 for cube in range(1,11)]
# for cube in cubes:
#     print(cube)

# print("Here is the first three values of the list:")
# for cube in cubes[:3]:
#     print(cube)

# print("\nHere is the three values from the middle of the list:")
# for cube in cubes[3:6]:
#     print(cube)

# print("\nHere is the last three values from the list:")
# for cube in cubes[-3:]:
#     print(cube)


# 4.11 My Pizzas, Your Pizzas

# my_pizzas = ['new york style pizza', 'chicago pizza', 'sicilian pizza']
# your_pizzas = my_pizzas[:]

# my_pizzas.append('myanmar pizza')
# your_pizzas.append('england pizza')

# print("My fvaorite pizzas are:")
# for pizza in my_pizzas:
#     print(pizza.title())

# print("\nYour favorite pizzas are:")
# for pizza in your_pizzas:
#     print(pizza.title())

# 4.12 More Loops 

# -----------------------------------------------------------------------------


