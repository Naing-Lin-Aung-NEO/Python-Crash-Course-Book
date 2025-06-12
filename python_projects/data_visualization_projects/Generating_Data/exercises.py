# 15.1 Cubes 

# For first 5 Cubes 

# import matplotlib.pyplot as plt 

# x_values = range(1, 6)
# y_values = [x**3 for x in x_values]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# # ax.scatter(x_values, y_values, s=100)
# ax.plot(x_values, y_values)

# # Set the styple , labels, title, ..
# ax.set_title('Cube Numbers', fontsize=24)
# ax.set_xlabel('Value', fontsize=14)
# ax.set_ylabel('Cube of Value', fontsize=14)
# ax.tick_params(labelsize=14)

# plt.show()


# For first 5000 cubes 

# import matplotlib.pyplot as plt 

# x_values = range(1, 5001)
# y_values = [x**3 for x in x_values]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)

# # Set the styple , labels, title, ..
# ax.set_title('Cube Numbers', fontsize=24)
# ax.set_xlabel('Value', fontsize=14)
# ax.set_ylabel('Cube of Value', fontsize=14)
# ax.tick_params(labelsize=14)

# # Set the axis 
# ax.axis([0, 5_000, 0, 125_000_000_000])
# ax.ticklabel_format(style='plain')

# plt.show()

# -----------------------------------------------------------------------------

# 15.2 Colored Cubes 

# For first 5 cubes with color mapping 

# import matplotlib.pyplot as plt 

# x_values = range(1, 6)
# y_values = [x**3 for x in x_values]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=100)

# # Set the styple , labels, title, ..
# ax.set_title('Cube Numbers', fontsize=24)
# ax.set_xlabel('Value', fontsize=14)
# ax.set_ylabel('Cube of Value', fontsize=14)
# ax.tick_params(labelsize=14)

# plt.show()

# For first 5000 cubes with color mapping 

# import matplotlib.pyplot as plt 

# x_values = range(1, 5001)
# y_values = [x**3 for x in x_values]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# # Set the styple , labels, title, ..
# ax.set_title('Cube Numbers', fontsize=24)
# ax.set_xlabel('Value', fontsize=14)
# ax.set_ylabel('Cube of Value', fontsize=14)
# ax.tick_params(labelsize=14)

# # Set the axis 
# ax.axis([0, 5_000, 0, 125_000_000_000])
# ax.ticklabel_format(style='plain')

# plt.show()

# -----------------------------------------------------------------------------

# 15.3 Molecular Motion 

# from random import choice
# import matplotlib.pyplot as plt

# class RandomWalk:
#     """A class to create random walks."""

#     def __init__(self, num_points=5000):
#         """Initalize attributes for randomwalk."""
#         self.num_points = num_points

#         # Start the walk with (0,0)
#         self.x_values = [0]
#         self.y_values = [0]

#     def fill_walk(self):
#         """Generate the walks."""
#         while len(self.x_values) < self.num_points:
            
#             # Direction and decide how far to go 
#             x_direction = choice([1, -1])
#             x_distance = choice([0, 1, 2, 3, 4])
#             x_step = x_direction * x_distance

#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance

#             # Remove when the steps are 0.
#             if x_step and y_step == 0:
#                 continue

#             # Create new position 
#             x = self.x_values[-1] + x_step
#             y = self.y_values[-1] + y_step

#             # Add to the x_values and y's.
#             self.x_values.append(x)
#             self.y_values.append(y)

# while True:
#     rw = RandomWalk()
#     rw.fill_walk()

#     plt.style.use('classic')
#     fig, ax = plt.subplots(figsize=(12, 8), dpi=120)
#     ax.plot(rw.x_values, rw.y_values, linewidth=14)
#     ax.set_aspect('equal')

#     # Remove the axes 
#     ax.xaxis.set_visible(False)
#     ax.yaxis.set_visible(False)

#     plt.show()

#     ans = input("Do you wanna make another walk? (y/n): ")
#     if ans == 'n':
#         break

# -----------------------------------------------------------------------------


# 15.4 Modified Random Walks 

# from random import choice
# import matplotlib.pyplot as plt

# class RandomWalk:
#     """A class to create random walks."""

#     def __init__(self, num_points=5000):
#         """Initalize attributes for randomwalk."""
#         self.num_points = num_points

#         # Start the walk with (0,0)
#         self.x_values = [0]
#         self.y_values = [0]

#     def fill_walk(self):
#         """Generate the walks."""
#         while len(self.x_values) < self.num_points:
            
#             # Direction and decide how far to go 
#             x_direction = choice([1])
#             x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
#             x_step = x_direction * x_distance

#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance

#             # Remove when the steps are 0.
#             if x_step and y_step == 0:
#                 continue

#             # Create new position 
#             x = self.x_values[-1] + x_step
#             y = self.y_values[-1] + y_step

#             # Add to the x_values and y's.
#             self.x_values.append(x)
#             self.y_values.append(y)

# while True:
#     rw = RandomWalk()
#     rw.fill_walk()

#     plt.style.use('classic')
#     fig, ax = plt.subplots(figsize=(12, 8), dpi=120)
#     ax.plot(rw.x_values, rw.y_values, linewidth=14)
#     ax.set_aspect('equal')

#     # Remove the axes 
#     ax.xaxis.set_visible(False)
#     ax.yaxis.set_visible(False)

#     plt.show()

#     ans = input("Do you wanna make another walk? (y/n): ")
#     if ans == 'n':
#         break

# -----------------------------------------------------------------------------

# 15.5 Refactoring 

# from random import choice
# import matplotlib.pyplot as plt

# class RandomWalk:
#     """A class to create random walks."""

#     def __init__(self, num_points=5000):
#         """Initalize attributes for randomwalk."""
#         self.num_points = num_points

#         # Start the walk with (0,0)
#         self.x_values = [0]
#         self.y_values = [0]

#     def fill_walk(self):
#         """Generate the walks."""
#         while len(self.x_values) < self.num_points:
            
#             x_step = self.get_step()
#             y_step = self.get_step()

#             # Remove when the steps are 0.
#             if x_step and y_step == 0:
#                 continue

#             # Create new position 
#             x = self.x_values[-1] + x_step
#             y = self.y_values[-1] + y_step

#             # Add to the x_values and y's.
#             self.x_values.append(x)
#             self.y_values.append(y)
    
#     def get_step(self):
#             direction = choice([1, -1])
#             distacne = choice([0, 1, 2, 3, 4])
#             step = direction * distacne
#             return step


# while True:
#     rw = RandomWalk()
#     rw.fill_walk()

#     plt.style.use('classic')
#     fig, ax = plt.subplots(figsize=(12, 8), dpi=120)
#     ax.plot(rw.x_values, rw.y_values, linewidth=14)
#     ax.set_aspect('equal')

#     # Remove the axes 
#     ax.xaxis.set_visible(False)
#     ax.yaxis.set_visible(False)

#     plt.show()

#     ans = input("Do you wanna make another walk? (y/n): ")
#     if ans == 'n':
#         break

# -----------------------------------------------------------------------------

# 15.6 Two D8s 

# from random import randint

# import plotly.express as px

# class Die:
#     """A class represent a model of die."""

#     def __init__(self, num_sides=6):
#         """Set the sides for the die."""
#         self.num_sides = num_sides

#     def roll(self):
#         """Return the result of rolling die."""
#         result = randint(1, self.num_sides)
#         return result

# # Make an instances of Die 
# die_1 = Die(8)
# die_2 = Die(8)

# # Roll the dice and store the result in a list 
# results = []
# for num_roll in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# # Analyze the Results 
# frequencies = []
# max_results = die_1.num_sides + die_2.num_sides
# poss_results = range(2, max_results+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # Visual the Chart 
# title = "Results of Rolling Two D8 1000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.update_layout(xaxis_dtick=1)
# fig.show()

# -----------------------------------------------------------------------------

# 15.7 Three Dice 


# from random import randint

# import plotly.express as px

# class Die:
#     """A class represent a model of die."""

#     def __init__(self, num_sides=6):
#         """Set the sides for the die."""
#         self.num_sides = num_sides

#     def roll(self):
#         """Return the result of rolling die."""
#         result = randint(1, self.num_sides)
#         return result

# # Make an instances of Die 
# die_1 = Die()
# die_2 = Die()
# die_3 = Die()

# # Roll the dice and store the result in a list 
# results = []
# for num_roll in range(1000):
#     result = die_1.roll() + die_2.roll() + die_3.roll()
#     results.append(result)

# # Analyze the Results 
# frequencies = []
# max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
# poss_results = range(3, max_results+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # Visual the Chart 
# title = "Results of Rolling Two D8 1000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.update_layout(xaxis_dtick=1)
# fig.show()

# -----------------------------------------------------------------------------

# Multiplication 

# from random import randint

# import plotly.express as px

# class Die:
#     """A class represent a model of die."""

#     def __init__(self, num_sides=6):
#         """Set the sides for the die."""
#         self.num_sides = num_sides

#     def roll(self):
#         """Return the result of rolling die."""
#         result = randint(1, self.num_sides)
#         return result

# # Make an instances of Die 
# die_1 = Die(8)
# die_2 = Die(8)

# # Roll the dice and store the result in a list 
# results = []
# for num_roll in range(1000):
#     result = die_1.roll() * die_2.roll()
#     results.append(result)

# # Analyze the Results 
# frequencies = []
# max_results = die_1.num_sides + die_2.num_sides
# poss_results = range(2, max_results+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # Visual the Chart 
# title = "Results of Rolling Two D8 1000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.update_layout(xaxis_dtick=1)
# fig.show()

# The difference is there is no frequency of 11, 13.... 

# -----------------------------------------------------------------------------

# 15.9 Die Comprehensions 

# from random import randint

# import plotly.express as px

# class Die:
#     """A class represent a model of die."""

#     def __init__(self, num_sides=6):
#         """Set the sides for the die."""
#         self.num_sides = num_sides

#     def roll(self):
#         """Return the result of rolling die."""
#         result = randint(1, self.num_sides)
#         return result

# # Make an instances of Die 
# die_1 = Die(8)
# die_2 = Die(8)

# # Roll the dice and store the result in a list 
# results = [die_1.roll() + die_2.roll() for num_roll in range(1000)]

# # Analyze the Results 
# max_results = die_1.num_sides + die_2.num_sides
# poss_results = range(2, max_results+1)
# frequencies = [results.count(value) for value in poss_results]

# # Visual the Chart 
# title = "Results of Rolling Two D8 1000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.update_layout(xaxis_dtick=1)
# fig.show()


# -----------------------------------------------------------------------------

# 15.10 Practicing with Both Libraries 

# Random Walk with Plotly 

# from random import choice

# class RandomWalk:
#     """Represent a randomwalk."""

#     def __init__(self, num_points):
#         """Initializing attributes for RandomWalk class."""
#         self.num_points = num_points

#         # Start with (0,0)
#         self.x_values = [0]
#         self.y_values = [0]

#     def fill_work(self):
#         """Calculate all the points in the walk."""
#         while len(self.x_values) < self.num_points:
#             x_step = self.get_step()
#             y_step = self.get_step()

#             # Reject moves that go nowhere.
#             if x_step and y_step == 0:
#                 continue

#             # Calculate the new positoin.
#             x = self.x_values[-1] + x_step
#             y = self.y_values[-1] + y_step

#             self.x_values.append(x)
#             self.y_values.append(y)           
    
#     def get_step(self):
#         direction = choice([1, -1])
#         distance = choice([0, 1, 2, 3, 4])
#         step = direction * distance
#         return step 
    
# import plotly.express as px 

# rw = RandomWalk(5000)
# rw.fill_work()

# title = "Random Walk"
# fig = px.bar(x=rw.x_values, y=rw.y_values, title=title)

# fig = px.scatter(x=rw.x_values, y=rw.y_values, title=title)

# fig.show()

# -----------------------------------------------------------------------------


# Rolling Dice with Matplotly 

# from random import randint

# class Die:
#     """A class to represent a die."""

#     def __init__(self, sides=6):
#         """Initialze the sides of the die."""
#         self.sides = sides

#     def roll_die(self):
#         """Roll the die and return the results."""
#         result = randint(1, self.sides)
#         return result
    

# # Create instances for dice.
# die_1 = Die()
# die_2 = Die()

# # roll the dice and store in a list.
# results = [die_1.roll_die() + die_2.roll_die() for num_roll in range(10_000)]

# # alalyze the results 
# max_results = die_1.sides + die_2.sides
# poss_results = range(2, max_results+1)
# frequencies = [results.count(value) for value in poss_results]

# import matplotlib.pyplot as plt

# plt.style.use('classic')
# fig, ax = plt.subplots()
# ax.bar(poss_results, frequencies, color='skyblue', edgecolor='none')

# ax.set_title("Rolling Two D6 Dice 10,000 Times", fontsize=24)
# ax.set_xlabel("Result", fontsize=14)
# ax.set_ylabel("Frequency of Result", fontsize=14)
# ax.set_xticks(list(poss_results))
# ax.tick_params(labelsize=14)

# plt.tight_layout()
# plt.show()
    

# -----------------------------------------------------------------------------