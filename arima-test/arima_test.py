import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

file_path1 = 'D:\Integrador2_pr\\arima-test\medellin_properties_with_ids.csv'
file_path2 = 'D:\Integrador2_pr\\arima-test\price_history_simulated.csv'

df_properties = pd.read_csv(file_path1)
df_price_history = pd.read_csv(file_path2)


df_price_history['year'] = pd.to_datetime(df_price_history['year'], format='%Y')
df_price_history.set_index('year', inplace=True)


df_properties['latitude'] = pd.to_numeric(df_properties['latitude'], errors='coerce')
df_properties['longitude'] = pd.to_numeric(df_properties['longitude'], errors='coerce')
df_properties['garages'] = pd.to_numeric(df_properties['garages'], errors='coerce')

#df_properties_info = df_properties.info()
#df_price_history_info = df_price_history.info()

#df_properties_head = df_properties.head()
#df_price_history_head = df_price_history.head()

#df_properties_info, df_properties_head, df_price_history_info, df_price_history_head

merged_data = pd.merge(df_price_history, df_properties, on='id')

merged_data_cleaned = merged_data.dropna()

#merged_data_info = merged_data_cleaned.info()
merged_data_head = merged_data_cleaned.head()

#print(merged_data_cleaned.dtypes)
#print(merged_data_cleaned.isnull().sum())
#print(merged_data_head)

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
