import pandas as pd

# customer dataframe
df_customer = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Zannatul', 'Farzana', 'Maria']
})

# order dataframe
df_order = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderAmount': [250, 300, 560]
})

# inner merge
df_merged = pd.merge(df_customer, df_order, how='inner', on='CustomerID')
print("Inner Merge")
print(df_merged)

# outer merge
df_merged = pd.merge(df_customer, df_order, how='outer', on='CustomerID')
print("\nOuter Merge")
print(df_merged)

# left merge
df_merged = pd.merge(df_customer, df_order, how='left', on='CustomerID')
print("\nLeft Merge")
print(df_merged)

# right merge
df_merged = pd.merge(df_customer, df_order, how='right', on='CustomerID')
print("\nRight Merge")
print(df_merged)

# Cross merge
df_merged= pd.merge(df_customer, df_order, how='cross')
print("\nCross Merge")
print(df_merged)

'''
cross join
1df= m rows
2df= n rows
m*n rows
'''
