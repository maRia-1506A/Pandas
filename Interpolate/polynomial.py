import pandas as pd

data={
    'Index': [0,1,2,3,4],
    'Value': [5, None, 14, None, 20]
}

df= pd.DataFrame(data)
print(f'Before applyng Interpolate:\n{df}')

df['Value']=df['Value'].interpolate(method='polynomial', order=2)
print('\nAfter applying Interpolation with linear ')
print(df)