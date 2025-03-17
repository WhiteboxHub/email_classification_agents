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

    classifications = []

    for index, row in df.iterrows():
        subject = row.get('Subject', '')
        body = row.get('Body', '')

        email_info = f"Subject: {subject}, Body: {body}"

        response = llm_pipeline.ask_question(email_info)

        classification = structure_output.invoke(response)

        classifications.append(classification)

        print(f"Email {index + 1}: {classification}")

    return classifications

# Example usage
csv_file_path = '/Users/innovapathinc/Downloads/Agentic_AI/emails.csv'
classifications = classify_emails_from_csv(csv_file_path)
