#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.db import models
import datetime

SEX_CHOICES = [
    (u'0', u'男'),
    (u'1', u'女'),
]

ROLE_CHOICES = [
    (0, u'学生'),
    (1, u'老师'),
    (2, u'管理员'),
]

class UserManager(BaseUserManager):
    def create_user(self,username,password=None):
        user=self.model(
            username=username,
        )

        user.role=0
        user.set_password(password)
        user.last_login = datetime.datetime.now()
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password):
        user=self.model(
            username=username,
        )

        user.role=2
        user.set_password(password)
        user.last_login=datetime.datetime.now()
        user.save(using=self._db)
        return user


# Create your models here.

class Class(models.Model):
    classid   = models.CharField(u'班号', unique=True, max_length=16)
    classname = models.CharField(u"班级名称", max_length=20)
    def __unicode__(self):
        return self.classid
    class Meta:
        db_table = u'ClassInfo'         # 创建数据库的时候名字叫做ClassInfo
        verbose_name_plural=u'班级'

class Course(models.Model):
    begindate = models.DateField(u'开始日期')
    enddate   = models.DateField(u'结束日期')
    term      = models.CharField(u'学期',max_length=16)
    name      = models.CharField(u'名字',max_length=16,unique=True)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'CourseInfo'
        verbose_name_plural = u'专业课程'

class Person(AbstractBaseUser):
    # user = models.OneToOneField(User)
    username = models.CharField(max_length=40, unique=True, db_index=True)
    # password = models.TextField()
    role     = models.IntegerField(choices=ROLE_CHOICES)
    realname = models.CharField(u'姓名', max_length=16)
    theclass = models.ForeignKey(Class, verbose_name=u'班级', null=True, blank=True)
    sex      = models.CharField(u'性别', choices=SEX_CHOICES, max_length=1)
    course   = models.ManyToManyField(Course, null=True, blank=True)

    USERNAME_FIELD = 'username' # 定义auth模块使用的用户名字段
    objects = UserManager()     # 定义用户管理器
    def __unicode__(self):
        return self.realname
    class Meta:
        db_table = u'Person'

class Score(models.Model):
    course    = models.ForeignKey(Course)
    student   = models.ForeignKey(Person)
    score     = models.IntegerField()