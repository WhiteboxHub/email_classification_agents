import pandas as pd
import numpy as np
import nltk
import re
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

import pandas as pd

# Use the raw URL to access the CSV file
url = "https://raw.githubusercontent.com/mohitgupta-1O1/Kaggle-SMS-Spam-Collection-Dataset-/master/spam.csv"

# Load the dataset with error handling
df = pd.read_csv(url, encoding="latin-1", on_bad_lines='skip')[['v1', 'v2']]
df.columns = ['label', 'message']  # Rename columns for clarity

# Convert labels to binary values (spam=1, ham=0)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Display the first few rows to verify
print(df.head())

import nltk
import re
import string
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt_tab')



def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)  
    text = text.translate(str.maketrans("", "", string.punctuation))  
    words = word_tokenize(text)  # Tokenize
    words = [word for word in words if word not in stopwords.words('english')]  
    return " ".join(words)

df['cleaned_message'] = df['message'].apply(clean_text)

print(df[['message', 'cleaned_message']])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned_message']) 
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred))


import joblib
joblib.dump(model, "spam_classifier_model.pkl")

joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("Model and vectorizer saved successfully!")


loaded_model = joblib.load("spam_classifier_model.pkl")

loaded_vectorizer = joblib.load("tfidf_vectorizer.pkl")

print("Model and vectorizer loaded successfully!")


def predict_spam(text):
    text_vectorized = loaded_vectorizer.transform([text])

    prediction = loaded_model.predict(text_vectorized)

    return "Spam" if prediction[0] == 1 else "Ham"

new_message = "let schedule a meet for further round snext week "
print(f"Message: {new_message}")
print(f"Prediction: {predict_spam(new_message)}")
