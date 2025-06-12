# Plotting and Styling Inividual Points with scatter()

# import matplotlib.pyplot as plt

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)

# # Set chart title and lable axes 
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)

# plt.show()


# Plotting a Series of Points with scatter()

# import matplotlib.pyplot as plt 

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100)

# # Set the title, lables, and label size 
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)

# plt.show()


# Calculating Data Automatically 

# import matplotlib.pyplot as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)

# # Set the style and texts 
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)

# # Set the range for each axis 
# ax.axis([0, 1100, 0, 1_100_000])

# plt.show()


# Customizing Tick Lables 

# import matplotlib.pyplot as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)

# # Set the style and texts 
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)

# # Set the range for each axis 
# ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style="plain")

# plt.show()

# Defining Custom Colors 

# import matplotlib.pyplot as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, color='red', s=10)

# # Set the style and texts 
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)

# # Set the range for each axis 
# ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style="plain")

# plt.show()

# Using a Colormap

# import matplotlib.pyplot as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# # Set the style and texts 
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)

# # Set the range for each axis 
# ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style="plain")

# plt.show()

# Saving Your Plots Automatically

# import matplotlib.pyplot as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# # Set the style and texts 
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)

# # Set the range for each axis 
# ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style="plain")

# plt.savefig('squares_plot.png', bbox_inches='tight')