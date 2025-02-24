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