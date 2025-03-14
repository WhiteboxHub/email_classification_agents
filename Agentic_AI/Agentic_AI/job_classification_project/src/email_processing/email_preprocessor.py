import pandas as pd
import joblib

# Load trained model and vectorizer
model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Load emails from CSV
df = pd.read_csv("/Users/innovapathinc/Downloads/Agentic_AI/Agentic_AI/job_classification_project/data/emails.csv")  # Replace with your actual CSV filename

# Check the structure of the file
print(df.head())


# Fill NaN values with empty string
df['Subject'] = df['Subject'].fillna("")
df['Body'] = df['Body'].fillna("")

# Create a new column with combined text
df['Full_Text'] = df['Subject'] + " " + df['Body']

# Transform text using the saved vectorizer
X = vectorizer.transform(df['Full_Text'])

# Predict using the saved model
df['Prediction'] = model.predict(X)

# Convert 1 → Spam, 0 → Ham
df['Prediction'] = df['Prediction'].map({1: "Spam", 0: "Ham"})

# Display results
print(df[['Sender', 'Subject', 'Prediction']])

# Save Spam emails
df[df['Prediction'] == "Spam"].to_csv("spam_emails.csv", index=False)

# Save Ham emails
df[df['Prediction'] == "Ham"].to_csv("ham_emails.csv", index=False)

print("Spam and Ham emails saved successfully!")
