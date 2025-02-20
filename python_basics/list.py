# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

# Accessing Elements in a List 

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0].title())
# print(bicycles[1])
# print(bicycles[3])
# print(bicycles[-1])

# Using Individual Values from a List 

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = f"My first bicycle was {bicycles[1].title()}"
# print(message)

# Exercise 
names = ['ki ki', 'no no', 'coya', 'hsu hsu', 'khin khin', 'ba mg', 'side side']
# print(names)
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])
# print(names[6])

# print(f"Hello!, {names[0].title()}")
# print(f"Hello!, {names[1].title()}")
# print(f"Hello!, {names[2].title()}")
# print(f"Hello!, {names[3].title()}")
# print(f"Hello!, {names[4].title()}")
# print(f"Hello!, {names[5].title()}")
# print(f"Hello!, {names[6].title()}")

cars = ["BMW", "Mercedes", "Roll Ryces", "Tesla"]
message = f"I would like to own a {cars[0]} car."
# print(message)

# Modifying, Adding, and Removing Elements 

# 1. Modifying Elements in a List 
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles[1] = 'honda'
# print(motorcycles)

# 2. Adding Elements to a List 
# -Appending Elements to the End of a List 
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
# print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
# print(motorcycles)

# 3. Inserting Elements into a List 
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
# print(motorcycles)

# 4. Removing Elements from a List 
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

del motorcycles[0]
# print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_own = motorcycles.pop()
# print(f"My last own motocycle is {last_own.title()}")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

motorcycles.remove('ducati')
# print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
# print(f'A {too_expensive.title()} is too expensive for me.')

# Exercise 

# guests = ['mom', 'dad', 'sis']
# message = f'Plz come to my dinner {guests[0].title()}'
# print(message)
# message = f'Plz come to my dinner {guests[1].title()}'
# print(message)
# message = f'Plz come to my dinner {guests[2].title()}'
# print(message)
# guests[1] = 'bro'
# print(guests)
# message = f'Plz come to my dinner {guests[1].title()}'
# print(message)
# guests.insert(0, 'best friend')
# guests.insert(2, 'girl friend')
# guests.append('teacher')
# print(guests)
# message = f'Plz come to my dinner {guests[0].title()}'
# print(message)
# message = f'Plz come to my dinner {guests[1].title()}'
# print(message)

# message = f'Plz come to my dinner {guests[2].title()}'
# print(message)

# message = f'Plz come to my dinner {guests[3].title()}'
# print(message)

# message = f'Plz come to my dinner {guests[4].title()}'
# print(message)

# message = f'Plz come to my dinner {guests[5].title()}'
# print(message)

# print("I'm sorry! I don't have big table to make a dinner, and I've decided to invite only two people!")
# print(guests)

# del_guest = guests.pop(0)
# message = f"I'm sorry!, {del_guest.title()} I don't have big table to make a dinner, and I've decided to invite only two people!"
# print(message)

# del_guest = guests.pop(2)
# message = f"I'm sorry!, {del_guest.title()} I don't have big table to make a dinner, and I've decided to invite only two people!"
# print(message)

# del_guest = guests.pop(2)
# message = f"I'm sorry!, {del_guest.title()} I don't have big table to make a dinner, and I've decided to invite only two people!"
# print(message)

# del_guest = guests.pop(2)
# message = f"I'm sorry!, {del_guest.title()} I don't have big table to make a dinner, and I've decided to invite only two people!"
# print(message)

# print(f"You're still invited! {guests[0]}")
# print(f"You're still invited! {guests[1]}")
# print(len(guests))

# del guests[0]
# del guests[0]
# print(guests)


# Sorting a List Permanently with the sort() Method 

cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# Sorting a List Temporarily with the sorted() Function

# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

# Printing a List in Reverse Order 

# print(cars)
# cars.reverse()
# print(cars)

# Finding the Length of a List 
# print(len(cars))

# Exercise 

# places = ['us', 'uk', 'myanmar', 'thai', 'korea']
# print(places)

# print(sorted(places))

# print(places)

# places.reverse()
# print(places)

# places.reverse()
# print(places)

# places.sort()
# print(places)

# places.sort(reverse=True)
# print(places)

#-----------------------------------------------------

# countries = ['myan', 'thai', 'indo', 'usa', 'sg']
# print(countries)

# countries[1] = 'sudi'
# print(countries)

# countries.append('india')
# print(countries)

# countries.insert(0, 'uk')
# print(countries)

# del countries[2]
# print(countries)

# popped_country = countries.pop(4)
# print(f'I deleted {popped_country} from the list!')
# print(countries)

# countries.remove("indo")
# print(countries)

# print(sorted(countries))
# print(sorted(countries, reverse=True))
# print(countries)

# countries.sort()
# print(countries)

# countries.sort(reverse=True)
# print(countries)

# countries.reverse()
# print(countries)

# print(len(countries))

# Avoiding Index Error working with lists

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) - IndexError: list index out of range 

# print(motorcycles[-1]) - the last item is index -1

motorcycles = []
# print(motorcycles[-1]) - IndexError: list index out of range 

# Exercise 
# cars = ['bmw', 'mercedes', 'audi']
# comment = f"{cars[0].upper()} is my last car."
# print(comment)
