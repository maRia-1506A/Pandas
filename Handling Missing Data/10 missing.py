import pandas as pd
details = {
    "Name": ['Zannatul', None, 'Maria', 'Afridi', 'Hasan', 'Tanmoy'],
    "Age": [22, 18, 21, 19, None, 23],
    "Salary": [20000, 25000, None, 34000, 40000, 30000],
    "Performance_Score": [54, 76, 85, 48, 90, 67]
}
df = pd.DataFrame(details)
print(df)

# TRUE means detecting that data is missing
print('\n')
print(df.isnull())

# number of missing values 
print('\n')
print(df.isnull().sum())