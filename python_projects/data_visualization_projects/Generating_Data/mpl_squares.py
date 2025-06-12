# Ploting a Simple Line Graph 

# import matplotlib.pyplot as plt 

# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()
# ax.plot(squares)

# plt.show()


# Changing the Lable Type and Line Thickness 

# import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()
# ax.plot(squares, linewidth=3)

# # Set Chart title and lable axes.
# ax.set_title("Suqare Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Suqare of Value", fontsize=14)

# # Set size of tick lables.
# ax.tick_params(labelsize=14)

# plt.show()

# Correcting the Plot 

# import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# suqares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)

# # Set the chart title and label axes, ticks
# ax.set_title("Square Numbers", fontsize=23)
# ax.set_xlabel("Value", fontsize=13)
# ax.set_ylabel("Suqare of Value", fontsize=13)
# ax.tick_params(labelsize=13)

# plt.show()


# Using Build-in-styles 

# import matplotlib.pyplot as plt
# print(plt.style.available)

# import matplotlib.pyplot as plt 

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)

# # Set the chart's title, lables thickness 
# ax.set_title("Square Numbers", fontsize=23)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Suqare of Value", fontsize=14)
# ax.tick_params(labelsize=14)

# plt.show()


