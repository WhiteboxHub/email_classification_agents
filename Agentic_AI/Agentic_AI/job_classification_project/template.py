import os

base_dir = "job_classification_project"

# Define the folder structure
folders = {
    "data": ["raw_emails", "processed_emails", "labeled_emails", "model_weights"],
    "src": {
        "email_processing": ["gmail_api.py", "outlook_api.py", "imap_client.py", "email_preprocessor.py"],
        "ai_models": ["bert_classifier.py", "langgraph_agent.py", "crewai_agent.py", "parsing_agent.py"],
        "orchestration": ["main_controller.py", "workflow_manager.py"],
        "storage": ["postgres_client.py", "mongodb_client.py", "pinecone_client.py"],
        "automation": ["slack_notifier.py", "google_sheets.py", "auto_reply.py"],
        "utils": ["config.py", "logger.py"]
    },
    "tests": ["test_email_processing.py", "test_ai_models.py", "test_orchestration.py", "test_storage.py", "test_automation.py"],
    "notebooks": ["data_exploration.ipynb", "model_training.ipynb"]
}

# Create the base directory
os.makedirs(base_dir, exist_ok=True)

# Function to create directories and files
def create_structure(base, structure):
    for key, value in structure.items():
        path = os.path.join(base, key)
        os.makedirs(path, exist_ok=True)
        if isinstance(value, list):
            # Create empty files
            for file in value:
                file_path = os.path.join(path, file)
                open(file_path, 'a').close()
        elif isinstance(value, dict):
            # Recursively create subdirectories
            create_structure(path, value)

# Create the folder structure
create_structure(base_dir, folders)

# Create additional files in the base directory
additional_files = ["requirements.txt", "README.md", ".gitignore"]
for file in additional_files:
    open(os.path.join(base_dir, file), 'a').close()

print("Folder structure created successfully!")
