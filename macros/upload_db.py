#%%
from sqlalchemy import create_engine
import pandas as pd

engine=create_engine("postgresql+psycopg2://postgres:nova@localhost:5432/projeto")

df = pd.read_csv('seeds/walmart.csv')

columns = [x.replace(' ','_').lower() for x in df.columns]
df.columns = columns

print(df.isna().sum())
duplicateRows = df[df.duplicated(keep='last')]
print(duplicateRows)

df.to_sql('walmart', engine, if_exists= 'replace', index= False)

engine.dispose()