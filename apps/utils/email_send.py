#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:taoke
import urllib
from apps.users.models import EmailVerifyRecord
from django.core.mail import send_mail
from django.conf import settings
from random import Random
from django.template import loader

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def send_register_email(email,username,send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.username = username
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "饕客博客注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/users/active/?username={0}&code={1}".format(urllib.parse.quote(username),code)

        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "饕客博客注册密码重置链接"
        email_body = "请点击下面的链接重置密码: http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "饕客博客邮箱修改验证码"
        email_body = "你的邮箱验证码为: {0}".format(code)

        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
        if send_status:
            pass



