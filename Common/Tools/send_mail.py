# coding=utf-8
import os
import smtplib
from Log import log
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendMail:
    """邮件发送测试报告"""

    def __init__(self, *args):
        """
        :param args: 初始化邮件发送测试报告所需的各种参数
        """

        self.email_server = args[0]  # 邮件服务地址
        self.sender_login_user = args[1]  # 发送人邮件登录用户名
        self.sender_login_password = args[2]  # 授权码
        self.sender = args[3]  # 发件人
        self.receiver = args[4]  # 收件人列表
        self.email_subject = args[5]  # 邮件主题
        self.path = args[6]  # 测试报告所在目录
        self.log = log.MyLog

    def send_mail(self):

        # 获取最新的测试报告
        try:
            list = os.listdir(self.path)
            list.sort(key=lambda filename: os.path.getmtime(os.path.join(self.path, filename)))
            send_file = os.path.join(self.path, list[-1])
        except Exception as e:
            self.log.error('failed to get the latest test report: %s' % e)
            raise

        # 发送邮件
        try:
            # 读取测试报告内容
            with open(send_file, 'rb') as file_html:
                content = file_html.read()

            # 实例化带附件的MIMEMultipart对象
            mail = MIMEMultipart()
            #  定义邮件主题
            mail['Subject'] = Header(self.email_subject, 'utf-8')
            #  定义邮件发送人
            mail['From'] = self.sender
            #  定义邮件接收人
            mail['To'] = ','.join(self.receiver.split(' '))

            # 构造邮件的正文
            mail_text = MIMEText(content, 'html', 'utf-8')
            # 将邮件的正文添加到MIMEMultipart对象中
            mail.attach(mail_text)

            # 构造邮件的附件
            mail_file = MIMEText(content, 'html', 'utf-8')
            mail_file['Content-Type'] = 'application/octet-stream'
            mail_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
            # 将邮件的附件添加到MIMEMultipart对象中
            mail.attach(mail_file)

            # 实例化SMTP对象 连接SMTP主机
            smtp = smtplib.SMTP_SSL(self.email_server, 465)
            # smtp = smtplib.SMTP()
            # smtp.connect(self.email_server)
            # 输出发送邮件详细过程
            # smtp.set_debuglevel(1)
            # 邮件登录
            smtp.login(self.sender_login_user, self.sender_login_password)
            # 邮件发送
            smtp.sendmail(mail['From'], self.receiver.split(' '), mail.as_string())
            # 断开SMTP连接
            smtp.quit()
            self.log.info('Mail sent test report successfully~')
        except Exception as e:
            self.log.error('failed to send mail: %s' % e)
            raise
