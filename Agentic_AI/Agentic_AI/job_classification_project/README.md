# Email Classification And Forwarding

## Overview
This project implements an email classification system that utilizes BERT and LLaMA3 models to detect classify emails based on different jobs. The system includes data processing, model training, and email retrieval using IMAP and for clasification and email forwarding used Crew AI for Agents.

## Project Structure
```bash
email_classification/
│── agents_tools/
│   ├── agent.py
│   ├── imap_client.py
│   ├── llama3_for_classification.py
│   ├── main.py
│   ├── task.py
│   ├── tools.py
│── data/
│── model/
│── notebooks/
│── src/
│   ├── email_processing/
│   │   ├── __init__.py
│   │   ├── imap_client.py
│   │   ├── predict_spam_output.py
│   │   ├── separate_spam.py
│   ├── Fine_tune_bert/
│   │   ├── bert_model.ipynb
│   │   ├── llama3_classification.ipynb
│   │   ├── test_data.csv
│   │   ├── train_data.csv
│   │   ├── valid_data.csv
│── .gitignore
│── README.md
│── requirements.txt

