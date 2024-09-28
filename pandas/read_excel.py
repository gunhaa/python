import pandas as pd

name = 'C:\workspace\99_python\pandas\sample_order.xlsx'

df =pd.read_excel(name)


df.loc[2, '받는고객'] = '최민혁(광주)'
df.loc[2, '받는고객전화번호'] = '010-9355-0049'



print(df)
#df.to_excel('result1.xlsx')