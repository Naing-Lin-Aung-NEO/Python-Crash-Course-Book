# Exercises 

# 16.1 Sitka Rainfall

# from pathlib import Path 
# import csv 
# from datetime import datetime

# import matplotlib.pyplot as plt

# path = Path('weather_data/death_valley_2021_full.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# # Extract rainfall amounts, and dates 
# dates, rainfalls = [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     try:
#         rainfall = row[3]
#     except ValueError:
#         print(f"The data is missing for {current_date}")
#     else:
#         dates.append(current_date)
#         rainfalls.append(rainfall)

# # Plot the rainfalls, Dates 
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(dates, rainfalls, color='green')

# # Format the Chart 
# ax.set_title('Daily RainFall Amounts, 2021\nDeath Valley, CA', fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel('RainFall Amount', fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()

# -----------------------------------------------------------------------------

# 16.2 Sitka-Death Valley Comparison / 16.4 Automatic Indexes 

# from pathlib import Path 
# import csv
# from datetime import datetime

# import matplotlib.pyplot as plt 

# def get_weather_data(path, dates, highs, lows, date_index, high_index, low_index):
#     lines = path.read_text().splitlines()
#     reader = csv.reader(lines)
#     header_row = next(reader)

#     # Extract the dates, highs, lows data
#     for row in reader:
#         date = datetime.strptime(row[date_index], '%Y-%m-%d')
#         try:
#             high = int(row[high_index])
#             low = int(row[low_index])
#         except ValueError:
#             print(f"The data is missing for {date}")
#         else:
#             dates.append(date)
#             highs.append(high)
#             lows.append(low)

# # For Sitka Weather Data
# path = Path('weather_data/sitka_weather_2021_simple.csv')
# dates, highs, lows = [], [], []
# get_weather_data(path, dates, highs, lows, date_index=2, high_index=4, low_index=5)

# # Ploting for Sitka 
# plt.style.use('seaborn-v0_8')
# fig,ax = plt.subplots(figsize=(12,6))
# ax.plot(dates, highs, color='red', alpha=0.7)
# ax.plot(dates, lows, color='blue', alpha=0.7)
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.17)

# # For Death Valley Weather Data 
# path = Path('weather_data/death_valley_2021_simple.csv')
# dates, highs, lows = [], [], []
# get_weather_data(path, dates, highs, lows, date_index=2, high_index=3, low_index=4)

# # Plot for Death Valley 
# ax.plot(dates, highs, color='red', alpha=0.5)
# ax.plot(dates, lows, color='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.07)

# # Format the Graph
# title = 'Daily High and Low Temperatures, 2021'
# title += '\nSitka, AK & Death Valley, CA'
# ax.set_title(title, fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel('Temperature(F)', fontsize=16)
# ax.tick_params(labelsize=16)

# ax.set_ylim(10, 140)

# plt.show()

# -----------------------------------------------------------------------------

# 16.3 New York / 16.5 Explore 

# from pathlib import Path 
# import csv 
# from datetime import datetime

# import matplotlib.pyplot as plt

# path = Path('weather_data/newyork_2024.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# # for index, column_header in enumerate(header_row):
# #     print(index, column_header) 
# # 5 date 
# # 8 tmax 
# # 9 tmin 

# # Extract dates, high and low temperatures.
# dates, highs, lows = [], [], []
# for row in reader:
#     current_date = datetime.strptime(row[5], '%Y-%m-%d')
#     try:
#         high = int(row[8])
#         low = int(row[9])
#     except ValueError:
#         print(f'The data is missing for {current_date}')
#     else:
#         dates.append(current_date)
#         highs.append(high)
#         lows.append(low)

# # Plot the chart.
# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red', alpha=0.5)
# ax.plot(dates, lows, color='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

# # Style the Graph 

# ax.set_title('Daily High and Low Temperatures, 2024\nNewYork, NY', fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel('Temperature(F)', fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()

# -----------------------------------------------------------------------------
