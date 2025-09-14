import pandas as pd
#from sklearn.tree import DecisionTreeRegressor
#from sklearn.metrics import mean_absolute_error
#from sklearn.model_selection import train_test_split

#read and clean data

'''
#most previus code (WITHOUT DRY principle)

unique_cities = stores_data['city'].unique()
city_map = {city: idx for idx, city in enumerate(unique_cities)}
stores_data['city'] = stores_data['city'].map(city_map)

unique_state = stores_data['state'].unique()
state_map = {state: idx for idx, state in enumerate(unique_state)}
stores_data['state'] = stores_data['state'].map(state_map) 

unique_type = stores_data['type'].unique()
type_map = {type: idx for idx, type in enumerate(unique_type)}
stores_data['type'] = stores_data['type'].map(type_map)

'''


# previous(hardcoded and unfinished)

#df = pd.read_csv('stores.csv')
#df = pd.read_csv('transactions.csv')
#df = pd.read_csv('train.csv')

#present(simple , DRY and finished?)
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
for col in ['city', 'state', 'type']:
    stores_data[col] = stores_data[col].map({val: i for i, val in enumerate(stores_data[col].unique())})


transa = data["transa"]
train = data["train"]

'''
features = []
X = features
y = train['sales']
train_X, val_X, train_y,val_y= train_test_split(X,y,random_state=0)

#define model
model = DecisionTreeRegressor 

#fit and test model
model.fit(train_X, train_y)
sales_predict = model.predict(val_X)
print(mean_absolute_error(val_y,sales_predict))
'''