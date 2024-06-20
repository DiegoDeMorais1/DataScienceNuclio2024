import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# SARIMA Model
def train_sarima_model(train_data):
    try:
        sarima_model = SARIMAX(train_data['value_sales'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 7))
        sarima_result = sarima_model.fit()
        return sarima_result
    except Exception as e:
        print("Error in model fitting:", e)


# Function to forecast sales for a given product_store
def forecast_sales(df, product_store, steps=1):
    # Filter the data for the specified product_store
    product_store_data = df[df['product_store'] == product_store]

    # Get the last available week for the specified product_store
    last_week = product_store_data['week'].max()

    # Train the model using data up to the last available week for the specified product_store
    train_data = product_store_data[product_store_data['week'] < last_week]
    model_sarima = train_sarima_model(train_data)

    # Forecast sales for the specified product_store for the next 'steps' weeks
    forecast = model_sarima.forecast(steps=steps)
    return forecast, product_store_data


def model(product_store):
    df = pd.read_csv('base_SARIMAX.csv')
    del df['Unnamed: 0']
    forecast = forecast_sales(df, product_store, steps=7)
    return forecast
