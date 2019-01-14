#! /usr/bin/env python
# -*- coding:utf-8-*-
__author__ = "taoke"
__datetime__ = "19-1-13 21:52:31"
from django import forms


class RegisterForm(forms.Form):
    username = forms.TextInput()
    password = forms.IntegerField()
    surepassword = forms.IntegerField()