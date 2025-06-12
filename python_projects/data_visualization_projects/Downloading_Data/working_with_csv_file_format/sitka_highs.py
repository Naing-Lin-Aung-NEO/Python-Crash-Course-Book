# Parsing the CSV File Headers 

# from pathlib import Path 
# import csv

# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)
# print(header_row)


# Printing the Headers and Their Positions 

# from pathlib import Path 
# import csv 

# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)


# Extracting and Reading Data

# from pathlib import Path 
# import csv 

# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# Extract high temperatures.
# highs = []
# for row in reader:
#     high = int(row[4])
#     highs.append(high)

# print(highs)


# Plotting Data in a Temperature Chart 

# from pathlib import Path 
# import csv 

# import matplotlib.pyplot as plt

# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# # Extract high temperatures.
# highs = []
# for row in reader:
#     high = int(row[4])
#     highs.append(high)

# # Plot the high temperature 
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(highs, color='red')

# # Format plot 
# ax.set_title('Daily High Temperatures, July 2021', fontsize=24)
# ax.set_xlabel('', fontsize=16)
# ax.set_ylabel('Tmperature(F)', fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()


# Datetime Module and Plotting Dates 

# from pathlib import Path 
# import csv 
# from datetime import datetime

# import matplotlib.pyplot as plt

# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# # Extract dates and high temperatures.
# dates, highs = [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     high = int(row[4])
#     dates.append(current_date)
#     highs.append(high)

# # Plot the high temperature 
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red')

# # Format plot 
# ax.set_title('Daily High Temperatures, July 2021', fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel('Tmperature(F)', fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()


# Plotting a Longer Timeframe 

# from pathlib import Path 
# import csv 
# from datetime import datetime

# import matplotlib.pyplot as plt 

# path = Path('weather_data/sitka_weather_2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# # Extract dates and high temperatures.
# dates, highs = [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     high = int(row[4])
#     dates.append(current_date)
#     highs.append(high)

# # Plot dates and high temperatures 
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red')

# # Format the chart 
# ax.set_title('Daily High Tmeperatures, 2021', fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel('Temperature(F)', fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()


