import pandas as  pd
import re
df=pd.read_excel("patrs.xlsx",sheet_name=3)
for ro in df:
    f=re.findall('[0-9]+',ro)
print(f)
