import imaplib
import email
from email.header import decode_header
import os

# Email credentials (use environment variables for security)
IMAP_SERVER = "imap.gmail.com"  # Change for other providers
EMAIL_ACCOUNT = "sample@gmail.com"
EMAIL_PASSWORD = "kaymeqsbvbpjtwjw"

def fetch_emails():
    """Fetch unread job emails from inbox"""
    try:
        # Connect to IMAP server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        mail.select("inbox")

        # Search for unread messages
        # status, messages = mail.search(None, "UNSEEN")
        # email_list = []

        # if status == "OK":
        #     for msg_num in messages[0].split():
        #         _, msg_data = mail.fetch(msg_num, "(RFC822)")
        #         for response_part in msg_data:
        #             if isinstance(response_part, tuple):
        #                 msg = email.message_from_bytes(response_part[1])

        #                 # Decode email subject
        #                 subject, encoding = decode_header(msg["Subject"])[0]
        #                 if isinstance(subject, bytes):
        #                     subject = subject.decode(encoding or "utf-8")

        #                 # Extract email body
        #                 if msg.is_multipart():
        #                     for part in msg.walk():
        #                         content_type = part.get_content_type()
        #                         if content_type == "text/plain":
        #                             email_body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
        #                             break
        #                 else:
        #                     email_body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")
        #                 from_header = msg["From"]
        #                 reply_to_header = msg["Reply-To"]
                        
        #                 email_list.append({"subject": subject, "body": email_body,"from":from_header})
        status, messages = mail.search(None, "UNSEEN")
        email_ids = messages[0].split()[-5:]  # Get last 5 emails

        emails = []  # Store email data

        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    sender = msg["From"]
                    subject = msg["Subject"]
                    
                    reply_to = None
                    
                    if msg['reply-to']:
                        reply_to = msg['Reply-to']
                    
                    # Extract email body
                    if msg.is_multipart():
                        body = ""
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                                break
                    else:
                        body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

                    emails.append({"sender": sender, "subject": subject, "body": body[:300],"reply_to":reply_to})

        mail.logout()
        return emails

    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []
print("executed")
# Example test
if __name__ == "__main__":
    emails = fetch_emails()
    for email in emails:
        print(f"📩 Subject: {email['subject']}")
        print(f"📝 Body: {email['body'][:100]}...")  
        print(f"👥 From: {email['sender']}")
        print("-" * 40)
