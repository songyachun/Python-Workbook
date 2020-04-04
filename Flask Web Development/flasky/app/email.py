from . import mail
from flask_mail import Message
from threading import Thread
from flask import current_app, render_template


def send_async_email(app, msg):
    # 异步发送邮件
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+' '+subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=['songyachun@139.com','106553784@qq.com'])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
