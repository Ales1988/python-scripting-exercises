"""
Basic script to send email with python.
In this example, credentials are entered manually via input, as password handling, authentication, and
data security are outside the scope of this exercise.
"""

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


def composing_mail(receiver_email: str, name: str) -> EmailMessage:
    # Composing the email
    email = EmailMessage()
    email["from"] = "Alessandro Ulisse Brancolini"
    email["to"] = receiver_email
    email["subject"] = "Python Email Sender Script"

    # Make html a Template instance to later use substitute method
    html = Template(Path("resources/email_sender/index.html").read_text())
    # Use index.html as a template replacing variable $name with ale
    email.set_content(html.substitute(name=name), "html")

    return email


def send_email(my_email: str, my_pass: str, email: EmailMessage):
    # Configure SMTP server and send email
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()  # initiate a session between an email client and a server
        smtp.starttls()  # encryption mechanism
        smtp.login(my_email, my_pass)
        smtp.send_message(email)


my_email = input("Sender email: ")
receiver_email = input("Receiver email: ")
my_pass = input("Sender password: ")
receiver_name = "Ale"

email = composing_mail(receiver_email, receiver_name)

try:
    send_email(my_email, my_pass, email)
    print("Email sent.")
except smtplib.SMTPAuthenticationError:
    print("Incorrect sender email or password.")
except Exception as e:
    print(f"Error: {e}")
