from crewai import Agent
from tools import send_email
from llama3_for_classify import classify_job
from crewai.tools import  BaseTool  

class ClassifyJobTool(BaseTool):
    def execute(self, email_data):
        """Execute the classification tool."""
        return classify_job(email_data)


# Agent to classify jobs from emails
job_classifier_agent = Agent(
    role="Job Classifier",
    goal="Classify job emails into ML or UI categories",
    backstory="An AI agent that scans emails and determines job categories.",
    tools=[ClassifyJobTool()] 
)

# Agent to forward ML jobs to Pathan
ml_forward_agent = Agent(
    role="ML Job Forwarder ",
    goal="Forward ML job emails to Pathan",
    backstory="An AI agent that receives ML job emails and sends them to Pathan.",
    tools=[send_email]
)

# Agent to forward UI jobs to Peter
ui_forward_agent = Agent(
    role="UI Job Forwarder",
    goal="Forward UI job emails to Peter",
    backstory="An AI agent that receives UI job emails and sends them to Peter.",
    tools=[send_email]
)
print("done")