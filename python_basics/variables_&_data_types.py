# Variables

message = "Hello Python World!"
# print(message)

message = "Hello Python Crash Course World!"
# print(message)

# Avoiding Name Errors When Using Variables

message = "Hello Python Crash World!"
# print(mesage) ---> error 
# print(message) --> work

# Variables Are Labels

# -----------------------------------------------------------------------------
# Exercise

# 2.1 Simple Message 

message = "I Love You!"
# print(message)

# 2.2 Simple Messages 

message = "I Love Python!"
# print(message)

# -----------------------------------------------------------------------------

# Strings

# Changing Case in a String Methods

name = "ada lovelace"
# print(name.title())

name = "Ada Lovelace"
# print(name.upper())
# print(name.lower())

# -----------------------------------------------------------------------------

# Using Variables in String 

frist_name = "ada"
last_name = "lovelace"
fullname = f"{frist_name} {last_name}"
# print(fullname)
# print(f"Hello,{fullname.title()}")

message = f"Hello, {fullname.title()}"
# print(message)

# -----------------------------------------------------------------------------

# Adding Whitespace to String with Tabs of Newlines

# \t 
# print("Python")
# print("\tPython")

# \n 
# print("Languages:\nPython\nC\nJavaScript")

# \n\t 
# print("Languages:\n\tPython\n\tC\n\tJavaScript")

# -----------------------------------------------------------------------------

# Stripping Whitespcae

fav_language = 'python '
fav_language = fav_language.rstrip()
# print(fav_language)

fav_language = ' python'
fav_language = fav_language.lstrip()
# print(fav_language)

fav_language = ' python '
fav_language = fav_language.strip()
# print(fav_language)

# -----------------------------------------------------------------------------

# Removing Prefixes

nostarch_url = "https://nostarch.com"
simple_url = nostarch_url.removeprefix('https://')
# print(simple_url)

# -----------------------------------------------------------------------------

# Avoiding SyntaxError with String 

# -----------------------------------------------------------------------------

# Exercises

# 2.3 Personal Message 

name = "eric"
message = f"Hello {name.title()}, would you likke to learn some python today?"
# print(message)


# 2.4 Name Cases 

name = "naing lin aung"
# print(name.title())
# print(name.upper())
# print(name.lower())


# 2.5/2.6 Famous Quote

# author = "albert eistein"
# quote = "A person who never made a mistake never tried anything new."
# message = f'{author.title()} once said, "{quote}"'
# print(message)


# 2.7 Stripping Names 

name = " naing lin aung "
name = f"\n\t{name}"
# print(name)

# print(name.rstrip())
# print(name.lstrip())
# print(name.strip())


# 2.8 File Extensions

filename = 'python_notes.txt'
filename = filename.removesuffix('.txt')
# print(filename)