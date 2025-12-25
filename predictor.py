# predictor.py

import pickle
import pandas as pd

# Load the trained model
with open("student_model.pkl", "rb") as f:
    model = pickle.load(f)

print("\n--- Student Performance Prediction ---")

# Input from user
attendance = float(input("Enter attendance: "))
study_hours = float(input("Enter study hours: "))
internal_marks = float(input("Enter internal marks: "))

# Create DataFrame with the same column names as used during training
student = pd.DataFrame([[attendance, study_hours, internal_marks]],
                       columns=["attendance", "study_hours", "internal_marks"])

# Predict
result = model.predict(student)[0]

# Show PASS or FAIL
print(f"RESULT: {'PASS' if result == 1 else 'FAIL'}")
