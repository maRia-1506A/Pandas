import pandas as pd

info = {
    'name': ['Maria', 'Afridi', 'Efath'],
    'age': [10, 20, 30],
    'city': ['Dhaka', "Mymensingh", "Bhola"]
}
df = pd.DataFrame(info)
print(df)

# convert dataframe to files
'''
df.to_csv("dataFrame.csv", index=False)
df.to_excel("dataFrame.xlsx", index=False)
'''
df.to_json("dataFrame.json", index=False)


print(df.info())