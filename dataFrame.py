import pandas as pd

info = {
    'name': ['Maria', 'Afridi', 'Efath'],
    'age': [10, 20, 30],
    'city': ['Dhaka', "Mymensingh", "Bhola"]
}

df= pd.DataFrame(info)
print(df)

df.to_csv("dataFrame.csv", index=False)
