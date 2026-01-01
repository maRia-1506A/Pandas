'''
1- select specific column
2- filter rows
3- combine multiple conditions
'''

'''
1- square brackets
2- boolean conditions
'''

import pandas as pd
details = {
    "Name": ['Zannatul', 'Farzana', 'Maria', 'Afridi', 'Hasan', 'Tanmoy'],
    "Age": [22, 18, 21, 19, 25, 23],
    "Salary": [20000, 25000, 15000, 34000, 40000, 30000],
    "Performance_Score": [54, 76, 85, 48, 90, 67]
}
df = pd.DataFrame(details)
print(f'Sample Dataframe\n{df}')

# single condition
highSalary = df[df['Salary'] > 30000]
print('\nEmployees with salary > 30000')
print(highSalary)

# multiple condition salary >30000 & age >20
multiple = df[(df['Salary'] > 30000) & (df['Age'] > 20)]
print('\nEmployees with salary > 30000 + age > 20')
print(multiple)

# multiple condition with OR
multiple = df[(df['Salary'] > 30000) | (df['Performance_Score'] > 80)]
print('\nEmployees with salary > 30000 OR Performance_Score > 80')
print(multiple)