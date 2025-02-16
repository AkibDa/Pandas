import pandas as pd

data = {"Name": ["Akib","Mahroof","Rishi"],
        "Age": ["18","19","20"],
        "Salary": [45000,25000,30000],}

df = pd.DataFrame(data)

print(df)

data = pd.read_csv("Data/daily_food_nutrition_dataset.csv")
print(data)

# Understanding Data
print(data.head(10))
print(data.tail(10))
print(data.info())
print(data.describe())
print(data.isnull().sum())