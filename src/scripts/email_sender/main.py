import smtplib
from email.message import EmailMessage

my_email = input("Sender email: ")
receiver_email = input("Receiver email: ")
my_pass = input("Sender password: ")

# Create the email
email = EmailMessage()
email["from"] = "Alessandro Ulisse Brancolini"
email["to"] = receiver_email
email["subject"] = "Python Email Sender Script"
email.set_content("I'm learning Python!")

# Configure SMTP server and send email
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # initiate a session between an email client and a server
    smtp.starttls()  # encryption mechanism
    smtp.login(my_email, my_pass)
    smtp.send_message(email)
