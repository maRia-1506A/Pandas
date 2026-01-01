import pandas as pd
details = {
    "Name": ['Zannatul', 'Farzana', 'Maria', 'Afridi', 'Hasan', 'Tanmoy'],
    "Age": [22, 18, 21, 19, 25, 23],
    "Salary": [20000, 25000, 15000, 34000, 40000, 30000],
    "Performance_Score": [54, 76, 85, 48, 90, 67]
}
df = pd.DataFrame(details)
print(df)

# update single value
df.loc[3, 'Salary'] = 50000
print(f'\nUpdate the 4th value of Salary\n{df}')

# update whole row
df['Salary'] = df['Salary']*1.05
print(f'\nUpdate the salary row by increasing 5%\n{df}')
