import pandas as pd

df = pd.read_csv('.\stores.csv')
store_data = df.dropna(axis=0)
print(store_data.to_string()) 