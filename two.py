import pandas as pd

data = {"Name": ["Akib","Mahroof","Rishi"],
        "Age": ["18","19","20"],
        "Salary": [45000,25000,30000],}

df = pd.DataFrame(data)

print(df)

data = pd.read_csv("Data/daily_food_nutrition_dataset.csv")
print(data)

# Understanding data
print(data.head(10))
print(data.tail(10))
print(data.info())
print(data.describe())
print(data.isnull().sum())

# Handling duplicate values
print(data.duplicated().sum())
# print(data.drop_duplicates("")) give name of the field where u want to delete the duplicate value

# Working with missing data
print(data.isnull().sum())
print(data.dropna())
# print(data.replace(np.nan,"hi"))

