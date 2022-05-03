import pandas as pd

filePath = r'220503\university\고등교육기관 하반기 주소록(2021).xlsx'
df_from_excel = pd.read_excel(filePath, engine='openpyxl')

df_from_excel.columns = df_from_excel.loc[4].to_list()

df_from_excel = df_from_excel.drop(index=list(range(0, 5)))

print(df_from_excel.head())
print(df_from_excel['학교명'].values)
print(df_from_excel['주소'].values)