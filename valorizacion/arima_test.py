import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.preprocessing import StandardScaler

def GetCsvData():
    file_path1 = 'D:\Integrador2_pr\proyecto\\valorizacion\csv\medellin_properties_with_ids.csv'
    file_path2 = 'D:\Integrador2_pr\proyecto\\valorizacion\csv\price_history_simulated.csv'

    df_properties = pd.read_csv(file_path1)
    df_price_history = pd.read_csv(file_path2)


    df_price_history['year'] = pd.to_datetime(df_price_history['year'], format='%Y')
    df_price_history.set_index(['id', 'year'], inplace=True)

    df_price_history = df_price_history.sort_index()

    df_price_history = df_price_history[df_price_history['price'] < 1100000000]

    df_properties['latitude'] = pd.to_numeric(df_properties['latitude'], errors='coerce')
    df_properties['longitude'] = pd.to_numeric(df_properties['longitude'], errors='coerce')
    df_properties['garages'] = pd.to_numeric(df_properties['garages'], errors='coerce')
    df_properties['neighbourhood'] = df_properties['neighbourhood'].astype('string')

    merged_data = pd.merge(df_price_history.reset_index(), df_properties, on='id')
    merged_data.set_index('year', inplace=True)
    merged_data_cleaned = merged_data.dropna()

    return merged_data_cleaned


def GetModelData(data, neighbourhood):
    new_data = data[data['neighbourhood'] == neighbourhood].copy()

    if new_data.empty:
        print(f"No data avaliable for the neighbourhood: {neighbourhood}")
        return 
    return new_data

def ArimaxPrediction(user_data_dict, merged_data):
    user_data = pd.DataFrame([user_data_dict])

    print(user_data.head())

    user_neighbourhood = user_data['neighbourhood'].iloc[0]

    neighbourhood_data = GetModelData(merged_data, user_neighbourhood)

    if neighbourhood_data.empty:
        return
    
    #neighbourhood_data.set_index('date', inplace=True)

    target_ts = neighbourhood_data['price_x']

    exog_vars = neighbourhood_data[['rooms','baths','area','age','garages','stratum']] #'latitude','longitude',

    scaler_price = StandardScaler()
    target_ts_scaled = scaler_price.fit_transform(target_ts.values.reshape(-1,1)).flatten()

    scaler_exog = StandardScaler()
    exog_vars_scaled = scaler_exog.fit_transform(exog_vars)
    
    target_ts_diff = np.diff(target_ts_scaled)

    model = SARIMAX(target_ts_diff, exog=exog_vars_scaled[:-1], order=(1,1,1))
    model_fit = model.fit(disp=False)


    user_exog_vars = user_data[['rooms','baths','area','age','garages','stratum']] #'latitude','longitude',

    user_exog_vars_replicated = pd.concat([user_exog_vars]*5, ignore_index=True)

    user_exog_vars_scaled = scaler_exog.transform(user_exog_vars_replicated)


    predictions_diff = model_fit.forecast(steps=5, exog=user_exog_vars_scaled)

    predictions_scaled = np.r_[target_ts_scaled[-1], predictions_diff].cumsum()

    predictions = scaler_price.inverse_transform(predictions_scaled.reshape(-1,1)).flatten()

    print(f"Predictios for the user's property in neighbourhood {user_neighbourhood}")
    print(predictions)

    
    '''neighbourhood_data.info()
    print(neighbourhood_data.index)'''
    return predictions

'''
def TestTolerance(property_id, merged_data):

    property_data = merged_data[merged_data['id'] == property_id]


    if property_data.empty:
        return

    property_neighbourhood = property_data['neighbourhood'].iloc[0]

    neighbourhood_data = GetModelData(merged_data, property_neighbourhood)

    if neighbourhood_data.empty:
        return
    
    #neighbourhood_data.set_index('date', inplace=True)

    target_ts = neighbourhood_data['price_x']

    exog_vars = neighbourhood_data[['rooms','baths','area','age','garages','stratum']] #'latitude','longitude',

    scaler_price = StandardScaler()
    target_ts_scaled = scaler_price.fit_transform(target_ts.values.reshape(-1,1)).flatten()

    scaler_exog = StandardScaler()
    exog_vars_scaled = scaler_exog.fit_transform(exog_vars)
    
    target_ts_diff = np.diff(target_ts_scaled)

    model = SARIMAX(target_ts_diff, exog=exog_vars_scaled[:-1], order=(1,1,1))
    model_fit = model.fit(disp=False)


    property_exog_vars = property_data[['rooms','baths','area','age','garages','stratum']] #'latitude','longitude',

    property_exog_vars = property_exog_vars[0:5]
    #property_exog_vars_replicated = pd.concat([property_exog_vars]*5, ignore_index=True)

    property_exog_vars_scaled = scaler_exog.transform(property_exog_vars)


    predictions_diff = model_fit.forecast(steps=5, exog=property_exog_vars_scaled)

    predictions_scaled = np.r_[target_ts_scaled[-1], predictions_diff].cumsum()

    predictions = scaler_price.inverse_transform(predictions_scaled.reshape(-1,1)).flatten()

    actual_price = property_data['price_x'].iloc[0]

    difference = abs((predictions[0]-actual_price)/actual_price)*100

    print(f"Difference: {difference:.2f}")
    

    return predictions
'''
#data = GetCsvData()

'''user_data_dict = {
    'neighbourhood': 'Laureles',
    'rooms': 3,
    'baths': 2,
    'garages': 1,
    'latitude':6.1862025,
    'longitude':-75.5994371,
    'area': 80,
    'administration_price': 250000,
    'age': 1,
    'stratum': 4,
    'year': 2024

}

prediction = ArimaxPrediction(user_data_dict, data)

'''#test = TestTolerance(40, data)

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