import pandas as pd
import joblib

# Load saved model
model = joblib.load("fraud_model.pkl")

# Load dataset
data = pd.read_csv("creditcard.csv")

# Select a sample transaction
sample = data.drop("Class", axis=1).iloc[[100]]

# Actual result
actual = data["Class"].iloc[100]

# Predict
prediction = model.predict(sample)

print("Actual Class :", actual)

if prediction[0] == 1:
    print("Prediction : FRAUD TRANSACTION")
else:
    print("Prediction : GENUINE TRANSACTION")
