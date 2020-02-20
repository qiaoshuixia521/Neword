from django import forms
from django.core.exceptions import NON_FIELD_ERRORS,ValidationError

from user.models import UserProfile


class RegForm(forms.Form):
    name = forms.CharField(required=True,min_length=3,error_messages={"required":"用户名不能为空",
    "min_length":"用户名太短"})
    password = forms.CharField(required=True,min_length=6,error_messages={"length_min":"密码长队太短"})
    repeat_password = forms.CharField(required=True,min_length=6)

#
# class UserProfileForm(forms.ModelForm):#登录认证使用form.ModelForm有些问题，会报错说是用户已存在
#
#     class Meta:
#         model = UserProfile
#         fields = ["password"]


class UserProfileForm(forms.Form):#wuhan 123456
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,max_length=10,min_length=6)

    def clean_password(self):
        pass

    def clean_username(self):
        pass

    def clean(self):
        pass