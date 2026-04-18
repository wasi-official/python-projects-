# Email Automation — Simulate sending emails with retry logic
import random

emails = []

def load_emails(emails):
    with open("email.txt", "r") as file:
        for line in file:
            email, subject, body = line.strip().split(":")
            emails.append((email, subject, body))

def send_emails(emails):
    open("email_status.txt", "w").close()
    with open("email_status.txt", "a") as file:
        for email in emails:
            rand = random.random()
            if rand < 0.8:
                print("Email sent")
                file.write(f"success:{email}\n")
            else:
                print("Send failed")
                file.write(f"failed:{email}\n")

def retry_failed_emails():
    failed = []
    with open("email_status.txt", "r") as file:
        for line in file:
            status, data = line.strip().split(":", 1)
            if status == "failed":
                failed.append(data)

    with open("email_status.txt", "a") as file:
        for email in failed:
            rand = random.random()
            if rand < 0.8:
                print("Retry sent")
                file.write(f"success:{email}\n")
            else:
                print("Retry failed")
                file.write(f"failed:{email}\n")

load_emails(emails)
send_emails(emails)
retry_failed_emails()