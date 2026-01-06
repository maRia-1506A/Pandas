import pandas as pd
details = {
    "Name": ['Zannatul', 'Farzana', 'Maria'],
    "Age": [22, 18, 21],
    "Salary": [10000,20000, 30000]
}
df = pd.DataFrame(details)
print(df)

# single column 
df.sort_values(by='Age', ascending=False, inplace=True)
print('\nSorted Age by Descending:')
print(df)

# multiple column 
df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print('\nSorted Age & Salary by Descending:')
print(df)
