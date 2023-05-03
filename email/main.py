import smtplib
from_email = ''
to_email  = ''
subj='TEST EMAIL'
message_text='Hello, World!'
username = str('')  
password = str('')  
  
server = smtplib.SMTP('',587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(from_email, to_email, message_text)
server.quit()