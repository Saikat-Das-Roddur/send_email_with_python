import email
import smtplib
from string import Template
from pathlib import Path
from email.message import EmailMessage
from unicodedata import name

html  = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Sender name'
email['to'] = 'sender_mail'
email['subject'] = 'You won 1,000,000 dollars!'
email.set_content(html.substitute(name='anything'),'html')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email','your_password')
    smtp.send_message(email)
    print('all good boss')
     