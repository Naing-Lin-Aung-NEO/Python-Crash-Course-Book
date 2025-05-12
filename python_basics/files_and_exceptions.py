# File And Exception 


# Reading from a File 

# Reading the Contents of a File 

# from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()
# print(contents)

# from pathlib import Path

# path = Path('pi_digits.txt')
# content = path.read_text().rstrip()
# print(content)


# Relative and Absolute File Paths 


# Accessing a File's Name 

# from pathlib import Path 

# path = Path('pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)


# Working with a File's Contents


# from pathlib import Path 

# path = Path('pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()

# print(pi_string)
# print(len(pi_string))


# Large Files: One Million Digits 


# from random import randint

# from pathlib import Path

# path = Path('pi_million_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''

# for line in lines:
#     pi_string += line.lstrip()


# print(f"{pi_string[:52]}")
# print(len(pi_string))


# Is Your Birthday Contained in Pi?

# from pathlib import Path 

# path = Path('pi_million_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

# -----------------------------------------------------------------------------

# Exercises 

# 10.1 Learning Python

# from pathlib import Path 

# path = Path('learning_python.txt')
# content = path.read_text()
# # print(content)

# lines = content.splitlines()
# string = ''
# for line in lines:
#     string += line

# print(string)


# 10.2 Learning C 

# from pathlib import Path 

# path = Path('learning_python.txt')
# content = path.read_text()
# content = content.replace('Python', 'C')

# lines = content.splitlines()
# string = ''
# for line in lines:
#     string += line 

# print(string)


# 10.3 Simpler Code 

# from pathlib import Path 

# path = Path('learning_python.txt')
# content = path.read_text()

# string = ''
# for line in content.splitlines():
#     string += line 

# print(string)

# -----------------------------------------------------------------------------

# Writing to a File 

# Writing a Single Line 


# from pathlib import Path 

# path = Path('programming.txt')
# path.write_text("I love programming.")


# Writing Multiple Lines 

# from pathlib import Path 

# contents = "I love programmig.\n"
# contents += "I love creating new games.\n"
# contents += "I also working with data.\n"

# path = Path('programming.txt')
# path.write_text(contents)


# -----------------------------------------------------------------------------

# Exercises 

# 10.4 Guest 

# from pathlib import Path

# name = input("What is your name?")
# path = Path('guest.txt')
# path.write_text(str(name))


# 10.5 Guest Book 

# from pathlib import Path

# names = ''
# name_qz = "\n(Enter 'q' at any time to quit!)"
# name_qz += "\nWhat is your name? "

# while True:
#     name_ans = input(name_qz)
#     if name_ans == 'q':
#         break
#     else:
#         names += f'{name_ans}\n'

# path = Path('guest_book.txt')
# path.write_text(names)

# -----------------------------------------------------------------------------

# Exception

# Handling the ZeroDivisionError Exception

# print(5/0) --> error 


# Using try-except Blocks 

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero.")


# Using Exception to Prevent Crashes / The else Bolck

# print("Give me two numbers, I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst Number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond Number: ")
#     if second_number == 'q':
#         break

#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero.")
#     else:
#         print(answer)

    
# Handling the FileNotFoundError Exception

# from pathlib import Path 

# path = Path('alice.txt')
# contents = path.read_text(encoding='utf-8') - error 


# from pathlib import Path

# path = Path('alice.txt')
# try:
#     contents = path.read_text(encoding='utf-8') 
# except FileNotFoundError:
#     print(f"Sorry, the file {path} doesn't exist.")


# Analyzing Text 

# from pathlib import Path 

# path = Path('physics.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} doesn't exist.")
# else:
#     # Count the approximate number of words in the file 
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {path} has about {num_words} words.")


# Working with Multiple Files 

# from pathlib import Path

# def count_words(path):
#     """Count the approximate number of words in a file."""
#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         print(f"Sorry, the file {path} doesn't exist.")
#     else:
#         # Count the approximate number of words in the file:
#         words = contents.split()
#         count_words = len(words)
#         print(f"The file {path} has about {count_words} words.")
    
# # path = Path('physics.txt')
# # count_words(path)

# files = ['alice.txt', 'programming.txt', 'physics.txt', 'chemistry.txt']
# for file in files:
#     path = Path(file)
#     count_words(path)


# Failing Silently 

# from pathlib import Path

# def count_words(path):
#     """Count the approximate number of words in a file."""
#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         pass
#     else:
#         # Count the approximate number of words in the file:
#         words = contents.split()
#         count_words = len(words)
#         print(f"The file {path} has about {count_words} words.")
    
# # path = Path('physics.txt')
# # count_words(path)

# files = ['alice.txt', 'programming.txt', 'physics.txt', 'chemistry.txt']
# for file in files:
#     path = Path(file)
#     count_words(path)

# Deciding Which Errors to Report 

# -----------------------------------------------------------------------------

# Exercises 

# 10.6 Addition 

# print("Give me two numbers, I'll add them.")

# first_number = input("\nFirst Number: ")
# second_number = input("\nSecond Number: ")

# try:
#     answer = int(first_number) + int(second_number)
# except ValueError:
#     print("You can't add the letters!")
# else:
#     print(answer)


# 10.7 Addition Calculator 

# print("Give me two numbers, I'll add them.")
# print("Enter 'q' at any time to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break

#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break

#     try:
#         answer = float(first_number) + float(second_number)
#     except ValueError:
#         print("You can't add the letters.")
#     else:
#         print(answer)


# 10.8 Cats and Dogs 

# from pathlib import Path 

# def animal_file(path):
#     """Read the files and print the contens to the screen."""
    
#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         print(f"The file {path} doesn't exist.")
#     else:
#         print(contents.lstrip())

# files = ['cats.txt', 'dogs.txt']
# for file in files:
#     path = Path(file)
#     animal_file(path)


# 10.9  Silent Cats and Dogs 

# from pathlib import Path 

# def animal_file(path):
#     """Read the files and print the contens to the screen."""
    
#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         pass
#     else:
#         print(contents.lstrip())

# files = ['cats.txt', 'dogs.txt']
# for file in files:
#     path = Path(file)
#     animal_file(path)


# 10.10 Common Words 

# from pathlib import Path 

# path = Path('physics.txt')
# contents = path.read_text(encoding='utf-8')
# count_the = contents.count('the ')
# print(count_the)

# -----------------------------------------------------------------------------

# Storing Data 

# Using json.dumps() and json.loads()

# from pathlib import Path
# import json

# numbers = [2, 3, 7, 11, 13]

# path = Path('numbers.json')
# contents = json.dumps(numbers)
# path.write_text(contents)


# from pathlib import Path
# import json 

# path = Path('numbers.json')
# contents = path.read_text()
# numbers = json.loads(contents)
# print(numbers)


# Saving and Reading User-Generated Data 

# from pathlib import Path 
# import json 

# username = input("What is your name? ")

# path = Path('username.json')
# contents = json.dumps(username)
# path.write_text(contents)

# print(f"We'll remember you when you come back, {username}!")


# from pathlib import Path 
# import json 

# path = Path('username.json')
# contents = path.read_text()
# username = json.loads(contents)

# print(f"Welcome back, {username}!")


# from pathlib import Path 
# import json 

# path = Path('username.json')
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Wlecome back, {username}!")
# else:
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")



# Refactoring 

# from pathlib import Path 
# import json 

# def greet_user():
#     """Greet the user by name."""

    # path = Path('username.json')
    # if path.exists():
    #     contents = path.read_text()
    #     username = json.loads(contents)
    #     print(f"Welcome back, {username}!")
    # else:
    #     username = input("What is your name? ")
    #     contents = json.dumps(username)
    #     path.write_text(contents)
    #     print(f"We'll remember you when you come back, {username}!")

# greet_user()


# from pathlib import Path 
# import json 

# def get_stored_username(path):
#     """Get stored username if available."""
#     contents = path.read_text()
#     username = json.loads(contents)
#     if username:
#         return username
#     else:
#         return None 
    
# def greet_user():
#     """Greet the user by name!"""
#     path = Path('username.json')
#     username = get_stored_username(path)
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")

# greet_user()



# from pathlib import Path 
# import json 

# def get_stored_username(path):
#     """Get stored username if available."""
#     contents = path.read_text()
#     username = json.loads(contents)
#     if username:
#         return username
#     else:
#         return None 
    

# def get_new_username(path):
#     """Prompt for a new username."""
#     username = input("What is your name? ")
#     contents= json.dumps(username)
#     path.write_text(contents)
#     return username
    
# def greet_user():
#     """Greet the user by name!"""
#     path = Path('username.json')
#     username = get_stored_username(path)
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = get_new_username(path)
#         print(f"We'll remember you when you come back, {username}!")

# greet_user()

# -----------------------------------------------------------------------------

# 10.11 Favorite Number 

# from pathlib import Path 
# import json 

# fav_number = input("What is your favorite number? ")

# path = Path('favorite_number.json')
# contents = json.dumps(fav_number)
# path.write_text(contents)

# from pathlib import Path 
# import json 

# path = Path('favorite_number.json')
# contents = path.read_text()
# fav_number = json.loads(contents)
# print(f"I know your favorite number! It's {fav_number}!")


# 10.12 Favorite Number Remembered 

# from pathlib import Path 
# import json 

# def favorite_number():
#     """Display favorite number."""

#     path = Path('favorite_number.json')
#     if path.exists():
#         contents = path.read_text()
#         fav_number = json.loads(contents)
#         print(f"I know your favorite number! It's {fav_number}!")
#     else:
#         fav_number = input("What is your favorite number? ")
#         contents = json.dumps(fav_number)
#         path.write_text(contents)
#         print(f"Wow! {fav_number} is lucky number.")

# favorite_number()


# 10.13 User Dictionary 

# from pathlib import Path 
# import json 

# def userinfo():
#     """Display userinfo: name, location and age."""
#     path = Path("username_two.json")
#     if path.exists():
#         contents = path.read_text()
#         userinfo = json.loads(contents)
#         for info, name in userinfo.items():
#             print(f"{info}: {name}")
#     else:
#         userinfo = {}
#         username = input("What is your name? ")
#         location = input("Where are you from? ")
#         age = input("How old are you? ")
#         userinfo['username'] = username
#         userinfo['location'] = location
#         userinfo['age'] = str(age) 
#         contents = json.dumps(userinfo)
#         path.write_text(contents)
#         for info, name in userinfo.items():
#             print(f"{info}: {name}")

# userinfo()


# 10.14 Verify User 

# from pathlib import Path 
# import json 

# def get_stored_userinfo(path):
#      """Get stored userinfo if available."""
#      if path.exists():
#           contents = path.read_text()
#           userinfo = json.loads(contents)
#           return userinfo
#      else:
#           return None    

# def get_new_userinfo(path):
#      """Prompt for a new user info."""
#      userinfo = {}   
#      username = input("What is your name? ")
#      location = input("Where are you from? ")
#      age = input("How old are you? ")
#      userinfo['username'] = username
#      userinfo['location'] = location
#      userinfo['age'] = str(age) 
#      contents = json.dumps(userinfo)
#      path.write_text(contents)
#      return userinfo


# def userinfo():
#     """Display userinfo: name, location and age."""
#     path = Path("username_two.json")
#     userinfo = get_stored_userinfo(path)
#     if userinfo:
#         username = input(f"Is your name {userinfo['username']}? (yes or no)")
#         if username.lower() == 'yes':
#             for info, name in userinfo.items():
#                 print(f"{info}: {name}")
#         else:
#             userinfo = get_new_userinfo(path)
#             for info, name in userinfo.items():
#                 print(f"{info}: {name}")
#     else:
#         userinfo = get_new_userinfo(path)
#         for info, name in userinfo.items():
#             print(f"{info}: {name}")

# userinfo()


# -----------------------------------------------------------------------------

