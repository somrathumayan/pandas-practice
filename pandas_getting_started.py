import pandas as pd
# to install pandas write "pip install pandas" in the terminal

mydataset = {
    'cars':  ["BMW","Toyota", "Audi"],
    'passing': [3,7,2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

print("********************************************")
print("Pandas Version: ", pd.__version__)