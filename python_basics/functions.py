# Defining a Function 

# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")

# greet_user()

# ---------------------------------------------------------------

# Passing Information to a Function 

# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello!, {username.title()}")

# greet_user('neo')

# ---------------------------------------------------------------

# Exercises 

# Message 

# def display_message():
#     print("In this chapter, we are learning about functions.")

# display_message()

# -----------------------

# Favorite Book

# def favorite_book(book):
#     print(f"One of my favorite books is {book.title()}.")

# favorite_book("alice in wonderland")

# ---------------------------------------------------------------

# Passing Arguments 

# Positional Arguments 

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')

# ---------------------------------------------------------------

# Multiple Function Calls

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'whillie')

# ---------------------------------------------------------------

# Order Matters in Positional Arguments

# def describe_pet(animal_type, pet_name):
#     """Display info about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('harry', 'hamster')

# ---------------------------------------------------------------

# Keyword Arguments 

# def describe_pet(animal_type, pet_name):
#     """Display info about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='harry')

# ---------------------------------------------------------------

# Default Values 

# def describe_pet(pet_name, animal_type='hamster'):
#     """Display info about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='harry')

# ---------------------------------------------------------------

# Equivalent Function Calls (all the forms are correct)

# A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')

# #A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

# ---------------------------------------------------------------

# Avoiding Argument Errors 

# def describe_pet(pet_name, animal_type):
#     """Display info about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet() ---> Error 

# ---------------------------------------------------------------

# Exercises 

# T-shirt

# def make_shirt(size, message):
#     print(f"\nI want {size} size T-shirt and '{message}' printed on it.")

# make_shirt('medium', 'I love you!')
# make_shirt(size='large', message='I hate you!')

# ----------------------

# Large Shirts

# def make_shirt(size, message='I love Python!'):
#     print(f"\nI want {size} size T-shirt and '{message}' printed on it.")

# make_shirt(size='large')
# make_shirt('medium')
# make_shirt(size='medium', message='x chin tal!')

# ----------------------

# Cities 

# def describe_city(name, country='myanmar'):
#     print(f"\n{name.title()} is in {country.title()}.")

# describe_city(name='yangon')
# describe_city('mandalay')
# describe_city(name='newyork', country='unite states of america')

# ---------------------------------------------------------------

# Return Values 

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     fullname = f"{first_name} {last_name}"
#     return fullname.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# ---------------------------------------------------------------

# Making an Argument Optional

# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     fullname = f"{first_name} {middle_name} {last_name}"
#     return fullname.title()

# musician = get_formatted_name('jimi', 'hendrix', 'hooker')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         fullname = f"{first_name} {middle_name} {last_name}"
#     else:
#         fullname = f"{first_name} {last_name}"
#     return fullname.title() 

# musician = get_formatted_name('jimi', 'hooker')
# print(musician)

# musician = get_formatted_name('jimi', 'hooker', 'lee')
# print(musician)

# ---------------------------------------------------------------

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

# musician = build_person('jimi', 'hendrix', age=25)
# print(musician)

# ---------------------------------------------------------------

# Using a function with while loop 

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# #This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# #This is not infinite loop
# while True:
#     print("\nPlease Tell me your name:")
#     print("(enter 'q' at any time to quit!)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"Hello, {formatted_name}!")

# ---------------------------------------------------------------

# Exercises 

# City Names 

# def city_country(city, country):
#     """Return city and country names."""
#     place = f"{city}, {country}"
#     return place.title()

# final_place = city_country('santiago', 'chile')
# print(final_place)

# final_place = city_country('yangon', 'myanmar')
# print(final_place)

# final_place = city_country('bankok', 'thailand')
# print(final_place)

# --------------------

# Album

# def make_album(artist, title, songs=None):
#     """Return a dictionary of information about an album."""
#     album = {'artist': artist, 'title': title}
#     if songs:
#         album['songs'] = songs
#     return album 

# final_album = make_album('neo', 'gangstar')
# print(final_album)


# final_album = make_album('jiji', 'frozen', 30)
# print(final_album)

# final_album = make_album('giga', 'done done')
# print(final_album)

# --------------------

# User Albums 

# def make_album(artist, title):
#     """Return a dictionary of information about an album."""
#     album = {'artist': artist, 'title': title}
#     return album 

# while True:
#     print("\nPlease Tell me your fav album:")
#     print("(enter 'q' at anytime to quit!)")
#     singer = input("Artist: ")
#     if singer == 'q':
#         break

#     album_title = input("Album Title: ")
#     if album_title == 'q':
#         break

#     final_album = make_album(singer, album_title)
#     print(final_album)

# ---------------------------------------------------------------

# Passing a List 

# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names: 
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# ---------------------------------------------------------------
# Modifying a List in a Function 

# # Start with some desgins that need to be printed 
# unprinted_desgins = ['phone case', 'robot pendant', 'dodecahedrom']
# completed_models = []

# # Simulate printing each design, util none are left 
# # Move each design to completed_models after printing 
# while unprinted_desgins:
#     current_desgin = unprinted_desgins.pop()
#     print(f"Printing design: {current_desgin}")
#     completed_models.append(current_desgin)

# # Diplay all completed models 
# print("\nThe following models are printed:")
# for completed_model in completed_models:
#     print(completed_model) ---> withoud a function 

# def print_models(unprinted_designs, completed_models):
#     """ Simulate printing each design, util none are left """
#     """Move each design to completed_models after printing """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing design: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Diplay all completed models """
#     print("\nThe follwoing models are printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_desgins = ['phone case', 'robot pendant', 'dodecahedrom']
# completed_models = []


# print_models(unprinted_desgins, completed_models)
# show_completed_models(completed_models)

# ---------------------------------------------------------------

# Preventing a Function from Modifying a List 

# def print_models(unprinted_designs_copy, completed_models):
#     """ Simulate printing each design, util none are left """
#     """Move each design to completed_models after printing """
#     while unprinted_designs_copy:
#         current_design = unprinted_designs_copy.pop()
#         print(f"Printing design: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Diplay all completed models """
#     print("\nThe follwoing models are printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_desgins = ['phone case', 'robot pendant', 'dodecahedrom']
# unprinted_desgins_copy = unprinted_desgins[:] ---> a copy 
# completed_models = []


# print_models(unprinted_desgins, completed_models)
# show_completed_models(completed_models)

# ---------------------------------------------------------------

# Exercises 

# Messages 

# def show_messages(msgs):
#     """Print short messages from the list."""
#     for msg in msgs:
#         messgae = msg.title()
#         print(messgae)

# messages = ['hello!', 'hi!', 'how are you?', 'good morning!']
# show_messages(messages)

# ------------------------

# Sending Messages 

# def sent_messages(messages, sent_msgs):
#     """Sent short messages from the list."""
#     """Move sent messages to sent_msgs list."""
#     while messages:
#         done_message = messages.pop()
#         print(done_message.title())
#         sent_msgs.append(done_message)

# messages = ['hello!', 'hi!', 'how are you?', 'good morning!']
# sent_msgs = []

# sent_messages(messages,sent_msgs)
# print(messages) ---> empty 
# print(sent_msgs) ---> full 

# ------------------------
# archived messages 

# def sent_messages(messages, sent_msgs):
#     """Sent short messages from the list."""
#     """Move sent messages to sent_msgs list."""
#     while messages:
#         done_message = messages.pop()
#         print(done_message.title())
#         sent_msgs.append(done_message)
        
        

# messages = ['hello!', 'hi!', 'how are you?', 'good morning!']
# messages_copy = messages[:]
# sent_msgs = []

# sent_messages(messages_copy,sent_msgs)
# print(messages)  
# # original full 
# print(messages_copy)
# # copy empty 

# ---------------------------------------------------------------

# Passing an Arbitrary Number of Arguments 

# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# ---------------------------------------------------------------

# Mixing Positinonal and Arbitrary Arguments 

# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nWe are making {size}-inch of pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# -------------------------------------------------------------------
# Using Aritrary Keyword Arguments 

# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everyting we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# userprofile = build_profile(
#     'albert', 'eistein',
#     location='princeton',
#     field='physics'
# )

# print(userprofile)

# -------------------------------------------------------------------

# Exercises 

# Sandwiches

# def make_sandwich(*items):
#     """Make a sandwich with the items."""
#     print("\nMaking a sandwich with the following items:")
#     for item in items:
#         print(f"- {item}")

# make_sandwich('cheese', 'chicken', 'tomato')
# make_sandwich('lattice', 'egg', 'beef')
# make_sandwich('pork', 'ham', 'meat ball')


# ----------------------

# User profiles 

# def build_profile(first, last, **my_info):
#     """Build a dictionary for me."""
#     my_info['first_name'] = first
#     my_info['last_name'] = last
#     return my_info

# my_profile = build_profile(
#     'naing', 'aung',
#     location='mandalay',
#     job='student',
#     income='$0'
# )

# print(my_profile)

# for key, value in my_profile.items():
#     print(f"My {key} is {value.title()}.")

# ----------------------
# Cars 

# def make_car(company, model, **car_info):
#     """Build a dictionary for the car."""
#     car_info['company'] = company
#     car_info['model'] = model
#     return car_info

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

# -------------------------------------------------------------------

# Storing Your Functions in Modules

# Importing an Entire Module

# Importing from module 1

# import module
# module.make_pizza(16, 'pepperoni')
# module.make_pizza(12, 'mushrooms', 'extr cheese')

# -------------------------------------------------------------------

# Importing Specific Functions

# - if you want to import specific functions, use this syntax 
#      from module import function
#      from module import function1, function2 (use comma to add more functions)
#      function() --> (don't need dot notation)

# -------------------------------------------------------------------

# Using as to Give a Function an Alias

# - if there is similar name for the function from module, use as statement to give nickname
#          from module import function as fn 
#          fn()

# -------------------------------------------------------------------

# Using as to Give a Module an Alias

# - if there is similar name of your module, use as statement to give nickname
#          import module as md 
#          md.function()

# -------------------------------------------------------------------

# Importing All Functions in a Module

# - if you don't want to use dot notation and want to use all function from a module
#   use this syntax 
#          from module import * 
# - don't recommend this syntax cuz you can cofuse with the others function from your program,
#   so, just import module and use dot notation to call function

# -------------------------------------------------------------------

# Styling a Functions

# - give descriptive name to function
# - write comment with docstring format in the next line of defining a function
# - if you specify a default value for parameter, don't use space on the both side 
#   (also keyword arguments)
# - if there's two function, use two lines to seprate 
# - follow PEP8 format and write only 79 characters each line 

# -------------------------------------------------------------------

# Exercises 

# Printing models & imports (module2)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedrom']
# completed_models = []

# import module 
# module.print_models(unprinted_desgins, completed_models)
# module.show_completed_models(completed_models)

# from module import print_models, show_completed_models
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# from module import print_models as pm, show_completed_models as scm
# pm(unprinted_designs, completed_models)
# scm(completed_models)

# import module as md 
# md.print_models(unprinted_designs, completed_models)
# md.show_completed_models(completed_models)

# from module import * 
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)