import pandas as pd

# region1 dataframe
df_region1= pd.DataFrame({
    "CustomerID": [1,2],
    "Name": ['Zannatul','Farzana']
})

# region2 dataframe
df_region2= pd.DataFrame({
    "CustomerID": [3,4],
    "Name": ['Afridi','Hasan']
})

# combining vertically (by default)
df_concate=pd.concat([df_region1, df_region2], axis=0, ignore_index=True)
print("Combine vertically")
print(df_concate)

# combining horizontally
df_concate=pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print("Combine horizontally")
print(df_concate)