# Model training script
import pandas as pd
import json
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.preprocess import clean_text

# Load dataset
data = pd.read_csv('../dataset/complaints.csv')

# Clean text
data['cleaned_text'] = data['complaint_text'].apply(clean_text)

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['cleaned_text'])
y = data['category']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)
# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Generate detailed report
report = classification_report(y_test, y_pred, output_dict=True)

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)

# Accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
pickle.dump(model, open('complaint_model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
# Save evaluation report
with open('model_report.json', 'w') as f:
    json.dump({
        "accuracy": accuracy,
        "classification_report": report,
        "confusion_matrix": cm.tolist()
    }, f)

print("Model report saved successfully!")