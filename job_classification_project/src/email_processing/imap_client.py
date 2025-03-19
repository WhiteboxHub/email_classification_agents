import imaplib
import email
from email.header import decode_header

# Gmail IMAP settings
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993
EMAIL_ACCOUNT = "junaidfaizan024@gmail.com"
EMAIL_PASSWORD = "kaymeqsbvbpjtwjw"  # Use App Password, not Gmail password

def fetch_emails():
    """Fetch emails using IMAP."""
    try:
        # Connect to Gmail IMAP server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

        # Select the mailbox (INBOX by default)
        mail.select("inbox")

        # Search for all emails
        status, messages = mail.search(None, "ALL")  # You can use 'UNSEEN' for unread emails

        # Convert the result into a list of email IDs
        email_ids = messages[0].split()

        print(f"Total Emails: {len(email_ids)}")

        # Fetch the latest 5 emails
        for email_id in email_ids[-5:]:
            status, msg_data = mail.fetch(email_id, "(RFC822)")

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    # Decode email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8")

                    # Decode sender info
                    sender, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(sender, bytes):
                        sender = sender.decode(encoding or "utf-8")

                    print(f"\nFrom: {sender}")
                    print(f"Subject: {subject}")

                    # Extract email body
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            # Extract the email body (only plain text, ignoring attachments)
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                body = part.get_payload(decode=True).decode()
                                print(f"Body:\n{body[:800]}...")  # Print first 300 chars
                    else:
                        body = msg.get_payload(decode=True).decode()
                        print(f"Body:\n{body[:300]}...")

        mail.logout()
    
    except Exception as e:
        print(f"Error: {e}")

fetch_emails()


