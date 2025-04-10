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