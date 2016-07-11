# coding=utf-8

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from ScoreMgr.form import CourseForm
from UserMgr.form import Course, Score, Person


# course操作
@login_required
def CourseMgrList(request):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    CourseList = Course.objects.all()
    kwvars = {
        'request': request,
        'CourseList':CourseList,
    }
    return render_to_response('course.mgr.list.html', kwvars, RequestContext(request))


@login_required
def AddCourse(request):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,u"添加课程成功")
            return HttpResponseRedirect(reverse('listcourse'))
    else:
        form = CourseForm()

    kwvars = {
        'form': form,
        'title':u"添加课程",
    }

    return render_to_response('common/common.form.html', kwvars, RequestContext(request))

@login_required
def EditCourse(request, ID):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")

    try:
        course = Course.objects.get(id=ID)
    except Course.DoesNotExist:
        messages.error(request, u'<b>编辑课程失败</b><br /><b>详细信息：</b>找不到ID为%s的课程！'%ID)
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request,u"修改课程成功")
            return HttpResponseRedirect(reverse('listcourse'))
    else:
        form = CourseForm(instance=course)

    kwvars = {
        'form': form,
        'title':u"修改课程",
    }

    return render_to_response('common/common.form.html', kwvars, RequestContext(request))

@login_required
def DelCourse(request, ID):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")

    try:
        Course.objects.get(id=ID).delete()
        messages.success(request, u"删除课程成功")
        return HttpResponseRedirect(reverse('listcourse'))
    except Course.DoesNotExist:
        messages.error(request, u'<b>删除课程失败</b><br /><b>详细信息：</b>找不到ID为%s的课程！'%ID)
        return HttpResponseRedirect(reverse('listcourse'))

# 任教课程管理


@login_required
def ListTeacher(request):   # 任课教师列表
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    TeacherList = get_user_model().objects.filter(role=1)
    kwvars = {
        'request': request,
        'TeacherList':TeacherList,
    }
    return render_to_response('teacher.list.html', kwvars, RequestContext(request))


'''
@login_required
def ListTeachCourse(request, ID):   # 增删 ID教师 的任教课程
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    CourseList = Course.objects.all()
    kwvars = {
        'request': request,
        'CourseList':CourseList,
    }
    return render_to_response('course.mgr.list.html', kwvars, RequestContext(request))
'''

# score操作


@login_required
def ListCourseScore(request):   # 学生查看自己课程成绩
    if not request.user.role == 0:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    ScoreList = Score.objects.filter(student=request.user)
    kwvars = {
        'request': request,
        'ScoreList':ScoreList,
    }
    return render_to_response('self.score.list.html', kwvars, RequestContext(request))


# 老师查看成绩


@login_required
def ListScoreOperation(request):
    if not request.user.role == 1:
        messages.error(request, u"权限不足！")
        return HttpResponseRedirect("/")
    teacher = get_user_model().objects.get(username=request.user.username)
    CourseList = teacher.course.all()
    kwvars = {
        'request': request,
        'CourseList': CourseList,
    }
    return render_to_response('teacher.score.list.html', kwvars, RequestContext(request))

# 老师查看自己对应课程的学生成绩
'''

@login_required
def ListStuScore(request,ID):
    if not request.user.role == 1:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
        ScoreList = Score.objects.filter(course=)
    kwvars = {
        'request': request,
        'ScoreList':ScoreList,
    }
    return render_to_response('cou.score.list.html', kwvars, RequestContext(request))
'''

# 老师查看自己对应课程的报表
'''

@login_required
def ListScoreChart(request,ID):
    if not request.user.role == 1:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
        ScoreList = Score.objects.filter(course=)
    kwvars = {
        'request': request,
        'ScoreList':ScoreList,
    }
    return render_to_response('cou.score.list.html', kwvars, RequestContext(request))
'''


# 老师查看自己教授的课程


@login_required
def EditScore(request):
    if not request.user.role == 1:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    teacher = get_user_model().objects.get(username=request.user.username)
    CourseList = teacher.course.all()
    kwvars = {
        'request': request,
        'CourseList':CourseList,
    }
    return render_to_response('teacher.course.list.html', kwvars, RequestContext(request))