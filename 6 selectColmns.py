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

# select single column
print('\nNames (Single column returns series)')
print(df['Age'])

# select multiple columns
print('\nSubset with Name and Salary')
print(df[['Name', 'Salary']])