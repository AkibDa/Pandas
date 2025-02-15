import pandas as pd

data = {"Name": ["Akib","Mahroof","Rishi"],
        "Age": ["18","19","20"],
        "Salary": [45000,25000,30000],}

df = pd.DataFrame(data)

print(df)

data = pd.read_excel("Data/kl.xlsx")
print(data)