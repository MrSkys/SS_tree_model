import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

#read and clean data

'''
 most previus code (WITHOUT DRY principle)

unique_cities = stores_data['city'].unique()
city_map = {city: idx for idx, city in enumerate(unique_cities)}
stores_data['city'] = stores_data['city'].map(city_map)

unique_state = stores_data['state'].unique()
state_map = {state: idx for idx, state in enumerate(unique_state)}
stores_data['state'] = stores_data['state'].map(state_map) 

unique_type = stores_data['type'].unique()
type_map = {type: idx for idx, type in enumerate(unique_type)}
stores_data['type'] = stores_data['type'].map(type_map)

 Previous(hardcoded and unfinished)

df = pd.read_csv('stores.csv')
df = pd.read_csv('transactions.csv')
df = pd.read_csv('train.csv')
'''

#present(simple , DRY and not hardcoded)

def read_file(path, has_date=True):
    df = pd.read_csv(path).drop_duplicates()
    if has_date and 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], format='mixed')
    return df

files = {
    "stores_data": ("stores.csv", False), 
    "transa": ("transactions.csv", True), 
    "train": ("train.csv", True)
}

data = {name: read_file(path, has_date) for name, (path, has_date) in files.items()}

stores_data = data["stores_data"]
#NEW code (WITH DRY principle)
#a loop wich encodes string into numeric data
for name, df in data.items():
    for col in df.select_dtypes(include=["object"]).columns:
        mapping = {val: i for i, val in enumerate(df[col].unique())}
        df[col] = df[col].map(mapping)

trainDf = data["train"].merge(data["stores_data"], on="store_nbr", how="left")
trainDf['year'] = trainDf['date'].dt.year
trainDf['month'] = trainDf['date'].dt.month
trainDf['dayofweek'] = trainDf['date'].dt.dayofweek

X = trainDf.drop(columns=['sales', 'date'])
y = trainDf['sales']
train_X, val_X, train_y,val_y= train_test_split(X,y,random_state=0)

#define model
model = DecisionTreeRegressor(random_state=0)

#fit and test model

test = pd.read_csv('test.csv')

model.fit(train_X, train_y)
sales_predict = model.predict(val_X)
print(trainDf.info())
#print(mean_absolute_error(val_y,test))
