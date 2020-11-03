# coding=utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from Log import log


class SendMail:
    def __init__(self, email_server, sender_login_user, sender_login_password, sender, receiver, email_subject, path):
        self.email_server = email_server
        self.sender_login_user = sender_login_user
        self.sender_login_password = sender_login_password
        self.sender = sender
        self.receiver = receiver
        self.email_subject = email_subject
        self.path = path
        self.log = log.MyLog()

    def send_mail(self):
        try:
            list = os.listdir(self.path)
            list.sort(key=lambda filename: os.path.getmtime(os.path.join(self.path, filename)))
            send_file = os.path.join(self.path, list[-1])
        except Exception as e:
            self.log.error('failed to get the latest test report: %s' % e)
            raise

        try:
            with open(send_file, 'rb') as file_html:
                content = file_html.read()
            mail = MIMEMultipart()
            mail['Subject'] = Header(self.email_subject, 'utf-8')
            mail_text = MIMEText(content, 'html', 'utf-8')
            mail.attach(mail_text)
            mail_file = MIMEText(content, 'html', 'utf-8')
            mail_file['Content-Type'] = 'application/octet-stream'
            mail_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
            mail.attach(mail_file)
            mail['From'] = self.sender
            mail['To'] = ','.join(self.receiver)
            smtp = smtplib.SMTP()
            smtp.connect(self.email_server)
            smtp.login(self.sender_login_user, self.sender_login_password)
            smtp.sendmail(mail['From'], mail['To'], mail.as_string())
            smtp.quit()
            self.log.info('Mail sent successfully~')
        except Exception as e:
            self.log.error('failed to send mail: %s' % e)
            raise
