import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX


def GetCsvData():
    file_path1 = 'D:\Integrador2_pr\\arima-test\medellin_properties_with_ids.csv'
    file_path2 = 'D:\Integrador2_pr\\arima-test\price_history_simulated.csv'

    df_properties = pd.read_csv(file_path1)
    df_price_history = pd.read_csv(file_path2)


    df_price_history['year'] = pd.to_datetime(df_price_history['year'], format='%Y')
    df_price_history.set_index(['id', 'year'], inplace=True)

    df_price_history = df_price_history.sort_index()


    df_properties['latitude'] = pd.to_numeric(df_properties['latitude'], errors='coerce')
    df_properties['longitude'] = pd.to_numeric(df_properties['longitude'], errors='coerce')
    df_properties['garages'] = pd.to_numeric(df_properties['garages'], errors='coerce')
    df_properties['neighbourhood'] = df_properties['neighbourhood'].astype('string')

    #df_properties_info = df_properties.info()
    #df_price_history_info = df_price_history.info()

    #df_properties_head = df_properties.head()
    #df_price_history_head = df_price_history.head()

    #df_properties_info, df_properties_head, df_price_history_info, df_price_history_head

    merged_data = pd.merge(df_price_history.reset_index(), df_properties, on='id')
    merged_data.set_index('year', inplace=True)
    merged_data_cleaned = merged_data.dropna()

    merged_data_info = merged_data_cleaned.info()
    merged_data_cleaned

    print(merged_data_cleaned.index)
    
    return merged_data_cleaned


def GetModelData(data, neighbourhood):
    new_data = data[data['neighbourhood'] == neighbourhood].copy()

    if new_data.empty:
        print(f"No data avaliable for the neighborhood: {neighbourhood}")
        return 
    return new_data

def ArimaxPrediction(user_data_dict, merged_data):
    user_data = pd.DataFrame([user_data_dict])

    user_neighborhood = user_data['neighborhood'].iloc[0]

    neighborhood_data = GetModelData(merged_data, user_neighborhood)

    if neighborhood_data.empty:
        return
    
    #neighborhood_data.set_index('date', inplace=True)

    target_ts = neighborhood_data['price_x']

    exog_vars = neighborhood_data[['rooms','baths','area','age','garages','stratum']] #'latitude','longitude',

    model = SARIMAX(target_ts, exog=exog_vars, order=(1,1,1))
    model_fit = model.fit(disp=False)

    user_exog_vars = user_data[['rooms','baths','area','age','garages','stratum']] #'latitude','longitude',

    predictions = model_fit.forecast(steps=len(user_data), exog=user_exog_vars)

    print(f"Predictios for the user's property in neighborhood {user_neighborhood}")
    print(predictions)

    
    '''neighborhood_data.info()
    print(neighborhood_data.index)'''
    return predictions

data = GetCsvData()

user_data_dict = {
    'neighborhood': 'Laureles',
    'rooms': 3,
    'baths': 2,
    'garages': 1,
    'latitude':6.1862025,
    'longitude':-75.5994371,
    'area': 80,
    'administration_price': 250000,
    'age': 1,
    'stratum': 4,
    'year': 2023

}

print(data[data['neighbourhood'] == 'Laureles'])
prediction = ArimaxPrediction(user_data_dict, data)


#merged_data_head = merged_data_cleaned.head()

#print(merged_data_cleaned.dtypes)
#print(merged_data_cleaned.isnull().sum())
#print(merged_data_cleaned.head(20))
'''
target = merged_data_cleaned['price_x'] #historical prices
exog_vars = merged_data_cleaned[['latitude','longitude','rooms','baths','area','age','garages','stratum']] #'administration_price',  'neighbourhood' exogen variables 'property_type', 'neighbourhood',

#Split into training data (80%) and test data (20%)


train_size = int(len(target) * 0.8)
train_target, test_target = target[:train_size], target[train_size:]
train_exogen, test_exogen = exog_vars[:train_size], exog_vars[train_size:]

#ARIMAX model
model = SARIMAX(train_target, exog=train_exogen, order=(1,1,1))
model_fit = model.fit(disp=False)

#generate predictions ont the test set
predictions = model_fit.forecast(steps=len(test_target), exog=test_exogen)


print(predictions[:5])
print(test_target[:5])
'''