from crewai import Agent, Task, Crew
from transformers import pipeline
import pandas as pd

# Load CSV file
df = pd.read_csv("/Users/innovapathinc/Downloads/Agentic_AI/Agentic_AI/job_classification_project/data/emails.csv")  # Replace with actual file name

# Load Pretrained BERT-based Classification Model
classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

# Agent: Reads Emails
class ReaderAgent(Agent):
    def run(self):
        emails = df[["Subject", "Body"]].astype(str).apply(lambda x: " ".join(x), axis=1)
        return emails.tolist()

# Agent: Classifies Emails
class ClassifierAgent(Agent):
    def run(self, emails):
        categories = {"ml": "ML", "ui": "UI", "qa": "QA"}
        results = [classifier(email)[0]["label"].lower() for email in emails]
        return [categories.get(label, "Unknown") for label in results]

# Agent: Stores Classified Data
class StorageAgent(Agent):
    def run(self, emails, labels):
        df["Category"] = labels
        df.to_csv("classified_emails.csv", index=False)
        return "Classification Completed!"
