import pandas as pd
details = {
    "Name": ['Zannatul', 'Farzana', 'Maria', 'Afridi', 'Hasan', 'Tanmoy'],
    "Age": [22, 18, 21, 19, 25, 23],
    "Salary": [20000, 25000, 15000, 34000, 40000, 30000],
    "Performance_Score": [54, 76, 85, 48, 90, 67]
}
df = pd.DataFrame(details)
print(df)

# removing columns
df.drop(columns=['Performance_Score', 'Age'], inplace=True)
print(f'\nDF after removing Performance_Score columns\n{df}')
