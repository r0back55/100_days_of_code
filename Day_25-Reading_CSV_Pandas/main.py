import pandas as pd

file = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240613.csv")
df = pd.DataFrame(file)

fur_color_count = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [0, 0, 0]
}

for color in df['Primary Fur Color']:
    if color == 'Gray':
        fur_color_count["Count"][0] += 1
    elif color == 'Cinnamon':
        fur_color_count["Count"][1] += 1
    elif color == 'Black':
        fur_color_count["Count"][2] += 1

fur_df = pd.DataFrame(fur_color_count)
print(fur_df)
fur_df.to_csv("./squirrel_count")
