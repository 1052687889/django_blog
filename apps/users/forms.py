#! /usr/bin/env python
# -*- coding:utf-8-*-
__author__ = "taoke"
__datetime__ = "19-1-13 21:52:31"
from django import forms
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    email = forms.EmailField(label='邮箱',required=True, error_messages={
		'required': '邮箱不能为空'
	})
    username = forms.CharField(label='注册用户名',max_length=20, min_length=3, required=True, error_messages={
		'max_length': '用户名的最大长度是20位',
		'min_length': '用户名的最小长度是3位',
		'required': '用户名不能为空'
	})
    password = forms.CharField(label='密码',max_length=20, min_length=3, required=True, error_messages={
		'max_length': '密码的最大长度是20位',
		'min_length': '密码的最小长度是6位',
		'required': '密码不能为空'
	})
    surepassword = forms.CharField(label='确认密码',max_length=20, min_length=3, required=True, error_messages={
		'max_length': '密码的最大长度是20位',
		'min_length': '密码的最小长度是6位',
		'required': '密码不能为空'
	})
    captcha = CaptchaField(label='验证码',error_messages={"invalid":"验证码错误"})

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3, required=True, error_messages={
		'max_length': '用户名的最大长度是20位',
		'min_length': '用户名的最小长度是3位',
		'required': '用户名不能为空'
	})
    password = forms.CharField(max_length=20, min_length=6, required=True, error_messages={
		'max_length': '密码的最大长度是20位',
		'min_length': '密码的最小长度是6位',
		'required': '密码不能为空'
	})
