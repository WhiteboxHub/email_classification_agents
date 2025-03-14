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

# Download NLTK stopwords
nltk.download('stopwords')
nltk.download('punkt_tab')

# # Sample DataFrame for demonstration
# data = {
#     'message': [
#         "Hello! This is a sample message with numbers 123 and punctuation!",
#         "Another example: removing stopwords, numbers, and symbols."
#     ]
# }
# df = pd.DataFrame(data)

def clean_text(text):
    text = text.lower()  # Lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    words = word_tokenize(text)  # Tokenize
    words = [word for word in words if word not in stopwords.words('english')]  # Remove stopwords
    return " ".join(words)

# Apply the cleaning function to the DataFrame
df['cleaned_message'] = df['message'].apply(clean_text)

# Display the cleaned messages
print(df[['message', 'cleaned_message']])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned_message'])  # Transform text data into vectors
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Print accuracy and classification report
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred))


import joblib
# Save the trained Naïve Bayes model
joblib.dump(model, "spam_classifier_model.pkl")

# Save the fitted TF-IDF vectorizer
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("Model and vectorizer saved successfully!")


# Load the trained model
loaded_model = joblib.load("spam_classifier_model.pkl")

# Load the TF-IDF vectorizer
loaded_vectorizer = joblib.load("tfidf_vectorizer.pkl")

print("Model and vectorizer loaded successfully!")


def predict_spam(text):
    # Convert text to TF-IDF feature representation
    text_vectorized = loaded_vectorizer.transform([text])

    # Predict using the trained model
    prediction = loaded_model.predict(text_vectorized)

    return "Spam" if prediction[0] == 1 else "Ham"

# Example usage
new_message = "let schedule a meet for further round snext week "
print(f"Message: {new_message}")
print(f"Prediction: {predict_spam(new_message)}")
