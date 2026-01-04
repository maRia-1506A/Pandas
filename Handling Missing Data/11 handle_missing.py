import pandas as pd
details = {
    "Name": ['Zannatul', None, 'Maria', 'Afridi', 'Hasan', 'Tanmoy'],
    "Age": [22, 18, 21, 19, None, 23],
    "Salary": [20000, 25000, None, 34000, 40000, 30000],
    "Performance_Score": [54, 76, 85, 48, 90, 67]
}
df = pd.DataFrame(details)
print(df)

# remove the row/col of missing values
df.dropna(inplace=True)  # by default axis=0
print(f'\n{df}')

# df.dropna(axis=1, inplace=True) remove the col of missing values
