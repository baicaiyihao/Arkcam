from django.core.mail import send_mail
from calery_tasks.main import app
from libs import email_config

#bind=True
#第一个参数始终是任务实例self
# default_retry_delay时默认重置的时间,max_retries最大重置次数
@app.task(bind=True,default_retry_delay=5)
def send_Email(self,email):
    subject = '主题'
    message = '内容'
    # 填写发件人
    from_email = email_config.EMAIL_FROM
    # 收件人，默认为当前用户绑定的邮箱
    recipient_list = [email]
    # 进行邮件发送操作
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list
        )
    except:
        raise self.retry(exc=Exception('重新发送'),max_retries=5)
