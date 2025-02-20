# A Simple Dictionary 

# aliien_0 = {'color': 'green', 'points': 5 }

# print(aliien_0['color'])
# print(aliien_0['points'])

# -------------------------------------------------------------

# Working with Dictionaries
# Accessing Values in a Dicitionary 

# aliien_0 = {'color': 'green'}
# print(aliien_0['color'])

# aliien_0 = {'color': 'green', 'points': 5 }

# new_points = aliien_0['points']
# print(f"You just earned {new_points} points!")

# -------------------------------------------------------------

# Adding New Key-Value Pairs 

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# -------------------------------------------------------------

# Starting with an Empty Dictionary 

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# Modifying Values in a Dictionary 

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is {alien_0['color']}.")

# ------

# ALien Speed 

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original Position: {alien_0['x_position']}")
# # alien_0['speed'] = 'fast'

# # Move alien to the right
# # Determine how far to move the alien based on its current speed

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien 
#     x_increment = 3

# # The new position is the old position plus the increment 
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New Position: {alien_0['x_position']}")

# -------------------------------------------------------------

# Removing Key-Value Pairs

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

# -------------------------------------------------------------

# A Dictionary of Similar Objects 

# favorite_languages ={
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phili': 'python',
# }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}")

# -------------------------------------------------------------

# Using get() to access Values 

# alien_0 = {'color': 'green', 'speed': 'slow'}
# # print(alien_0['point']) Error 

# point_value = alien_0.get('points', 'No point value assigned')
# print(point_value)

# -------------------------------------------------------------

# -------------------------------------------------------------
 
# Exercises 

# best_friend = {
#     'first_name': 'lin',
#     'middle_name': 'let',
#     'last_name': 'aung',
#     'city': 'yangon',
# }

# print(best_friend['first_name'].title())
# print(best_friend['middle_name'].title())
# print(best_friend['last_name'].title())
# print(best_friend['city'].title())

# -------------------------

# fav_numbers = {
#     'neo': '1',
#     'lin': '7',
#     'aung': '10',
#     'naing': '13',
#     'let': '20'
# }

# print(f"Neo's fav number is {fav_numbers['neo']}.")
# print(f"Lin's fav number is {fav_numbers['lin']}.")
# print(f"Aung's fav number is {fav_numbers['aung']}.")
# print(f"Naing's fav number is {fav_numbers['naing']}.")
# print(f"Let's fav number is {fav_numbers['let']}.")

# -------------------------

# glossary = {
#     'print': 'outputs data to the console',
#     'insert()': 'adds an element at a specified position in a list',
#     'append()': 'adds an element to the end of a list',
#     'del': 'deletes a specified element from a list (or variable)',
#     'remove()' : 'removes the first occurrence of a specified value from a list',
# }

# print(f"Print : {glossary['print'].capitalize()}")
# print(f"\nInsert() : {glossary['insert()'].capitalize()}")
# print(f"\nAppend() : {glossary['append()'].capitalize()}")
# print(f"\nDel : {glossary['del'].capitalize()}")
# print(f"\nRemove() : {glossary['remove()'].capitalize()}")


#---------------------------------------------------------------

# Looping through a Dictionary 

# user_0 ={
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print(f"\nKey : {key}")
#     print(f"Value : {value}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s fav language is {language.title()}.")

# ---------------------------------------------------

# Looping through All the keys in a Dictionary 

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name in favorite_languages:
#     print(name.title())

# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# ---------------------------------------------------

# Looping Through a Dictionary's Keys in a Particular Order

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name in sorted(favorite_languages.keys()):
    # print(f"{name.title()}, thank you for taking the poll!")

# ---------------------------------------------------

# Looping Through All the Values in a Dictionary 

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# for language in set(favorite_languages.values()):
#     print(language.title())

# ----------------------------------------------------------------------------

# Exercises 

# glossary = {
#     'print': 'outputs data to the console',
#     'insert()': 'adds an element at a specified position in a list',
#     'append()': 'adds an element to the end of a list',
#     'del': 'deletes a specified element from a list (or variable)',
#     'remove()' : 'removes the first occurrence of a specified value from a list',
# }

# for word, meaning in glossary.items():
#     print(f"{word}: {meaning}.")

# ------------------------------

# rivers = {
#     'nile': 'egypt',
#     'ayeyarwaddy': 'myanmar',
#     'amazon': 'brazil',
# }

# for river, country in rivers.items():
#     print(f"{river.title()} runs through {country.title()}.")

# for river in rivers.keys():
#     print(river.title())

# for country in rivers.values():
#     print(country.title())

# ------------------------------

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# friends = ['jen', 'neo', 'lewis', 'phil', 'lisa']
# for friend in friends:
#     if friend in favorite_languages.keys():
#         print(f"{friend.title()}, thank you for taking the poll!")
#     else:
#         print(f"{friend.title()}, you should take the poll!")

# ------------------------------

# Nesting 

# A List of Dictionary 

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# ------------

# # Make an empty list for storing aliens.
# aliens = []

# # Make 30 green aliens 
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# # Show the first five aliens 
# for alien in aliens[:5]:
#     print(alien)
# print("....")

# # Show how many aliens have been created.
# print(f"Total number of aliens : {len(aliens)}")

# ------------

# # Make an empty list for storing aliens.
# aliens = []

# # Make 30 green aliens 
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

# # Show the first five aliens 
# for alien in aliens[:5]:
#     print(alien)
# print("....")

# ------------------------------------------------------

# A list in a Dictionary 

# Store information about a pizza being ordered
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# # Summarize the order
# print(f"You ordered a {pizza['crust']}-crust pizza"
#       "with the follwoing toppings:")

# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# ------------

# favorite_languages = {
#     'jen': ['python', 'rust'],
#     'sarah': ['c'],
#     'edward': ['rust', 'go'],
#     'phil': ['python', 'haskell'],
# }

# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#         for language in languages:
#             print(f"{name.title()}'s favorite language is {language.title()}.")
#     else:
#         print(f"{name.title()}'s favorite languages are:")
#         for language in languages:
#             print(f"\t{language.title()}")

# ----------------------

# A Dictionary in a Dictionary 

# users = {
#     'aung': {
#         'first': 'naing',
#         'middle': 'lin',
#         'last': 'aung',
#         'location': 'mandalay',
#     },
#     'let': {
#         'first': 'lin',
#         'middle': 'let',
#         'last': 'aung',
#         'location': 'yangon',
#     },
# }

# for username, user_info in users.items():
#     print(f"Username: {username.title()}")
#     fullname = f"{user_info['first']} {user_info['middle']} {user_info['last']}"
#     location = user_info['location']

#     print(f"\tFull name: {fullname.title()}")
#     print(f"\tLocation: {location.title()}")


# users = {
#     'xiao': {
#         'first': 'xiao',
#         'last': 'zhan',
#         'location': 'china',
#     },
#     'yibo': {
#         'first': 'wang',
#         'last': 'yibo',
#         'location': 'china',
#     }
# }

# for username, user_info in users.items():
#     print(f"Username: {username.title()}")
#     fullname = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']

#     print(f"\tFullname: {fullname.title()}")
#     print(f"\tLocation: {location.title()}")

# --------------------------------------------

# Exercises


# people = [
#         {
#         'first_name': 'lin',
#         'middle_name': 'let',
#         'last_name': 'aung',
#         'city': 'yangon',
#     },
#         {
#         'first_name': 'naing',
#         'middle_name': 'lin',
#         'last_name': 'aung',
#         'city': 'mandalay',
#     },
#         {
#         'first_name': 'thin',
#         'middle_name': 'wottyi',
#         'last_name': 'phyo',
#         'city': 'mandalay',
#     },
# ]
# for person in people:
#     fullname = f"{person['first_name']} {person['middle_name']} {person['last_name']}"
#     location = person['city']

#     print(f"Fullname: {fullname.title()}")
#     print(f"Location: {location.title()}")

# ---------------

# pets = [
#     {
#         'name': 'superman',
#         'type': 'dog',
#         'owner': 'neo',
#     },
#     {
#         'name': 'hero',
#         'type': 'cat',
#         'owner': 'theo',
#     },
#     {
#         'name': 'cherry',
#         'type': 'fish',
#         'owner': 'alice',
#     },
# ]

# for pet in pets:
#     print(f"\nName: {pet['name'].title()}")
#     print(f"\tType: {pet['type'].title()}")
#     print(f"\tOwner: {pet['owner'].title()}")

# ---------------

# fav_places = {
#     'neo': {
#         'name': 'london',
#         'country': 'england',
#     },
#     'xiao': {
#         'name': 'beijing',
#         'country': 'china',
#     },
#     'theo': {
#         'name': 'new york',
#         'country': 'us'
#     }
# }

# for person, fav_place in fav_places.items():
#     place = fav_place['name']
#     country = fav_place['country']
#     if country == 'us':
#         print(f"{person.title()}'s favorite place is {place.title()} located in"
#               f" the {country.upper()}.")
#     else:
#         print(f"{person.title()}'s favorite place is {place.title()} located in"
#               f" {country.title()}.")
        
# ---------------

# fav_numbers = {
#     'neo': {
#         '1st': 31,
#         '2nd': 7,
#     },
#     'lin': {
#         '1st': 13,
#         '2nd': 20,
#     },
#     'aung': {
#         '1st': 10,
#         '2nd': 100,
#     },
#     'let': {
#         '1st': 23,
#         '2nd': 9,
#     },
# }
# for name, number in fav_numbers.items():
#     print(f"{name.title()}'s fav numbers are {number['1st']} and {number['2nd']}.")

# ---------------

# cities = {
#     'yangon': {
#         'country': 'myanmar',
#         'population': '5m',
#         'size' : 'largest',
#     },
#     'mandalay': {
#         'country': 'myanmar',
#         'population': '1m',
#         'size': 'second largest',
#     },
#     'naypyidaw': {
#         'country': 'myanmar',
#         'population': '758k',
#         'size': 'smallest',
#     },
# }

# for city, city_info in cities.items():
#     print(f"City: {city.title()}")
#     print(f"\tCountry: {city_info['country'].title()}")
#     print(f"\tPopulation: {city_info['population'].title()}")
#     print(f"\tSize: {city_info['size'].title()}")

# ---------------

# rivers = {
#     'nile': {
#         'length': '6650km',
#         'width': '2.8km',
#         'country': 'egypt',
#     },

#     'ayeyarwaddy': {
#         'length': '2170km',
#         'width': '800m',
#         'country': 'myanmar'        
#     },
#     'amazon': {
#         'length': '6400km',
#         'width': '50km',
#         'country': 'brazil',
#     },
# }

# for river, river_info in rivers.items():
#     print(f"Name: {river.title()}")
#     print(f"\tLength: {river_info['length'].title()}")
#     print(f"\tWidth: {river_info['width'].title()}")
#     print(f"\tCountry: {river_info['country'].title()}")

