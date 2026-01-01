import pandas as pd
details = {
    "Name": ['Zannatul', 'Farzana', 'Maria', 'Afridi', 'Hasan', 'Tanmoy'],
    "Age": [22, 18, 21, 19, 25, 23],
    "Salary": [20000, 25000, 15000, 34000, 40000, 30000],
    "Performance_Score": [54, 76, 85, 48, 90, 67]
}
df = pd.DataFrame(details)
print(df)

# adding columns using square brackets
df["Bonus"] = df['Salary']*0.1
print(f'\nAdding Bonus column using square brackets\n{df}')

# adding columns using insert() method
df.insert(0, "Employee ID", ['ID1', 'ID2','ID3','ID4','ID5','ID6'])
print(f'\nAdding Employee ID column using insert method\n{df}')
