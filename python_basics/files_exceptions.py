# Reading from a File 

from pathlib import Path

path = Path('/home/user/Desktop/python/python_work/python_basics/pi.txt')
contents = path.read_text().rstrip()
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


from pathlib import Path 

path = Path('/home/user/Desktop/python/python_work/python_basics/learning_py.txt')
contents = path.read_text()
# print(contents)

lines = contents.splitlines()
for line in lines:
    c_lan = line.replace('Python', 'C')
    print(c_lan)

# -----------

# Simpler Code 

from pathlib import Path 

path = Path('/home/user/Desktop/python/python_work/python_basics/learning_py.txt')
contents = path.read_text()
# print(contents)

for line in contents.splitlines():
    print(line)