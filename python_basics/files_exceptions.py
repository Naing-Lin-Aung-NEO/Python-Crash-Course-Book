# Reading from a File 

# from pathlib import Path

# path = Path('/home/user/Desktop/python/python_work/python_basics/pi.txt')
# contents = path.read_text().rstrip()
# print(contents)

# -----------------------------------------------------------------------------

# Accessing a File's Line

# from pathlib import Path 

# path = Path('/home/user/Desktop/python/python_work/python_basics/pi.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)

# -----------------------------------------------------------------------------

# Working with a File's content

# from pathlib import Path 

# path = Path('/home/user/Desktop/python/python_work/python_basics/pi.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()

# print(pi_string)
# print(len(pi_string))

# -----------------------------------------------------------------------------

# Large Files 

# from pathlib import Path 

# path = Path('/home/user/Desktop/python/python_work/python_basics/pi_million_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()

# print(pi_string[:5])
# print(len(pi_string))



# -----------------------------------------------------------------------------

# Is your birthday Contained in Pi?

# from pathlib import Path

# path = Path('/home/user/Desktop/python/python_work/python_basics/pi_million_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()

# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday doesn't appear in the first million digits of pi!")
    
# -----------------------------------------------------------------------------

# Exercises 

# Learning python 

# from pathlib import Path 

# path = Path('/home/user/Desktop/python/python_work/python_basics/learning_py.txt')
# contents = path.read_text()
# # print(contents)

# lines = contents.splitlines()
# for line in lines:
#     print(line)

# -----------

# Learning C 


# from pathlib import Path 

# path = Path('/home/user/Desktop/python/python_work/python_basics/learning_py.txt')
# contents = path.read_text()
# # print(contents)

# lines = contents.splitlines()
# for line in lines:
#     c_lan = line.replace('Python', 'C')
#     print(c_lan)

# -----------

# Simpler Code 

# from pathlib import Path 

# path = Path('/home/user/Desktop/python/python_work/python_basics/learning_py.txt')
# contents = path.read_text()
# # print(contents)

# for line in contents.splitlines():
#     print(line)

# Writing to a File 

# Writing a Single Line 

# from pathlib import Path 

# path = Path('/home/user/Desktop/python/python_crash_course/python_basics/programming.txt')
# path.write_text('I love programming.')

# # Writing Multiple Lines 

# contents = "I love programming.\n"
# contents += "I love creating new games.\n"
# contents += "I also love working with data.\n"

# path.write_text(contents)

# -----------------------------------------------------------------------------

# Exercises 
# Guest

# from pathlib import Path 

# path = Path('python_basics/guest.txt')
# guests = []


# while True:
#     print("\nEnter 'q' if you want to stop!")
#     guest_name = input('What is your name? ')

#     if guest_name == 'q':
#         break

#     guests.append(guest_name.title())

# all_guests = "The name of the guests are:\n"
# for guest in guests:
#     all_guests += f"{guest}\n"
    
# path.write_text(all_guests)

# -----------------------------------------------------------------------------


# Exception

# print(5/0) --> error traceback

# Using try-except Blocks 

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# Using Exception to Prevent Crashes

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_num = input("\nFirst number: ")
#     if first_num == 'q':
#         break

#     second_num = input("Second number: ")
#     if second_num == 'q':
#         break

    # answer = int(first_num) / int(second_num) --> if second num is 0, it's error 
    # print(answer) 

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_num = input("\nFirst number: ")
#     if first_num == 'q':
#         break

#     second_num = input("Second number: ")
#     if second_num == 'q':
#         break

#     try:
#         answer = int(first_num) / int(second_num)
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
#     else:
#         print(answer)

# -----------------------------------------------------------------------------

# Handling the FileNotFoundError Exception

# from pathlib import Path

# path = Path('alice.txt')
# content = path.read_text(encoding='utf-8')


# from pathlib import Path 

# path = Path('alice.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")



# from pathlib import Path 

# path = Path('alice.txt')
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} doesn't exist.")
# else:
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {path} has about {num_words} words.")


# -----------------------------------------------------------------------------

# Working with Multiple Files 

# from pathlib import Path 

# def count_words(path):
#     try:
#         contents = path.read_text(encoding='utf=8')
#     except FileNotFoundError:
#         print(f"The file {path} doens't exist.")
#     else:
#         num_words = len(contents.split())
#         print(f"The file {path} has {num_words} words.")

# # path = Path("alice.txt")
# # count_words(path)

# file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
#               'little_woman.txt']

# for file_name in file_names:
#     path = Path(file_name)
#     count_words(path)

# -----------------------------------------------------------------------------

# Failing Silently

# from pathlib import Path 

# def count_words(path):
#     try:
#         contents = path.read_text(encoding='utf=8')
#     except FileNotFoundError:
#         pass
#     else:
#         num_words = len(contents.split())
#         print(f"The file {path} has {num_words} words.")

# # path = Path("alice.txt")
# # count_words(path)

# file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
#               'little_woman.txt']

# for file_name in file_names:
#     path = Path(file_name)
#     count_words(path)

# Deciding Which Errors to Report

# You have to decide which Errors to let the user know and you have to be aware 
# that some kind of internal information can be in the message to user 

# -----------------------------------------------------------------------------

# Exercises 

# Addition 

# print("Give me two numbers, I'll give you the addition.")
# print("Enter 'q' to quit.")

# while True:
#     first_num = input("\nFirst number: ")
#     if first_num == 'q':
#         break

#     second_num = input("Second number: ")
#     if second_num == 'q':
#         break

#     try:
#         addition = int(first_num) + int(second_num)
#     except ValueError:
#         print("You can't add the text!")
#     else:
#         print(addition)

    
# -----------------------------------------------------------------------------

# Addition Calculator 

# use while loop 

# -----------------------------------------------------------------------------

# Cats & Dogs 

# from pathlib import Path 

# def content(path):
#     try:
#         contents = path.read_text(encoding='utf-8').splitlines()
#     except FileNotFoundError:
#         print(f"The file {path} doesn't exists.")
#     else:
#         print(contents)

# file_names = ['cats.txt', 'dogs.txt']
# for file_name in file_names:
#     path = Path(file_name)
#     content(path)

# -----------------------------------------------------------------------------

# Common Words 

# from pathlib import Path 

# path = Path('programming.txt')

# contents = path.read_text(encoding='utf-8').rstrip()
# love = contents.lower().count('love ')
# print(love)

# -----------------------------------------------------------------------------

# Storing Data 

# json.loads() & json.dumps()


# from pathlib import Path 
# import json

# numbers = [2, 3, 5, 7, 11, 13]

# path = Path('numbers.json')
# contents = json.dumps(numbers)
# path.write_text(contents)


# from pathlib import Path 
# import json 

# path = Path('numbers.json')
# contents = path.read_text()
# numbers = json.loads(contents)
# print(numbers)

# -----------------------------------------------------------------------------

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



from pathlib import Path
import json 

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)

    print(f"We'll remember you when you come back, {username}!")