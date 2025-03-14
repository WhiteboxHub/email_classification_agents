import smtplib
from email.mime.text import MIMEText
from typing import Optional

def send_email(to_email : str,email_data : str,subject : Optional[str] = "email categoriezed based on the content from body."):
    """Send an email using SMTP."""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "junaidfaizan024@gmail.com"
    sender_password = "kaymeqsbvbpjtwjw" 

    msg = MIMEText(email_data)
    msg["email_data"] =email_data
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print(f"Email sent to {to_email} with subject: {email_data}")
    except Exception as e:
        print(f"Error sending email: {e}")


# send_email('khajaaka@gmail.com',"this is a test case test case.................")