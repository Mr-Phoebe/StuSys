from django.conf.urls import patterns, include, url

import UserMgr.views

urlpatterns = patterns('UserMgr.views',
    url(r'^login/$', 'LoginUser', name='loginurl'),
    url(r'^logout/$', 'LogoutUser', name='logouturl'),
    url(r'^ucinfo/$', 'UserInfoShow', name='ucinfo'),
    url(r'^admin/list/$', 'ListUser', name='uclist'),
    url(r'^admin/add/$', 'AddUser', name='ucadd'),
    url(r'^changepassword/$', 'ChangePassword', name='changepassword'),
    url(r'^admin/edit/(?P<ID>\d+)/$', 'EditUser', name='ucedit'),
    url(r'^admin/del/(?P<ID>\d+)/$', 'DelUser', name='ucdel'),
    url(r'^admin/class/add/$', 'AddClass', name='addclass'),
    url(r'^admin/class/list/$', 'ClassMgrList', name='listclass'),
    url(r'^admin/class/edit/(?P<ID>\d+)/$', 'EditClass', name='editclass'),
    url(r'^admin/class/del/(?P<ID>\d+)/$', 'DelClass', name='delclass'),

    url(r'^debug/random/student/add/$', 'RandomAddStudent', name='dbg_randstudents'),

)
