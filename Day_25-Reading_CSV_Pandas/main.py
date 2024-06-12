## Reading CSV files - Native way ##
# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)


## Reading CSV files - Pandas ##
import pandas as pd

data = pd.read_csv("./weather_data.csv")
print(data["temp"])
print("data =>> ", type(data))
print("data['temp'] =>> ", type(data["temp"]))

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

avg_temp = data["temp"].mean()
max_temp = data["temp"].max()
print(avg_temp.round(2))
print(max_temp)

# Get data in columns
print(data.condition)

# Get data in a row:
print(data[data["day"] == "Monday"], "\n")

print(data.iloc[1])
