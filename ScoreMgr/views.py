# coding=utf-8

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from ScoreMgr.form import CourseForm, TeacherCourseForm, AddScoreForm
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
        'CourseList': CourseList,
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
        'title': u"添加课程",
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
        'title': u"修改课程",
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
        'TeacherList': TeacherList,
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
        'ScoreList': ScoreList,
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
        'ScoreList': ScoreList,
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
        'ScoreList': ScoreList,
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
        'CourseList': CourseList,
    }
    return render_to_response('teacher.score.add.html', kwvars, RequestContext(request))


@login_required
def AddScore(request, ID):
    if not request.user.role == 1:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    try:
        course = Course.objects.get(id=ID)
    except Course.DoesNotExist:
        messages.error(request, u'<b>编辑课程成绩失败</b><br /><b>详细信息：</b>找不到ID为%s的课程！' % ID)
        return HttpResponseRedirect("/")
    '''
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, u"修改课程成功")
            return HttpResponseRedirect(reverse('listcourse'))
    else:
        form = CourseForm(instance=course)

    kwvars = {
        'form': form,
        'title': u"修改课程",
    }

    return render_to_response('common/common.form.html', kwvars, RequestContext(request))
    '''
    return HttpResponseRedirect("/")


# 管理员修改某教师课程
@login_required
def CourseMgr(request, ID):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")

    try:
        teacher = Person.objects.get(id=ID)
    except Course.DoesNotExist:
        messages.error(request, u'<b>编辑任教课程失败！</b><br /><b>详细信息：</b>找不到ID为%s的教师！'%ID)
        return HttpResponseRedirect(reverse('listteacher'))
    if not teacher.role == 1:
        messages.error(request, u'<b>编辑任教课程失败！</b><br /><b>详细信息：</b>ID为%s的用户并不是老师！' % ID)
        return HttpResponseRedirect(reverse('listteacher'))
    if request.method == "POST":
        form = TeacherCourseForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request,u"编辑任教课程成功")
            return HttpResponseRedirect(reverse('listteacher'))
    else:
        form = TeacherCourseForm(instance=teacher)

    kwvars = {
        'form': form,
        'title': u"编辑任教课程",
        'extjs':"""
            var catbox = $('select[name="course"]').bootstrapDualListbox({
                  nonSelectedListLabel: '可选择课程',
                  selectedListLabel: '已选择课程',
                  preserveSelectionOnMove: 'moved',
                  moveOnSelect: false,
            });
        """ # 额外扩展的js插件，用于实现友好的SelectMutiple
    }

    return render_to_response('common/common.form.html', kwvars, RequestContext(request))

# 教师所任课程列表
@login_required
def ListCourseTaught(request):
    if not request.user.role == 1:
        messages.error(request, u"权限不足！")
        return HttpResponseRedirect("/")
    teacher = get_user_model().objects.get(username=request.user.username)
    CourseList = teacher.course.all()
    kwvars = {
        'request': request,
        'CourseList': CourseList,
        'editscore':False,
    }
    return render_to_response('course.teacher.list.html', kwvars, RequestContext(request))

# 成绩录入->教师所任课程列表
@login_required
def ListCourseForInput(request):
    if not request.user.role == 1:
        messages.error(request, u"权限不足！")
        return HttpResponseRedirect("/")
    teacher = get_user_model().objects.get(username=request.user.username)
    CourseList = teacher.course.all()
    kwvars = {
        'request': request,
        'CourseList': CourseList,
        'editscore':True,
    }
    return render_to_response('course.teacher.list.html', kwvars, RequestContext(request))

@login_required
def AddScore(request, ID):
    if not request.user.role == 1:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")

    try:
        course = Course.objects.get(id=ID)
    except Course.DoesNotExist:
        messages.error(request, u'<b>录入成绩失败！</b><br /><b>详细信息：</b>找不到ID为%s的课程！'%ID)
        return HttpResponseRedirect(reverse('listCourseFprInput'))
    if request.method == "POST":
        form = AddScoreForm(request.POST)
        if form.is_valid():
            try:
                student = Person.objects.get(username=form.cleaned_data['studentid'])
            except Person.DoesNotExist:
                messages.warning(request, u'<b>未能录入该数据</b><br /><b>详细信息：</b>学生%s不存在！' % form.cleaned_data['studentid'])
                return HttpResponseRedirect(reverse("addscore",args=(ID,)))
            try:
                sinstance = Score.objects.get(course_id=ID, student__username=form.cleaned_data['studentid'])
                sinstance.score = form.cleaned_data['score']
                sinstance.save()
                messages.success(request, u"录入（覆盖已有记录） 科目:%s    学号:%s  姓名:%s    成绩:%s"%(
                    course.name,student.username,student.realname,form.cleaned_data['score']
                ))
            except Score.DoesNotExist:
                Score.objects.create(student=student,course=course,score=form.cleaned_data['score'])
                messages.success(request, u"录入 科目:%s    学号:%s  姓名:%s    成绩:%s" % (
                    course.name, student.username, student.realname, form.cleaned_data['score']
                ))
            except Score.MultipleObjectsReturned:
                Score.objects.filter(course_id=ID, student_id=form.cleaned_data['studentid']).all().delete()
                Score.objects.create(student=student, course=course, score=form.cleaned_data['score'])
                messages.success(request, u"录入（覆盖已有记录） 科目:%s    学号:%s  姓名:%s    成绩:%s" % (
                    course.name, student.username, student.realname, form.cleaned_data['score']
                ))
            return HttpResponseRedirect(reverse("addscore", args=(ID,)))
    else:
        form = AddScoreForm()

    kwvars = {
        'form': form,
        'title': u"手工录入成绩",
        'coursename':course.name,
    }

    return render_to_response('score.input.form.html', kwvars, RequestContext(request))

@login_required
def ViewScore(request, ID):
    if not request.user.role == 1:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")

    try:
        course = Course.objects.get(id=ID)
    except Course.DoesNotExist:
        messages.error(request, u'<b>录入成绩失败！</b><br /><b>详细信息：</b>找不到ID为%s的课程！'%ID)
        return HttpResponseRedirect(reverse('listCourseFprInput'))

    kwvars = {
        'ScoreList': course.score_set.all(),
        'title': u"查看成绩",
        'coursename':course.name,
    }

    return render_to_response('score.view.html', kwvars, RequestContext(request))

@login_required
def DelScore(request, ID):
    if not request.user.role == 1:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    try:
        score = Score.objects.get(id=ID)
        if(get_user_model().course.filter(id=score.id).count()==0):
            messages.error(request, u"权限不足！")
            return HttpResponseRedirect("/")
        score.delete()
        messages.success(request, u"删除成绩记录成功")
        return HttpResponseRedirect(reverse("viewscore", args=(score.course.id,)))
    except Course.DoesNotExist:
        messages.error(request, u'<b>删除成绩记录失败</b><br /><b>详细信息：</b>找不到ID为%s的成绩记录！'%ID)
        return HttpResponseRedirect("/")