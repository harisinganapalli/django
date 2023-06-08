from django.urls import path
from . import views

urlpatterns=[
    path('function/', views.function, name='function'),
    path('testing/',views.testing,name='testing'),
    path('test/', views.test,name='test'),
    path('tag/', views.tag,name='tag'),
    path('common/',views.common,name='common'),
    path('proper/',views.proper,name='proper'),
    path('loops/',views.loops,name='loops'),
    path('query/',views.query,name='query'),
    path('particular/',views.particular,name='particular'),
    path('rare/', views.rare, name='rare'),
    path('bootstrap/',views.bootstrap,name='bootstrap'),
    path('boot/', views.boot,name='boot'),
    path('stylecss/',views.stylecss,name='stylecss'),
    # path('',views.employeeform),
    path('employeelist/',views.employeelist,name='employeelist'),
    path('studentform/',views.studentform,name="studentform")
    
    
]