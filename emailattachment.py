# https://www.google.com/settings/security/lesssecureapps
#allow above 

#####################################################################
# D.Ellis 16 
#####################################################################


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email.mime.text import MIMEText
from email import Encoders
import os,sys,getpass
from email.mime.application import MIMEApplication
from os.path import basename


def send(to , subject , text , gmail_user="dp626@york.ac.uk" , attach = sys.argv[1:]):
        #your username is gmail_user

        msg = MIMEMultipart()

        msg['From'] = gmail_user
        msg['To'] = to 
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        for f in sys.argv[1:]:
            with open(f, "rb") as fil:
                    msg.attach(MIMEApplication(
                        fil.read(),
                        Content_Disposition='attachment; filename="%s"' % basename(f),
                        Name=basename(f)
                        ))

        mailServer = smtplib.SMTP("smtp.gmail.com", 587)

        ######################
        #http://www.arclab.com/en/amlc/list-of-smtp-and-pop3-servers-mailserver-list.html
        ######################
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, str(getpass.getpass('enter secret code\n')).replace(' ',''))
        mailServer.sendmail(gmail_user, to, msg.as_string())

        mailServer.close()


        print  'email from %s sent to %s. Attached files: %s' %(gmail_user, to, attach)
        
        return None
