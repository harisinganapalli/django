from django.urls import path
from .views import PersonList, PersonCreate, PersonUpdate, PersonDelete

urlpatterns = [
    path('', PersonList.as_view(), name='person_list'),
    path('create/', PersonCreate.as_view(), name='person_create'),
    path('update/<int:pk>/', PersonUpdate.as_view(), name='person_update'),
    path('delete/<int:pk>/', PersonDelete.as_view(), name='person_delete'),
]
