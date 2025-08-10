import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import LabelEncoder


url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
df = pd.read_csv(url)


le_smoker = LabelEncoder()
df['smoker'] = le_smoker.fit_transform(df['smoker'])

le_region = LabelEncoder()
df['region'] = le_region.fit_transform(df['region'])

X = df[['age', 'bmi', 'children', 'smoker', 'region']]
y = df['charges']


model = Ridge(alpha=1.0)
model.fit(X, y)


joblib.dump(model, "ridge_insurance_model.pkl")
joblib.dump(le_smoker, "smoker_encoder.pkl")
joblib.dump(le_region, "region_encoder.pkl")
