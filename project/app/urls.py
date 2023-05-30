from django.urls import path
from . import views

urlpatterns=[
    path('function/', views.function, name='function'),
    path('testing/',views.testing,name='testing'),
    path('test/', views.test,name='test'),
    path('tag/', views.tag,name='tag'),
    path('common/',views.common,name='common'),
    path('proper/',views.proper,name='proper')
]