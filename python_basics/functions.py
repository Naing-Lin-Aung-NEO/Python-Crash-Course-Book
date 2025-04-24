# Function 

# Defining a Function 

# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")

# greet_user()


# Passing Information to a Function 

# def greet_user(username):
#     """Display a simple greeting by name."""
#     print(f"Hello, {username.title()}!")

# greet_user('neo')
# greet_user('lin')


# Arguments and Parameters 

# -----------------------------------------------------------------------------

# Exercises 

# 8.1 Messages 

# def display_message():
#     """Dispaly what I am learning in this chapter."""
#     print("I'm learning how to work with functions in this chapter.")

# display_message()


# 8.2 Favorite Book 

# def favorite_book(title):
#     """Display my favorite name."""
#     print(f"One of my favorite books is {title}.")

# favorite_book("Cinderella")

# -----------------------------------------------------------------------------

# Passing Arguments 

# Positional Arguments , Multiple Function call

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'whillie')


# Order Matters in Positional Arguments

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('harry', 'hamster')


# Keyword Arguments 

# def describe_pet(animal_type, pet_name):
#     """Describe information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='harry')

# describe_pet(pet_name='harry', animal_type='hamster')


# Default Values 

# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='whillie')

# describe_pet(pet_name='harry', animal_type='hamster')


# Equivalent Function Calls 

# A dog named Whillie 
# describe_pet('whillie')
# describe_pet(pet_name='whillie')

# A hamster named Harry 
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')


# Avoiding Arguments Errors 

# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet()

# -----------------------------------------------------------------------------

# Exercises 

# 8.3 T-shirt

# def make_shirt(size, message):
#     """Making a different size shirt with customize message."""
#     print(f"\nI've made a {size.upper()}-size shirt with this text:")
#     print(f"\t{message.title()}")

# make_shirt('m', 'i love you')
# make_shirt(size='xl', message='i hate you')


# 8.3 Large Shirts 

# def make_shirt(message="I Love Python", size='large'):
#     """Making a large size shirt with customize message."""
#     print(f"\nI've made a {size} size shirt with this text:")
#     print(f"\t{message.title()}")

# make_shirt()
# make_shirt(size="medium")
# make_shirt(message="I Hate You", size='small')


# 8.4 Cities

# def describe_city(city, country="Myanmar"):
#     """Display city and its country."""
#     print(f"{city.title()} is in {country.title()}.")

# describe_city("Yangon")
# describe_city(city="New York", country="United states")
# describe_city(city='bangkok', country='thailand')

# -----------------------------------------------------------------------------

# Return Values 

# Returning a Simple Value 

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     fullname = f"{first_name} {last_name}"
#     return fullname.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# Making an Argument Optional

# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     fullname = f"{first_name} {middle_name} {last_name}"
#     return fullname.title()

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)


# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         fullname = f"{first_name} {middle_name} {last_name}"
#     else:
#         fullname = f"{first_name} {last_name}"
#     return fullname.title()

# musician = get_formatted_name(first_name='naing', last_name='aung')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# Returning a Dictionary 

# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('jimi', 'hendrix')
# print(musician)


# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)


# Using a Function with a while Loop 

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     fullname = f"{first_name} {last_name}"
#     return fullname.title()

# # This is an infinite loop.
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
    
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     fullname = f"{first_name} {last_name}"
#     return fullname.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(Enter 'q' at any time to quit!)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
    
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# -----------------------------------------------------------------------------

# Exercises

# 8.6 City Names 

# def city_country(city, country):
#     """Return a neatly formatted name."""
#     full_name = f'"{city}, {country}"'
#     return full_name.title()

# name = city_country('mandalay', 'myanmar')
# print(name)

# name = city_country('bangkok', 'thailand')
# print(name)


# 8.7 Album

# def make_album(artist, title, songs=None):
#     """Return a dictionary about info of music album."""
#     album = {'artist': artist, 'title': title}
#     if songs:
#         album['songs'] = songs

#     return album

# album = make_album('neo', 'love')
# print(album)

# album = make_album('lin', 'hate')
# print(album)

# album = make_album('aung', 'why?', songs=7)
# print(album)

# 8.8 User Albums 

def make_album(artist, title):
    """Return a dictionary about info of music album."""
    album = {'artist': artist, 'title': title}
    return album

while True:
    print("\nTell me an artist name and album title:")
    print("(Enter 'q' at any time to quit!)")

    artist = input('Artist: ')
    if artist == 'q':
        break

    title = input('Title: ')
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)

# -----------------------------------------------------------------------------

