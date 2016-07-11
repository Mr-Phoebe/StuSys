from django.conf.urls import patterns, include, url

import UserMgr.views

urlpatterns = patterns('ScoreMgr.views',
    url(r'^admin/course/add/', 'AddCourse', name='addcourse'),
    url(r'^admin/course/list/', 'CourseMgrList', name='listcourse'),
    url(r'^admin/course/edit/(?P<ID>\d+)/', 'EditCourse', name='editcourse'),
    url(r'^admin/course/del/(?P<ID>\d+)/', 'DelCourse', name='delcourse'),
    url(r'^admin/course/teacher/', 'ListTeacher', name='listteacher'),
    url(r'^student/score/$', 'ListCourseScore', name='listcoursescore'),
    url(r'^teacher/course/$', 'EditScore', name='editscore'),
    url(r'^teacher/score/$', 'ListScoreOperation', name='listscoreoperation'),
)
