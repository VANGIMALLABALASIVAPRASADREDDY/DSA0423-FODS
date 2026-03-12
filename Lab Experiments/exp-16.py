import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

data = {
    "Age": [45, 50, 36, 62, 29, 41, 55, 48, 33, 60, 39, 52, 47, 58, 31],
    "Gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female", "Male", "Male", "Female", "Female"],
    "Blood_Pressure": [130, 140, 120, 150, 110, 135, 145, 128, 118, 155, 125, 142, 138, 148, 115],
    "Cholesterol": [200, 220, 180, 240, 170, 210, 230, 195, 175, 250, 185, 225, 215, 235, 165],
    "Outcome": ["Good", "Bad", "Good", "Bad", "Good", "Good", "Bad", "Good", "Good", "Bad", "Good", "Bad", "Good", "Bad", "Good"]
}

df = pd.DataFrame(data)

label_encoder = LabelEncoder()
df["Gender"] = label_encoder.fit_transform(df["Gender"])
df["Outcome"] = label_encoder.fit_transform(df["Outcome"])

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print("\nTest Set Predictions:\n")
print(results)
