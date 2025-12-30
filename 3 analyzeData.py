'''
1- understand the data set
2- identify the problems
3- plan next steps
'''

import pandas as pd
df= pd.read_json("sample_Data.json")

print("Display first 10 rows")
print(df.head(10))

print("Display last 10 rows")
print(df.tail(10))


# Info About the Data
print(df.info())