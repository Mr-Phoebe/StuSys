# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.contrib import messages
from UserMgr.form import LoginUserForm, ChangePasswordForm, AddUserForm, ClassForm
from UserMgr.models import Class, Person
from django.contrib.auth import get_user_model


# Create your views here.

# user操作

def LoginUser(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == 'GET' and request.GET.has_key('next'):
        next = request.GET['next']
    else:
        next = '/'

    if next.find('logout') > -1:
        next = '/'

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            messages.success(request,u"登陆成功")
            return HttpResponseRedirect(request.POST['next'])
    else:
        form = LoginUserForm(request)

    kwvars = {
        'request':request,
        'form':form,
        'next':next,
    }

    return render_to_response('login.html',kwvars,RequestContext(request))


@login_required
def LogoutUser(request):
    auth.logout(request)
    kwvars = {
        'request':request,
    }
    return render_to_response('logged_out.html',kwvars, RequestContext(request))


@login_required
def UserInfoShow(request):
    return render_to_response('user.info.html', {}, RequestContext(request))


@login_required
def ChangePassword(request):
    if request.method=='POST':
        form = ChangePasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logouturl'))
    else:
        form = ChangePasswordForm(user=request.user)

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('password.change.html',kwvars,RequestContext(request))


@login_required
def ListUser(request):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    UserList = get_user_model().objects.all()
    kwvars = {
        'request': request,
        'UserList':UserList,
    }
    return render_to_response('user.list.html', kwvars, RequestContext(request))


@login_required
def AddUser(request):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,u"添加用户成功")
            return HttpResponseRedirect(reverse('uclist'))
    else:
        form = AddUserForm()

    kwvars = {
        'form': form,
        'title':u"添加用户",
    }

    return render_to_response('common/common.form.html', kwvars, RequestContext(request))


@login_required
def EditUser(request, ID):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")

    try:
        users = Person.objects.get(id=ID)
    except Person.DoesNotExist:
        messages.error(request, u'<b>编辑人员失败</b><br /><b>详细信息：</b>找不到ID为%s的人员！'%ID)
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = AddUserForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            messages.success(request,u"修改人员成功")
            return HttpResponseRedirect(reverse('uclist'))
    else:
        form = AddUserForm(instance=users)

    kwvars = {
        'form': form,
        'title':u"修改人员",
    }

    return render_to_response('common/common.form.html', kwvars, RequestContext(request))


@login_required
def DelUser(request, ID):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")

    try:
        Person.objects.get(id=ID).delete()
        messages.success(request, u"删除人员成功")
        return HttpResponseRedirect(reverse('uclist'))
    except Person.DoesNotExist:
        messages.error(request, u'<b>删除人员失败</b><br /><b>详细信息：</b>找不到ID为%s的人员！'%ID)
        return HttpResponseRedirect(reverse('uclist'))

# class操作


@login_required
def ClassMgrList(request):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    ClassList = Class.objects.all()
    kwvars = {
        'request': request,
        'ClassList':ClassList,
    }
    return render_to_response('class.mgr.list.html', kwvars, RequestContext(request))

def AddClass(request):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,u"添加班级成功")
            return HttpResponseRedirect(reverse('listclass'))
    else:
        form = ClassForm()

    kwvars = {
        'form': form,
        'title':u"添加班级",
    }

    return render_to_response('common/common.form.html', kwvars, RequestContext(request))


@login_required
def EditClass(request, ID):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")

    try:
        classes = Class.objects.get(id=ID)
    except Class.DoesNotExist:
        messages.error(request, u'<b>编辑课程失败</b><br /><b>详细信息：</b>找不到ID为%s的课程！'%ID)
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = ClassForm(request.POST, instance=classes)
        if form.is_valid():
            form.save()
            messages.success(request,u"修改课程成功")
            return HttpResponseRedirect(reverse('listclass'))
    else:
        form = ClassForm(instance=classes)

    kwvars = {
        'form': form,
        'title':u"修改课程",
    }

    return render_to_response('common/common.form.html', kwvars, RequestContext(request))

@login_required
def DelClass(request, ID):
    if not request.user.role == 2:
        messages.error(request,u"权限不足！")
        return HttpResponseRedirect("/")

    try:
        Class.objects.get(id=ID).delete()
        messages.success(request, u"删除课程成功")
        return HttpResponseRedirect(reverse('listclass'))
    except Class.DoesNotExist:
        messages.error(request, u'<b>删除课程失败</b><br /><b>详细信息：</b>找不到ID为%s的课程！'%ID)
        return HttpResponseRedirect(reverse('listclass'))

@login_required
def RandomAddStudent(request):
    return


