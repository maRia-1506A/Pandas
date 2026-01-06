import pandas as pd

data={
    'Index': [0,1,2,3,4],
    'Value': [5, None, 14, None, 20]
}

df= pd.DataFrame(data)
print(f'Before applyng Interpolate:\n{df}')

df['Value']= df['Value'].interpolate(method='linear')
print('\nAfter applying Interpolation with linear ')
print(df)

'''
Change in value  14-5= 9
Index gap  2-0=2
Change per step  9/2=4
so, Index 1 = 5 + 4 = 9
'''