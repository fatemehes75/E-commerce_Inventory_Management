import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle  # Add this import

# Create synthetic data
np.random.seed(42)  # For reproducibility
n_samples = 1000
data = {
    'Date': pd.date_range(start='2022-01-01', periods=n_samples, freq='D'),
    'Year': np.random.randint(2020, 2023, size=n_samples),
    'Month': np.random.randint(1, 13, size=n_samples),
    'Day': np.random.randint(1, 32, size=n_samples),
    'Inventory Level': np.random.randint(1, 101, size=n_samples),
    'Sales': np.random.randint(1, 101, size=n_samples)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Feature engineering (e.g., extracting date-related features)
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Split data into features (X) and target (y)
X = df[['Year', 'Month', 'Day', 'Inventory Level']]
y = df['Sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a machine learning model (Random Forest Regressor)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model to a file
with open('/Users/fati/PycharmProjects/inventory_management/models/model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
