import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


def composing_mail(receiver_email):
    # Composing the email
    email = EmailMessage()
    email["from"] = "Alessandro Ulisse Brancolini"
    email["to"] = receiver_email
    email["subject"] = "Python Email Sender Script"

    # Make html a Template instance to later use substitute method
    html = Template(Path("resources/email_sender/index.html").read_text())
    # Use index.html as a template replacing variable $name with ale
    email.set_content(html.substitute(name="ale"), "html")

    return email


def send_email(my_email, my_pass, email):
    # Configure SMTP server and send email
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()  # initiate a session between an email client and a server
        smtp.starttls()  # encryption mechanism
        smtp.login(my_email, my_pass)
        smtp.send_message(email)


my_email = input("Sender email: ")
receiver_email = input("Receiver email: ")
my_pass = input("Sender password: ")

email = composing_mail(receiver_email)

send_email(my_email, my_pass, email)
