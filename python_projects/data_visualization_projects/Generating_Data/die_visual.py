# Rolling a Die 

# from die import Die 

# # Create a D6.
# die = Die()

# # Make some rolls, and store results in a list 
# results = []
# for roll_num in range(100):
#     result = die.roll()
#     results.append(result)


# Analyzing the Results 

# from die import Die 

# # Create a D6
# die = Die()

# # Make some rolls, and store results in a list 
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# # Analyze the results.
# frequencies = []
# poss_results = range(1, die.num_sides+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# print(frequencies)


# Making a Histogram

# import plotly.express as px 

# from die import Die 

# # Create a D6
# die = Die()

# # Make some rolls, and store results in a list 
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# # Analyze the results.
# frequencies = []
# poss_results = range(1, die.num_sides+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)


# # Visulize the results 
# fig = px.bar(x=poss_results, y=frequencies)
# fig.show()


# Customizing the Plot 

# import plotly.express as px 

# from die import Die 

# # Create a D6
# die = Die()

# # Make some rolls, and store results in a list 
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# # Analyze the results.
# frequencies = []
# poss_results = range(1, die.num_sides+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)


# # Visulize the results 
# title = "Results of Rolling One D6 1,000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.show()


# Rolling Two Dice 

# import plotly.express as px 

# from die import Die

# die_1 = Die()
# die_2 = Die()

# # Make some rolls and store in a list. 
# results = []
# for num_roll in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# # Analyze the results 
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# poss_results = range(2, max_result+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # Visualize the results 
# title = "Results of Rolling Two D6 Dice 1,000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.show()


# Further Customization 


# import plotly.express as px 

# from die import Die

# die_1 = Die()
# die_2 = Die()

# # Make some rolls and store in a list. 
# results = []
# for num_roll in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# # Analyze the results 
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# poss_results = range(2, max_result+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # Visualize the results 
# title = "Results of Rolling Two D6 Dice 1,000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# # Further customize chart.
# fig.update_layout(xaxis_dtick=1)

# fig.show()


# Rolling Dice of Different Size 

# import plotly.express as px

# from die import Die 


# die_1 = Die()
# die_2 = Die(10)

# # Make the rolls and add to the list 
# results = []
# for num_roll in range(50_000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# # Analyze the results 
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# poss_results = range(2, max_result+1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)


# # Visualize the chart.
# title = "Results of Rolling a D6 and a D10 50,000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.update_layout(xaxis_dtick=1)
# fig.show()


# Saving Figures 

import plotly.express as px

from die import Die 


die_1 = Die()
die_2 = Die(10)

# Make the rolls and add to the list 
results = []
for num_roll in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results 
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualize the chart.
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.write_html('dice_visual_d6d10.html')

