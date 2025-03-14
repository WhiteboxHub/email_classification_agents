import pandas as pd
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

# Load pre-trained BERT model (fine-tuned on job classification)
MODEL_NAME = "bert-base-uncased"  # Replace with actual model path or Hugging Face model

tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
model = BertForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()

# Load email data
csv_file = "/Users/innovapathinc/Downloads/Agentic_AI/Agentic_AI/job_classification_project/data/emails.csv"  # Update with actual CSV file
emails_df = pd.read_csv(csv_file)

# Job categories
categories = ["ML", "UI", "QA"]

# Keyword-based fallback if LLM confidence is low
keywords = {
    "ML": ["pytorch", "tensorflow", "ai", "deep learning", "machine learning"],
    "UI": ["react", "figma", "html", "css", "ux/ui"],
    "QA": ["selenium", "test automation", "software testing"]
}

def classify_email(subject, body):
    text = f"{subject} {body}"
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    scores = softmax(outputs.logits, dim=1).numpy()[0]
    
    # Use LLM classification
    category = categories[scores.argmax()]
    confidence = scores.max()
    
    # Fallback to keyword matching if confidence is low
    if confidence < 0.6:
        for cat, words in keywords.items():
            if any(word in text.lower() for word in words):
                return cat
    
    return category

# Apply classification
emails_df["Category"] = emails_df.apply(lambda row: classify_email(row["Subject"], row["Body"]), axis=1)

# Save results
emails_df.to_csv("classified_emails.csv", index=False)
print("Classification completed and saved!")
