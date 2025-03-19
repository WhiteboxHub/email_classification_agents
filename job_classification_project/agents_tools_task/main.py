# from crewai import Crew
# from task import classify_jobs_task
# from agent import job_classifier_agent, ml_forward_agent, ui_forward_agent
from tools import send_email
from imap_client import fetch_emails
from llama3_for_classify import classify_job

# Function to execute the email classification and forwarding
def process_emails():
    """Fetch, classify, and forward job emails."""
    emails = fetch_emails()  # Get unread emails
    
    for email in emails:
        email_data = f"subject: {email['subject']} body: {email['body']}"
        print(email_data)
        job_type = classify_job(email_data) 
        print(job_type)
       
        # """

        if job_type == "ML":
            send_email("pathan@gmail.com", email["body"], email["subject"])
            print(f"ML job email sent to Pathan: {email['subject']}")

        elif job_type == "UI":
            
            print(email['subject'] , "------------\n \n \n", email['body'])
            send_email("peter@gmail.com", email["body"], email["subject"])
            print(f"UI job email sent to Peter: {email['subject']}")

        else:
            print(f"Unknown job type detected: {job_type}")

if __name__ == "__main__":
    # Define a Crew with all agents
    # crew = Crew(agents=[job_classifier_agent, ml_forward_agent, ui_forward_agent], tasks=[classify_jobs_task])

    # Start email processing
    print("Fetching and processing job emails...")
    process_emails()

    # Execute CrewAI workflow
    # crew.kickoff()
    print("Email classification and forwarding complete!")
