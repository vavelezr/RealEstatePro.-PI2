import os
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.preprocessing import StandardScaler


def get_csv_data():

    base_dir = os.path.dirname(os.path.abspath(__file__))

    file_path1 = os.path.join(base_dir, "csv", "medellin_properties_with_ids.csv")
    file_path2 = os.path.join(base_dir, "csv", "price_history_simulated.csv")

    df_properties = pd.read_csv(file_path1)
    df_price_history = pd.read_csv(file_path2)

    df_price_history["year"] = pd.to_datetime(df_price_history["year"], format="%Y")
    df_price_history.set_index(["id", "year"], inplace=True)

    df_price_history = df_price_history.sort_index()

    df_price_history = df_price_history[df_price_history["price"] < 1100000000]

    df_properties["latitude"] = pd.to_numeric(
        df_properties["latitude"], errors="coerce"
    )
    df_properties["longitude"] = pd.to_numeric(
        df_properties["longitude"], errors="coerce"
    )
    df_properties["garages"] = pd.to_numeric(df_properties["garages"], errors="coerce")
    df_properties["neighbourhood"] = df_properties["neighbourhood"].astype("string")

    merged_data = pd.merge(df_price_history.reset_index(), df_properties, on="id")
    merged_data.set_index("year", inplace=True)
    merged_data_cleaned = merged_data.dropna()

    return merged_data_cleaned


def get_model_data(data, neighbourhood):
    new_data = data[data["neighbourhood"] == neighbourhood].copy()

    if new_data.empty:
        print(f"No data avaliable for the neighbourhood: {neighbourhood}")
        return new_data
    return new_data


def arimax_prediction(user_data_dict, merged_data):
    user_data = pd.DataFrame([user_data_dict])
    user_neighbourhood = user_data["neighbourhood"].iloc[0]
    neighbourhood_data = get_model_data(merged_data, user_neighbourhood)
    if neighbourhood_data.empty:
        return neighbourhood_data
    # neighbourhood_data.set_index('date', inplace=True)
    target_ts = neighbourhood_data["price_x"]
    exog_vars = neighbourhood_data[
        ["rooms", "baths", "area", "age", "garages", "stratum"]
    ]  #'latitude','longitude',
    scaler_price = StandardScaler()
    target_ts_scaled = scaler_price.fit_transform(
        target_ts.values.reshape(-1, 1)
    ).flatten()
    scaler_exog = StandardScaler()
    exog_vars_scaled = scaler_exog.fit_transform(exog_vars)
    target_ts_diff = np.diff(target_ts_scaled)
    model = SARIMAX(target_ts_diff, exog=exog_vars_scaled[:-1], order=(1, 1, 1))
    model_fit = model.fit(disp=False)
    user_exog_vars = user_data[
        ["rooms", "baths", "area", "age", "garages", "stratum"]
    ]  #'latitude','longitude',
    user_exog_vars_replicated = pd.concat([user_exog_vars] * 5, ignore_index=True)
    user_exog_vars_scaled = scaler_exog.transform(user_exog_vars_replicated)
    predictions_diff = model_fit.forecast(steps=5, exog=user_exog_vars_scaled)
    predictions_scaled = np.r_[target_ts_scaled[-1], predictions_diff].cumsum()
    predictions = scaler_price.inverse_transform(
        predictions_scaled.reshape(-1, 1)
    ).flatten()
    print(f"Predictios for the user's property in neighbourhood {user_neighbourhood}")
    print(predictions)

    return predictions
