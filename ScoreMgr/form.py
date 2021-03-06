#-*- coding: utf-8 -*-

from django import forms
from UserMgr.models import *


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["begindate","enddate","term","name"]
        widgets = {
            "begindate":forms.TextInput(attrs={'class':'form-control'}),
            "enddate":forms.TextInput(attrs={'class':'form-control'}),
            "term":forms.TextInput(attrs={'class':'form-control'}),
            "name":forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(CourseForm,self).__init__(*args,**kwargs)
        self.fields['name'].label = u'课程名称'
        self.fields['name'].error_messages = {'required': u'请输入课程名称'}
        self.fields['term'].label = u'学期'
        self.fields['term'].error_messages = {'required': u'请输入学期'}
        self.fields['begindate'].label = u'开始时间'
        self.fields['begindate'].error_messages = {'required': u'请输入开始时间',
                                                   'invalid':u"请输入有效的日期（年-月-日）"}
        self.fields['enddate'].label = u'结束时间'
        self.fields['enddate'].error_messages = {'required': u'请输入结束时间',
                                                 'invalid':u"请输入有效的日期（年-月-日）"}

    def clean_enddate(self):
        if self.cleaned_data.get('enddate') < self.cleaned_data.get('begindate'):
            raise forms.ValidationError(u"开始日期必须小于结束日期")
        return self.cleaned_data.get('enddate')


class TeacherCourseForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["course"]
        widgets = {
            "course": forms.SelectMultiple(attrs={'class': 'form-control', 'size': '10'})
        }

    def __init__(self, *args, **kwargs):
        super(TeacherCourseForm, self).__init__(*args, **kwargs)
        self.fields['course'].label = u'选择任教课程'
        self.fields['course'].error_messages = {'invalid': u'请正确选择任教课程'}


class AddScoreForm(forms.Form):
    studentid = forms.CharField(label=u'学号', error_messages={'required': u'学号不能为空'},
                                widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "请输入学号"}))
    score = forms.IntegerField(label=u'分数', error_messages={'required': u'分数不能为空'},
                               widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "请输入分数"}))
