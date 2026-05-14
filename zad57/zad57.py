import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('~/Downloads/Auto.csv', na_values='?')
df = df.dropna()
df['origin'] = df['origin'].astype('category')

train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

print(f"Data ready. Training: {train_df.shape[0]} rows, Validation: {val_df.shape[0]} rows.\n")

print('a)')
model_a = smf.ols('mpg ~ horsepower', data=train_df).fit()
print(model_a.summary())
print("\n")


print('b)')
model_b1 = smf.ols('mpg ~ weight + cylinders + displacement + origin', data=train_df).fit()

model_b2 = smf.ols('mpg ~ weight * horsepower', data=train_df).fit()

model_b3 = smf.ols('mpg ~ I(np.log(weight)) + horsepower + I(horsepower**2)', data=train_df).fit()

print(f"Adjusted R-squared Model B1 (many features): {model_b1.rsquared_adj:.3f}")
print(f"Adjusted R-squared Model B2 (interaction):    {model_b2.rsquared_adj:.3f}")
print(f"Adjusted R-squared Model B3 (transformation): {model_b3.rsquared_adj:.3f}")

print('generalization errors')

def get_validation_mse(model, validation_data):
    predictions = model.predict(validation_data)
    mse = mean_squared_error(validation_data['mpg'], predictions)
    return mse

mse_a = get_validation_mse(model_a, val_df)
mse_b1 = get_validation_mse(model_b1, val_df)
mse_b2 = get_validation_mse(model_b2, val_df)
mse_b3 = get_validation_mse(model_b3, val_df)

print(f"MSE Model A (horsepower only):         {mse_a:.2f}")
print(f"MSE Model B1 (many features + origin):  {mse_b1:.2f}")
print(f"MSE Model B2 (weight*horsepower):       {mse_b2:.2f}")
print(f"MSE Model B3 (logs and powers):         {mse_b3:.2f}")

wyniki = [
    (mse_a, 'A'), 
    (mse_b1, 'B1'), 
    (mse_b2, 'B2'), 
    (mse_b3, 'B3')
]