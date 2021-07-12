import pandas as pd

# Return a new Data Frame with no empty cells:
df = pd.read_csv("data.csv")
new_df = df.dropna()
print(new_df.to_string())
print("*********************************************")

# Remove all rows with NULL values:
df2 = pd.read_csv('data.csv')
df2.dropna(inplace=True)
print(df2.to_string())
print("*********************************************")


# Replace NULL values with the number 130:
df4 = pd.read_csv('data.csv')
df4.fillna(130, inplace=True)
print(df4.to_string())
print("*********************************************")


dfr = pd.read_csv('data.csv')
dfr["Duration"].fillna(1.0, inplace=True)
print(dfr.to_string())
# This operation inserts 130 in empty cells in the "Calories" column (row 18 and 28).
print("*********************************************")

dj = pd.read_csv("data.csv")
dx = dj["Duration"].mean()
dj["Duration"].fillna(dx, inplace=True)
# #As you can see in row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68
print(dj.to_string())

# we can use mean(), mode(), median() function and replaced with
# mean, median, mode value in empty places
