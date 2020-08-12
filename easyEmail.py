import smtplib, time
from email.message import EmailMessage

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login("jfuhrimantest@gmail.com", 'pythontest1')

msg = EmailMessage()
msg['Subject'] = "Test"
msg['From'] = 'jfuhrimantest@gmail.com'
msg['To'] = 'jnfuhriman@gmail.com'
msg.set_content("This is a test script to send an email")
s.send_message(msg)
s.quit()