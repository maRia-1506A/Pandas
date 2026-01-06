'''
mean(), min(), max(), sum(), count(), std()
'''

import pandas as pd
details = {
    "Name": ['Zannatul', 'Farzana', 'Maria'],
    "Age": [22, 18, 21],
    "Salary": [10000,20000, 30000]
}
df = pd.DataFrame(details)
print(df)

print(f'Total Salary: {df['Salary'].sum()}')
avg_salary= df['Salary'].mean()
print(f'Average Salary: {avg_salary}')