import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class LLMSelector:
    def __init__(self):
        """Initialize Llama3 with API Key"""
        self.api_key = os.getenv("GROQ_API_KEY")  
        self.llm = ChatGroq(model="llama3-70b-8192", api_key=self.api_key)

    def generate_response(self, prompt):
        """Generate classification response from Llama3"""
        return self.llm.invoke(prompt)

class JobClassifier:
    def __init__(self):
        self.llm_selector = LLMSelector()
        self.output_parser = StrOutputParser()

    def classify_job(self, email_content):
        """Classifies email content as ML, UI, or QA"""
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """You are a job classifier. Read the email content and classify it as one of:  
            - ML (Machine Learning)  
            - UI (User Interface)  
            - QA (Quality Assurance)  
            Only return the classification label.  

            Example:  
            Email: 'Exciting opportunity for an ML Engineer at Google, Hyderabad.'  
            Output: ML  
            """),
            ("human", "{question}")
        ])
        
        formatted_prompt = prompt_template.format(question=email_content)
        response = self.llm_selector.generate_response(formatted_prompt)

        return self.output_parser.invoke(response).strip()  # Clean response



def classify_job(email_body):
    classifier = JobClassifier()
    return classifier.classify_job(email_body)

#  Example test
if __name__ == "__main__":
    test_email = "We have a new llm engineer  position available at Microsoft!"
    print(classify_job(test_email))  # Expected Output: "UI"
