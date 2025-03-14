import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from llama3_for_classify import PromptEngineering,LLMSelector
class LLMPipeline:
    def __init__(self):
        self.llm_selector = LLMSelector()
        self.prompt_engineering = PromptEngineering()

    def ask_question(self, question):
        prompt_template = self.prompt_engineering.get_interview_prompt()
        formatted_prompt = prompt_template.format(question=question)
        response = self.llm_selector.generate_response(formatted_prompt)
        return response
def classify_emails_from_csv(csv_file_path):
    df = pd.read_csv(csv_file_path)

    llm_pipeline = LLMPipeline()

    structure_output = StrOutputParser()

    # List to store classifications
    classifications = []

    # Loop through each email in the CSV file
    for index, row in df.iterrows():
        subject = row.get('Subject', '')
        body = row.get('Body', '')

        # Combine subject and body for classification
        email_info = f"Subject: {subject}, Body: {body}"

        # Feed the email info to the LLM
        response = llm_pipeline.ask_question(email_info)

        # Parse the response to get the classification
        classification = structure_output.invoke(response)

        # Store the classification
        classifications.append(classification)

        # Print the classification for each email
        print(f"Email {index + 1}: {classification}")

    return classifications

# Example usage
csv_file_path = '/Users/innovapathinc/Downloads/Agentic_AI/emails.csv'
classifications = classify_emails_from_csv(csv_file_path)
