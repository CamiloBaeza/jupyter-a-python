#!/usr/bin/env python3
## Built from download.ipynb by nbtopy ##

# %%
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

# %%
!pip3 install -U nbtopy

# %%
!nbtopy test.ipynb
