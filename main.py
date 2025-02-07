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

print(ex["Id"]) # type = Series
print(ex[["Id", "SepalLengthCm"]])
print(ex.iloc[0]) 

ex2 = pd.read_csv("data/data.csv")
print(ex2.head())
print(ex2.dropna())
print(ex2.fillna(0))
print(ex.rename(columns={"SepalLengthCm": "SL"}))
print(ex.describe())
print(ex.info())
# ex["SL"] = ex["SL"].astype(int)
# print(ex.info())

ex["zeros"] = [0 for i in range(len(ex))] 
print(ex)

def fx(a):
  return a+1

ex["zeros + 1"] = ex["zeros"].apply(fx)
print(ex["zeros + 1"])

ex.to_csv("data/export.csv", index=False)

ex1 = pd.DataFrame({
  "name": ["Akib","Rohit","Debom","Barnob","Shuvayan","Shubham"],
  "marks": [100,86,54,68,92,77],
})
print(ex1)

ex3 = pd.DataFrame({
  "name": ["Shail","Nikita","Saloni","Ananya","Sneha","Shreya"],
  "marks": [81,78,66,79,72,67],
})
print(ex3)

pd.concat(ex1, ex3)