# AI Student Performance Predictor

## 📌 Project Description
This project predicts whether a student will **PASS or FAIL** based on:
- Attendance
- Study hours
- Internal marks

The project integrates **C programming** for data collection and **Python Machine Learning** for prediction.

---

## 🛠 Technologies Used
- C Programming
- Python
- Pandas
- Scikit-learn
- Machine Learning

---

## 📂 Project Structure
- `input_data.c` – C program to take student input and store it in CSV
- `student_data.csv` – Dataset used for training
- `train_model.py` – Trains the machine learning model
- `predictor.py` – Predicts PASS / FAIL
- `trained_model.pkl` – Saved trained model

---

## 🚀 How to Run the Project

### 1️⃣ Run C Program
```bash
gcc input_data.c -o input
input.exe
2️⃣ Train the Model (Run once)
bash
Copy code
python train_model.py
3️⃣ Predict Student Result
bash
Copy code
python predictor.py
📊 Sample Output
--- Student Performance Prediction ---
Enter attendance: 80
Enter study hours: 15
Enter internal marks: 30

RESULT: PASS

👤 Author
Chaitanya
B.Tech 1st Year Student
