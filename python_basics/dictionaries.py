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

# Nesting

# A List of Dictionaries 

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)


# # Make an empty list for storing aliens.
# aliens = []

# # Make 30 green aliens. 
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# # Show the first 5 aliens 
# for alien in aliens[:5]:
#     print(alien)

# print("....")

# # Show how many aliens have been created
# print(f"Total number of aliens: {len(aliens)}")



# # Make an empty list for storing aliens.
# aliens = []

# # Make 30 green aliens. 
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'medium'
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['points'] = 15
#         alien['speed'] = 'fast'

# # Show the first 5 aliens 
# for alien in aliens[:5]:
#     print(alien)

# print("....")

# # Show how many aliens have been created
# print(f"Total number of aliens: {len(aliens)}")


# # A List in a Dictionary 

# # Store information about a pizza being ordered
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# # Summarize the order 
# print(f"You ordered a {pizza['crust']}-crust pizza with the follwoing "
#       "toppings:")

# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# favorite_languages = {
#     'jen': ['python', 'rust'],
#     'sarah': ['c'],
#     'edward': ['rust', 'go'],
#     'phil': ['python', 'haskell']
# }

# for name,language in favorite_languages.items():
#     if len(language) == 1:
#         print(f"\n{name.title()}'s favorite language is:")
#     else:
#         print(f"\n{name.title()}'s favorite languages are:")

#     for lan in language:
#         print(f"\t{lan.title()}")
        

# A Dictionary in a Dictionary 

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princetion',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }

# for username, userinfo in users.items():
#     print(f"\nUsername: {username.title()}")
#     full_name = f"{userinfo['first']} {userinfo['last']}"
#     location = userinfo['location']

#     print(f"\tFull Name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

# -----------------------------------------------------------------------------

# Exercises 

# 6.7 People 

# friend_0 = {
#     'first_name': 'thaku',
#     'last_name': 'khin',
#     'age': 22,
#     'city': 'taungyi',
# }

# friend_1 = {
#     'first_name': 'neo',
#     'last_name': 'lin',
#     'age': 18,
#     'city': 'mandalay',
# }

# friend_2 = {
#     'first_name': 'aung',
#     'last_name': 'gyi',
#     'age': 30,
#     'city': 'yangon',
# }

# people = [friend_0, friend_1, friend_2]

# for person in people:
#     # print(person)
#     full_name = f"{person['first_name']} {person['last_name']}"

#     print(f"\nFull name: {full_name.title()}")
#     print(f"Age: {person['age']}")
#     print(f"City: {person['city'].title()}")


# 6.8 Pets 

# pet_0 = {
#     'type': 'cat',
#     'owner': 'neo',
# }

# pet_1 = {
#     'type': 'dog',
#     'owner': 'jame',
# }

# pet_2 = {
#     'type': 'bird',
#     'owner': 'lin',
# }

# pets = [pet_0, pet_1, pet_2]

# for pet in pets:
#     message = f"{pet['owner'].title()} has a {pet['type']}."
#     print(message)


# 6.9 Favorite Places 

# favorite_places = {
#     'neo': ['yangon', 'mandalay', 'kalaw'],
#     'jame': ['new york', 'bankok', 'singapore'],
#     'lin': ['texas', 'washinton', 'seoul'],
# }

# for name,places in favorite_places.items():
#     print(f"\n{name.title()}'s favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")


# 6.10 Favorite Numbers 

# fav_numbers = {
#     'jen': [1, 10, 91],
#     'neo': [7, 3, 11],
#     'leo': [100, 1 , 7],
#     'khin': [8, 2, 22],
#     'aung': [4, 45, 0],
# }

# for name,numbers in fav_numbers.items():
#     print(f"\n{name.title()}'s favorite numbers are:")
#     for number in numbers:
#         print(f"\t{number}")


# 6.11 Cities 

# cities = {
#     'yangon': {
#         'country': 'myanmar',
#         'population': 3,
#         'area': 598,
#     },
#     'mandalay': {
#         'country': 'myanmar',
#         'population': 1.5,
#         'area': 163,
#     },
#     'naypyidaw': {
#         'country': 'myanmar',
#         'population': 0.9,
#         'area': 7054,
#     },
# }

# for name,info in cities.items():
#     print(f"\nName: {name.title()}")
#     print(f"\tCountry: {info['country'].title()}")
#     print(f"\tPopulation: {info['population']} M")
#     print(f"\tArea: {info['area']} Km^2")


# 6.12 Extensions

# rivers = {
#     'nile': {
#         'country': 'egypt',
#         'length': '6650',
#         'wide': '8',
#     },
#     'amazon': {
#         'country': 'brazil',
#         'length': '6400',
#         'wide': '10',
#     },
#     'yangtze': {
#         'country': 'china',
#         'length': '6300',
#         'wide': '9',
#     },
# }

# for river,info in rivers.items():
#     print(f"\nRiver: {river.title()}")
#     print(f"\tCountry: {info['country'].title()}")
#     print(f"\tLength: {info['length']} Km")
#     print(f"\tWidth: {info['wide']} Km")