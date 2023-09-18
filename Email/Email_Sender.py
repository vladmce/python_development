"""
This software sends emails. Make sure you complete your gmail address on line 10 and your app password from gmail on line 11.
"""

from email.message import EmailMessage
import ssl
import smtplib

# My email account data
email_sender = ""
email_password = ""  # From Gmail settings -> two-factor auth -> app passwords

# Email structure inputs
email_receiver = input("Email receiver: ")


subject = input("Add the subject of the email: ")
body = input("Add the content of the email:\n")

print(f"You want to send {subject} to {email_receiver} containing the following message:\n{body}")
while True:
    decision = input("\nSend it? (y/n): ")
    if decision == "y" or decision == "n":
        break

if decision == "y":
    # Create the instance of the email
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["subject"] = subject
    em.set_content(body)

    # Disable SSL certificate verification
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
else:
    pass
