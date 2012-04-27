    #! /usr/bin/python
     
    import os
    import fnmatch
    import smtplib
    import string
     
    from email import Encoders
    from email.MIMEBase import MIMEBase
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEImage import MIMEImage
    from email.Utils import formatdate
     
    COMMASPACE = ', '
     
    msg = MIMEMultipart()
    msg['Subject'] = 'Weekly Graphs'
    msg['From'] = 'bmorrison@tld.com'
    msg['To'] = 'bmorrison@tld.com'
    msg.preamble = 'Weekly Graphs blah'
     
    PATH = '/home/bmorrison/graphs'
     
    for path, dirs, files in os.walk(PATH):
        for file in files:
            fullpath = os.path.join(path,file)
            png = open(fullpath, 'r')
            img = MIMEImage(png.read())
            png.close()
            msg.attach(img)
     
    s = smtplib.SMTP('smtp.tld.com')
    s.sendmail('bmorrison@tld.com', 'bmorrison@tld.com', msg.as_string())
    s.quit()

