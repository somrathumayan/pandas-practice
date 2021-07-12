import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)
print("***********************")
print(myvar[0])
print(myvar["y"])
print("***********************")


calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390,
}

myvar2 = pd.Series(calories)
print(myvar2)
print("***********************")




