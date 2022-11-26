import pandas as pd

# df = pd.DataFrame([[i for i in range(100)], ['a' + str(i) for i in range(100)]])
#
# print(df)
# import pandas as pd

df1 = pd.DataFrame({'number': [i for i in range(100)], 'char': ['a' + str(i) for i in range(100)]})
print(df1.T)
df2 = df1['char'][6]
print(df2)

print(df1.loc[6, 'char']) # .loc can return the elemennt in 6 string in 'char' colomn
print(df1.loc[6:12:3, 'char']) # .loc can return the elements from 6 to 12 strings in char colomn
print(df1.loc[6:12:3, ['char', 'number']])
print(df1.iloc[6:12:3, 1])

print(df1.query('char == "a3"'))
print(df1.loc[df1.char == 'a4'])

# func = lambda x: x + '_course'
df1.char.apply(lambda x: x + '_course')
#lambda x: x + '_course'
print(df1.char.apply(lambda x: x + '_course'))
print(df1.char + 'privet')