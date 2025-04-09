# Introducing Lists 

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)


# Accessing Elements in a List 

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0])
# print(bicycles[0].title())


# Index Positions Start at 0, Not 1 

# print(bicycles[0])
# print(bicycles[3])

# print(bicycles[-1])
# print(bicycles[-2])


# Using Individual Values from a List 

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = f"My frist bicycle is {bicycles[-1].title()}."

# print(message)

# -----------------------------------------------------------------------------

# Exercises 

# 3.1 Names 

names = ['neo', 'lin', 'aung', 'naing', 'let', 'xiao']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])


# 3.2 Greetings 

# names = ['neo', 'lin', 'aung', 'naing', 'let', 'xiao']
# print(f"Hello, {names[0].title()}!")
# print(f"Hello, {names[1].title()}!")
# print(f"Hello, {names[2].title()}!")
# print(f"Hello, {names[3].title()}!")
# print(f"Hello, {names[4].title()}!")
# print(f"Hello, {names[5].title()}!")


# 3.4 Your Own List 

cars = ['Vortex V8', 'Titan GT', 'Phantom XRS', 'Apex Fury', 'Inferno R1']
my_dream_car = f"My dream car is {cars[2]}!"

# print(my_dream_car)

# -----------------------------------------------------------------------------

# Modifying, Adding, and Removing Elements 

# Modifying Elements in a List 

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

motorcycles[0] = 'ducati'
# print(motorcycles)


# Adding Elements to a List 

# Appending Elements to the End of the List 

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

motorcycles.append('ducati')
# print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('ducati')

# print(motorcycles)


# Inserting Elements to a List 

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(1, 'ducati')
# print(motorcycles)


# Removing Elements from a List 

# Removing an Item Using the del Statement 

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

del motorcycles[0]
# print(motorcycles)

# Removing an Item using the pop() Method 

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)


last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")


# Popping Items from Any Position in a List 

motorcycles = ['honda', 'yamaha', 'suzuki']

first_motor = motorcycles.pop(1)
# print(f"My first owned motorcycle is {first_motor.title()}.")

# Removing an Item by Value 

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

motorcycles.remove('honda')
# print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"{too_expensive.title()} is too expensive for me!")

# -----------------------------------------------------------------------------

# Exercises 

# 3.4 Guest list 

names = ['lin let aung', 'naing lin aung', 'neo', 'xaio']

# print(f"Would you like to have a dinner with me, {names[0].title()}?")
# print(f"Would you like to have a dinner with me, {names[1].title()}?")
# print(f"Would you like to have a dinner with me, {names[2].title()}?")
# print(f"Would you like to have a dinner with me, {names[3].title()}?")

# 3.5 Changing Guest List 

names = ['lin let aung', 'naing lin aung', 'neo', 'xaio']

# print(f"{names[2].title()} can't come to the dinner!")
names[2] = 'aung'
# print(f"Would you like to have a dinner with me, {names[0].title()}?")
# print(f"Would you like to have a dinner with me, {names[1].title()}?")
# print(f"Would you like to have a dinner with me, {names[2].title()}?")
# print(f"Would you like to have a dinner with me, {names[3].title()}?")

# 3.6 More Guest 


# print("Hello, Ladies and Gentlemen! I've found a bigger dinner table.")

names.insert(0, 'shwe')
names.insert(2, 'ti')
names.insert(6, 'wat')

# print(f"Would you like to have a dinner with me, {names[0].title()}?")
# print(f"Would you like to have a dinner with me, {names[1].title()}?")
# print(f"Would you like to have a dinner with me, {names[2].title()}?")
# print(f"Would you like to have a dinner with me, {names[4].title()}?")
# print(f"Would you like to have a dinner with me, {names[5].title()}?")
# print(f"Would you like to have a dinner with me, {names[6].title()}?")

# print(f"I'm inviting the {len(names)} people for the dinner!")

# 3.7 Shrinking Guest List 

# print("Sorry, I can only invite 2 people for the dinner!")
# print(names)

# remove_guest = names.pop(0)
# print(f"I can't invite you to dinner,{remove_guest.title()}.")

# remove_guest = names.pop(1)
# print(f"I can't invite you to dinner,{remove_guest.title()}.")

# remove_guest = names.pop(2)
# print(f"I can't invite you to dinner,{remove_guest.title()}.")

# remove_guest = names.pop(2)
# print(f"I can't invite you to dinner,{remove_guest.title()}.")

# remove_guest = names.pop(2)
# print(f"I can't invite you to dinner,{remove_guest.title()}.")

# print(f"You are still invited to the dinner, {names[0].title()}!")
# print(f"You are still invited to the dinner, {names[1].title()}!")

# print(f"I'm inviting the {len(names)} people for the dinner!")

# del names[0]
# del names[0]

# print(names)

# -----------------------------------------------------------------------------

# Organizing a List 

# Sorting a List Permanently with the sort() Method 

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
# print(cars)

cars.sort(reverse=True)
# print(cars)


# Sorting a List Temporarily with the sorted() function 

cars = ['bmw', 'audi', 'toyota', 'subaru']

# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere si the original list again:")
# print(cars)

# print(sorted(cars, reverse=True))


# Printing a List in Reverse Order 

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)

# cars.reverse()
# print(cars)


# Finding the Length of a List 

cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars))

# -----------------------------------------------------------------------------

# Exercises 

# 3.8 Seeing the World 

places = ['myanmar', 'thai', 'usa', 'uk', 'china']

# print("Here is the orginal order:")
# print(places)

# print("\nHere is the tempo list:")
# print(sorted(places))

# print("\nHere is the original list again:")
# print(places)

# print("\nHere is the tempo reverse list:")
# print(sorted(places, reverse=True))

# print("\nHere is the original list again:")
# print(places)

# places.reverse()
# print("\nHere is the reverse order list:")
# print(places)

# places.reverse()
# print("\nHere is the reverse order list:")
# print(places)

# places.sort()
# print("\nHere is the perment sort list:")
# print(places)

# places.sort()
# print("\nHere is the perment reverse sort list:")
# print(places)


# 3.9 Dinner Guests //Done


# 3.10 Every Functions

# insert(index, value)
# append(value)

# pop(value)
# pop(index, value)
# del list[index]
# list.remove(value)


# sort()
# sort(revers=True)
# sorted(list)
# sorted(list, reverse=True)
# list.reverse()
# len(list)

# -----------------------------------------------------------------------------


# Avoiding Index Errors When working with Lists 