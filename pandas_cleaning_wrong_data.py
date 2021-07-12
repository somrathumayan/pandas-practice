import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv("datta.csv")

x.loc[1,"Duration"] = 45



# for m in x.index:
#     if x.loc[m, "Duration"] >= 50:
#         x.drop(m, inplace=True)

x.drop_duplicates(inplace = True)
print(x.to_string())

print("****************************")

print(x.corr())
print("****************************")


x.plot()
plt.show()