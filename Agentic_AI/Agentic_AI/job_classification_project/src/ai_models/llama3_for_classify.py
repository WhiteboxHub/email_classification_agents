import os
from langchain_groq import ChatGroq

class LLMSelector:
    def __init__(self):
        # Initialize the Llama2 model with the Groq API key
        grog_api_key = "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"
        self.llm = ChatGroq(model="llama3-70b-8192", api_key=grog_api_key)

    def generate_response(self, prompt):
        # Generate a response using the Llama2 model
        return self.llm.invoke(prompt)

# Example usage
selector = LLMSelector()
# response = selector.generate_response("Hello, how are you?")
# print(response)



from langchain_core.output_parsers import StrOutputParser
import os 
import sys 
# dataset.py
import json


from langchain_core.prompts import ChatPromptTemplate

class PromptEngineering:
    @staticmethod
    def get_interview_prompt():
        return ChatPromptTemplate.from_messages([
            ("system", """you are an classifier just read the content from the mails and just classify them in JObs in 
             [Ml ,UI ,QA] jobs by identifying the Keywords related to each Domain.
             dont provide and other information just the classifcation of the job type thats it

             example:
             mail:--  got the job opprtunity from google for ml engineer at location hyderabad 
             answer:-- ML
                """),
            ("human", "{question}")
        ])

    


class LLMPipeline:
    def __init__(self):
        self.llm_selector = LLMSelector()
        self.prompt_engineering = PromptEngineering()

    def ask_question(self, question):
        prompt_template = self.prompt_engineering.get_interview_prompt()
        formatted_prompt = prompt_template.format(question=question)
        response = self.llm_selector.generate_response(formatted_prompt)
        return response

if __name__ == "__main__":
    llm_pipeline = LLMPipeline()
    response = llm_pipeline.ask_question("""Dear [Candidate's Name],

c""")
    
    structure_output = StrOutputParser()
    print(structure_output.invoke(response))