import pandas as pd
details = {
    "Name": ['Zannatul', 'Farzana', 'Maria', 'Afridi', 'Hasan', 'Tanmoy'],
    "Age": [22, 18, 21, 22, 25, 18],
    "Salary": [20000, 25000, 15000, 34000, 40000, 30000],
}
df = pd.DataFrame(details)
print(df)

# single group 
grouped= df.groupby("Age")['Salary'].sum()
print(f'\n{grouped}')

# multiple group 
grouped= df.groupby(["Age","Name"])['Salary'].sum()
print(f'\n{grouped}')