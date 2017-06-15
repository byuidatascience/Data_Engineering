#!/usr/bin/env python3

#import smtplib for the actual sending function
import smtplib
#from flask import Flask
#import twit_ht
from awsome_tweet import connect_twitter,prepare_page,upload_page
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#app = Flask(__name__)
#@app.route('/')


def who_what_where(html_code):
# me == the sender's email address
# you == the recipient's ema
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'This is the generic subject.'
    msg['From'] = '2check91@gmail.com'
    msg['To'] = 'ptluczek@mail.usciences.edu'
    part1 = MIMEText('www.google.com', 'plain')
    part2 = MIMEText(html_code, 'html')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    print ("Hi, I'm Paul.")
    return msg

# Send the message via our own SMTP server, try localhost.
def send(host,msg):
    s = smtplib.SMTP(host)
    s.send_message(msg)
    s.quit()


print ("Hi, I'm JC.")
t = connect_twitter(config_filepath='/home/ubuntu/.ssh/api_cred.yml')
page, timestamp = prepare_page(t)
html_code = upload_page(page, timestamp) 
msg = who_what_where(html_code)
send('localhost',msg) # Must define hose still. 
