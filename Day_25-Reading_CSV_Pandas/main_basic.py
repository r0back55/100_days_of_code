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


# Get data in a full row:
print(data[data["day"] == "Monday"], "\n")
print(data[data["temp"] == max_temp], "\n")


# Get only one value
monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp*1.8+32)


# Create a dataframe from scratch
data_dict_2 = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

df = pd.DataFrame(data_dict_2)
print(df)
df.to_csv("./new-data.csv")
