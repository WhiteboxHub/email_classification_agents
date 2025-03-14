
from crewai import Task
from agent import job_classifier_agent, ml_forward_agent, ui_forward_agent
from imap_client import fetch_emails  
from tools import send_email  
from llama3_for_classify import classify_job  


def classify_and_forward():
    """Fetch emails, classify them using Llama3, and forward accordingly."""
    emails = fetch_emails()  

    for email in emails:
        email_data = f"subject: {email['subject']} body: {email['body']}"
        classification = classify_job(email_data) 
        
        if classification == "ML":
            ml_forward_agent.execute({"email": email})  
            email_data=f"body : {email['body']},sender : {email['sender']} ,subject:{email['subject']}"
            send_email("pathan@example.com",email_data) 
        elif classification == "UI":
            ui_forward_agent.execute({"email": email})  
            send_email("peter@example.com",email["body"],email["subject"])  


classify_jobs_task = Task(
    description="Read emails and classify job type",
    expected_output="ML or UI classification for each email",
    agent=job_classifier_agent,
    function=classify_and_forward
)


# Task to forward ML jobs
forward_ml_task = Task(
    description="Forward ML jobs to Pathan",
    expected_output="ML job email sent to Pathan",
    agent=ml_forward_agent
)

# Task to forward UI jobs
forward_ui_task = Task(
    description="Forward UI jobs to Peter",
    expected_output="UI job email sent to Peter",
    agent=ui_forward_agent
)
