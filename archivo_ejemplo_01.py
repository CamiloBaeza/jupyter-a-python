# %%sadsdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdas
import pandas as pd

url = 'https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv'
df = pd.read_csv(url, index_col=0)

# %%
import random

# %%
str(int(random.random()*10000)) + "_df.csv"

# %%
file_name = str(int(random.random()*10000)) + "_df.csv"

# %%
df.to_csv(file_name,index = False)