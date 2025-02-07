import pandas as pd

print("Introduction to pandas")

'''Key Data Structures in Pandas'''
# Series (1 Dimensional)
# DataFrame (2 Dimensional)

s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s)

df = pd.DataFrame({"names": ["Akib","Rishi","Mahroof"], "marks":["100","59","55"]})
print(df)

ex = pd.read_csv("data/Iris.csv")
print(ex)
print(ex.head())
print(ex.tail())
print(ex.describe())
print(ex.info())

#Data Selection

print(ex["Id"])
print(ex[["Id", "SepalLengthCm"]])