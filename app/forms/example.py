#!/usr/bin/env python
# -*- coding: utf-8 -*-
# example

"""
from backend.form.forms import BaseForm
from backend.form.fields import StringField
from backend.form.fields import EmailField
class CustomForm(BaseForm):
    def __init__(self):
        self.content = StringField()
        self.news_id = EmailField(custom_error_dict={'required': '注册邮箱不能为空.', 'valid': '注册邮箱格式错误.'})
        self.reply_id = StringField(required=False)

        super(CustomForm, self).__init__()
"""