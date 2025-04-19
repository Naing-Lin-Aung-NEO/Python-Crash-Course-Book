# DICTONARIES

# A Simple Dictionary 

# alien_0 = {'color': 'green', 'points' : 5}

# print(alien_0['color'])
# print(alien_0['points'])


# Working with Dictionaries


# Accessing Values in a Dictionary

# alien_0 = {'color': 'green'}
# print(alien_0['color'])


# alien_0 = {'color': 'green', 'points': 5}

# new_points = alien_0['points']
# print(f"You've just earned {new_points} points!")


# Adding New Key-Value Pairs 

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# Starting with Empty Dictionary

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)


# Modifying Values in a Dictionary

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'green'
# print(f"The alien color is {alien_0['color']} now.")


# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original x-position: {alien_0['x_position']}")

# # Move the alien to the right 
# # Determine how far to move the alien based on its curren speed

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien 
#     x_increment = 3

# # The new position is the old position plus the increment 
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New x-position: {alien_0['x_position']}")


# Removing Key-Value Pairs

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)


# A Dictionary of Similar Objects 

# fav_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# language = fav_languages['sarah'].title()
# print(f"Sarah's fav language is {language}.")

# language = fav_languages['jen'].title()
# print(f"Jen's fav language is {language}.")


# Using get() to Access Values 

# alien_0 = {'color': 'green', 'speed': 'slow'}
# # print(alien_0['points']) -> error 

# points = alien_0.get('points', 'No point value assigend')
# print(points)


# -----------------------------------------------------------------------------

# Exercises

# 6.1 Person 

# friend = {
#     'first_name': 'thaku',
#     'last name': 'khin',
#     'age': 22,
#     'city': 'taungyi',
# }

# print(friend['first_name'])
# print(friend['last name'])
# print(friend['age'])
# print(friend['city'])

# print(f"My friend name is {friend['first_name'].title()} {friend['last name'].title()}. She is\
#  {friend['age']} years old girl and lives in {friend['city'].title()}.")


# 6.2 Favorite Number 

# fav_numbers = {
#     'jen': 10,
#     'neo': 7,
#     'leo': 1,
#     'khin': 3,
#     'aung': 4,
# }

# print(f"Aung's favorite number is {fav_numbers['aung']}.")
# print(f"Jen's favorite number is {fav_numbers['jen']}.")
# print(f"Neo's favorite number is {fav_numbers['neo']}.")
# print(f"Khin's favorite number is {fav_numbers['khin']}.")
# print(f"Leo's favorite number is {fav_numbers['leo']}.")


# 6.3 Glossary 

# glossary = {
#     'print()': 'print the text',
#     'get()': 'to avoid error while calling value through its key',
#     'sum()': 'to add all the numbers in a list',
#     'range()': 'to generate a series of numbers',
#     'dictionary': 'a collection of key-vale pairs',
# }

# print(f"print(): {glossary['print()']}")
# print(f"\nget(): {glossary['get()']}")
# print(f"\nsum(): {glossary['sum()']}")
# print(f"\nrange(): {glossary['range()']}")
# print(f"\ndictionary: {glossary['dictionary']}")

# -----------------------------------------------------------------------------

# Looping Through a Dictionary


# Looping Through All Key-Value Pairs 

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")


# Looping Through All the Keys in a Dictionary 

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name in favorite_languages.keys():
#     print(name.title())

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}.")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")


# Looping Through a Dictionar's Keys in a Particular Order 

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")


# Looping Through All Values in a Dictionary


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# print("The following languages have been  mentioned:")
# for language in favorite_languages.values():
#     print(language.title())



# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())


# -----------------------------------------------------------------------------

# Exercises

# 6.4 Glossary 2

# glossary = {
#     'print()': 'print the text',
#     'get()': 'to avoid error while calling value through its key',
#     'sum()': 'to add all the numbers in a list',
#     'range()': 'to generate a series of numbers',
#     'dictionary': 'a collection of key-vale pairs',
#     'set()': 'to remove duplicate elements in a dictionary or a list',
#     'sorted()': 'to sort alphabatically the elements',
#     'keys()': 'returns keys from dictionary',
#     'values()': 'returns values from dictionary', 
#     'items()': 'returns key-values pairs from dictionary',
# }

# for word, meaning in sorted(glossary.items()):
#     print(f"{word}: {meaning}")



# 6.5 Rivers 

# rivers = {
#     'nile': 'egypt',
#     'amazon': 'brazil',
#     'yangtze': 'china',
#     'mississippi': 'united states',
#     'ayeyarwady': 'myanmar',
# }

# for river, country in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}.")

# for river in rivers.keys():
#     print(river.title())

# for country in rivers.values():
#     print(country.title())


# 6.6 Polling 

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# people = ['jen', 'edward', 'neo', 'tim', 'phil']

# for person in people:
#     if person in favorite_languages.keys():
#         print(f"Hi, {person.title()}, thank you for taking the poll!")
#     else:
#         print(f"Hi {person.title()}, take the poll please!")

# -----------------------------------------------------------------------------

