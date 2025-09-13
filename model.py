import pandas as pd
from sklearn.tree import DecisionTreeRegressor

#define model
model = DecisionTreeRegressor 

#read and clean data
df = pd.read_csv('.\stores.csv')
store_data = df.dropna(axis=0)

#previus code (WITHOUT DRY principle)
'''
unique_cities = store_data['city'].unique()
city_map = {city: idx for idx, city in enumerate(unique_cities)}
store_data['city'] = store_data['city'].map(city_map)

unique_state = store_data['state'].unique()
state_map = {state: idx for idx, state in enumerate(unique_state)}
store_data['state'] = store_data['state'].map(state_map) 

unique_type = store_data['type'].unique()
type_map = {type: idx for idx, type in enumerate(unique_type)}
store_data['type'] = store_data['type'].map(type_map)
'''

#NEW code (WITH DRY principle)

for col in ['city', 'state', 'type']:
    store_data[col] = store_data[col].map({val: i for i, val in enumerate(store_data[col].unique())})

print(store_data)
