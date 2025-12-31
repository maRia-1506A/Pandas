import pandas as pd

details={
    "Name": ['Zannatul', 'Farzana', 'Maria', 'Afridi', 'Hasan', 'Tanmoy'],
    "Age" :[22, 18, 21, 19, 25, 23],
    "Salary": [20000, 25000,15000, 34000, 40000, 30000],
    "Performance Score": [54, 76, 85, 48, 90, 67]
}
df= pd.DataFrame(details)
print('Simple Dataframe:')
print(df)
print('Descriptive Statistics:')
print(df.describe())