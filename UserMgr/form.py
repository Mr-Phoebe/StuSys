#-*- coding: utf-8 -*-

from django import forms
from django.contrib import auth
from django.contrib.auth import get_user_model
from UserMgr.models import *
import datetime

class LoginUserForm(forms.Form):
    username = forms.CharField(label=u'学号/工号',
        error_messages={'required':u'学号/工号不能为空'},
        widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"请输入学号/工号"}))
    password = forms.CharField(label=u'密码',
        error_messages={'required':u'密码不能为空'},
        widget=forms.PasswordInput(attrs={'class':'form-control',"placeholder":"请输入密码"}))

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None

        super(LoginUserForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = auth.authenticate(username=username,password=password)
            if self.user_cache is None:
                raise forms.ValidationError(u'学号/工号与密码不匹配')
        return self.cleaned_data

    def get_user(self):
        return self.user_cache

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label=u'原始密码',error_messages={'required':'请输入原始密码'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=u'新密码',error_messages={'required':'请输入新密码'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=u'重复输入',error_messages={'required':'请重复新输入密码'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(u'原密码错误')
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if len(password1)<6:
            raise forms.ValidationError(u'密码必须大于6位')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(u'两次密码输入不一致')
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user

class AddUserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["username","role","realname","password","theclass","sex"]
        widgets = {
            "username":forms.TextInput(attrs={'class': 'form-control'}),
            "role":forms.Select(attrs={'class': 'form-control'}),
            "realname":forms.TextInput(attrs={'class': 'form-control'}),
            "password":forms.PasswordInput(attrs={'class': 'form-control'}),
            "theclass":forms.Select(attrs={'class': 'form-control'}),
            "sex":forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].lable=u"用户名(一般为学号或工号)"
        self.fields['role'].lable = u"身份"
        self.fields['realname'].lable = u"真实姓名"
        self.fields['password'].lable = u"密码"
        self.fields['theclass'].lable = u"班级（身份为教师则留空）"
        self.fields['sex'].lable = u"性别"
        self.fields['username'].error_messages={'required':u"请输入用户名"}
        self.fields['role'].error_messages={'required':u"请选择身份"}
        self.fields['realname'].error_messages={'required':u"请输入真实姓名"}
        self.fields['password'].error_messages={'required':u"请输入密码"}
        #self.fields['theclass'].error_messages={'required':u"请输入正文"}
        self.fields['sex'].error_messages={'required':u"请选择性别"}

    def clean_theclass(self):
        if self.cleaned_data.get("role") == 0:
            if self.cleaned_data.get("theclass") == "":
                raise forms.ValidationError(u"对于学生，必须选择班级")
            else:
                return self.cleaned_data.get("theclass")
        else:
            return None

    def clean_username(self):
        if self.cleaned_data.get("role") != 2:
            username =self.cleaned_data.get('username')
            if len(username) != 10:
                raise forms.ValidationError(u"学号/工号必须为10位")
        return username

    def save(self, commit=True):
        userobj = super(AddUserForm,self).save(commit=False)
        userobj.set_password(userobj.password)
        userobj.last_login = datetime.datetime.now()
        userobj.save()


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ["classid","classname"]
        widgets = {
            "classid":forms.TextInput(attrs={'class':'form-control'}),
            "classname":forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(ClassForm,self).__init__(*args,**kwargs)
        self.fields['classid'].label = u'班级编号'
        self.fields['classid'].error_messages = {'required': u'请输入班级编号'}
        self.fields['classname'].label = u'班级名称'
        self.fields['classname'].error_messages = {'required': u'请输入班规名称'}

    def clean_classid(self):
        classid = self.cleaned_data.get('classid')
        if len(classid) != 10:
            raise forms.ValidationError(u'班级编号必须为10号')
        return classid
