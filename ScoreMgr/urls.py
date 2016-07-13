from django.conf.urls import patterns, include, url

import UserMgr.views

urlpatterns = patterns('ScoreMgr.views',
                       url(r'^admin/course/add/$', 'AddCourse', name='addcourse'),
                       url(r'^admin/course/list/$', 'CourseMgrList', name='listcourse'),
                       url(r'^admin/course/edit/(?P<ID>\d+)/$', 'EditCourse', name='editcourse'),
                       url(r'^admin/course/del/(?P<ID>\d+)/$', 'DelCourse', name='delcourse'),
                       url(r'^admin/course/teacher/$', 'ListTeacher', name='listteacher'),
                       url(r'^student/score/$', 'ListCourseScore', name='listcoursescore'),
                       url(r'^admin/course/teacher/mgr/(?P<ID>\d+)/$', 'CourseMgr', name='coursemgr'),
                       url(r'^teacher/score/$', 'ListScoreOperation', name='listscoreoperation'),
                       url(r'^teacher/mycourse/$', 'ListCourseTaught', name='listCourseTaught'),
                       url(r'^teacher/student/$', 'ListStudent', name='liststudent'),
                       url(r'^teacher/score/input/courseList/$', 'ListCourseForInput', name='listCourseForInput'),
                       url(r'^teacher/score/input/course/(?P<ID>\d+)/$', 'AddScore', name='addscore'),
                       url(r'^teacher/score/view/course/(?P<ID>\d+)/$', 'ViewScore', name='viewscore'),
                       url(r'^teacher/score/chart/course/(?P<ID>\d+)/$', 'ViewChart', name='viewchart'),
                       url(r'^teacher/score/del/(?P<ID>\d+)/$', 'DelScore', name='delscore'),
                       )
