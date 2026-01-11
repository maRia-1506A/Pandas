import pandas as pd

# Customer Profile DataFrame
customer_profile = pd.DataFrame(
    {
        'CustomerID': [101, 102, 103],
        'Name': ['Maria', 'Afridi', 'Efath'],
        'City': ['Jashore', 'Mymensingh', 'Bhola']
    }
)

# Transaction History DataFrame
transaction_history = pd.DataFrame(
    {
        'CustomerID': [101, 102, 101, 103],
        'TransactionID': [1, 2, 3, 4],
        'Amount': [600, 500, 450, 700]
    }
)

# 1. Merge using the CustomerID column
merge_df= pd.merge(customer_profile, transaction_history, how='inner', on='CustomerID')
print('Merge using the CustomerID column')
print(merge_df)

# 2. Create a new customer record
new_customer= pd.DataFrame({
    'CustomerID': [104],
    'Name': ['Fathum'],
    'City': ['Kurigram'],
    'TransactionID': [5],
    'Amount': [1000]
})

#  3. Concatenate this new customer record with the merged DataFrame
concat_df= pd.concat([merge_df, new_customer], ignore_index=True)
print('\nConcatenate the new customer record with the merged DataFrame')
print(concat_df)

# 4. Save the final DataFrame to a CSV file.
concat_df.to_csv('I:\CODE\Pandas\CASE_BASED_QUESTION\Final_customer_df.csv', index=False)