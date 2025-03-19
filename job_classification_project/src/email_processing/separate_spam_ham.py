import pandas as pd
import joblib

model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

df = pd.read_csv("/Users/innovapathinc/Downloads/Agentic_AI/Agentic_AI/job_classification_project/data/emails.csv")  # Replace with your actual CSV filename

print(df.head())


df['Subject'] = df['Subject'].fillna("")
df['Body'] = df['Body'].fillna("")

df['Full_Text'] = df['Subject'] + " " + df['Body']

X = vectorizer.transform(df['Full_Text'])

df['Prediction'] = model.predict(X)

df['Prediction'] = df['Prediction'].map({1: "Spam", 0: "Ham"})

print(df[['Sender', 'Subject', 'Prediction']])

df[df['Prediction'] == "Spam"].to_csv("spam_emails.csv", index=False)

df[df['Prediction'] == "Ham"].to_csv("ham_emails.csv", index=False)

print("Spam and Ham emails saved successfully!")
