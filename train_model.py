# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data (use your correct CSV file name)
data = pd.read_csv("student_data.csv")

# Use the correct column names from your CSV
X = data[["attendance", "study_hours", "internal_marks"]]
y = data["result"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("student_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully")
