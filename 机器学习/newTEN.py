import pandas as pd

df_new = pd.read_table('data/news_tensite.dat', encoding='GBK')
df_new = df_new.dropna()
print(df_new)
