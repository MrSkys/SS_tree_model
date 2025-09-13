import pandas as pd
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('.\stores.csv')
store_data = df.dropna()
model = DecisionTreeRegressor 

unique_cities = store_data['city'].unique()
city_map = {city: idx for idx, city in enumerate(unique_cities)}
store_data['city'] = store_data['city'].map(city_map)

unique_state = store_data['state'].unique()
state_map = {state: idx for idx, state in enumerate(unique_state)}
store_data['state'] = store_data['state'].map(state_map) 

unique_type = store_data['type'].unique()
type_map = {type: idx for idx, type in enumerate(unique_type)}
store_data['type'] = store_data['type'].map(type_map)
print(store_data)

# Name of the city with code 0
#d = {'Quito':0,'Santo Domingo':1,'Cayambe':2, 'Latacunga':3,'Riobamba':4,'Ibarra':5 ,'Puyo':6,'Guayaquil':7,'Daule':8,
#'Babahoyo':9,'Loja':10, 'Salinas':11, 'Ambato':12,'Guaranda':13,'Quevedo':14,'Playas':15,'Libertad':16,'Cuenca':17,'Machala':18,'Manta':19,'El Carmen':20,'Esmeraldas':21}
#store_data['city']=store_data['city'].map(d)
#print(store_data.to_string)