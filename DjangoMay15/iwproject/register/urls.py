from .import views
from django.urls import path

urlpatterns=[
    path('form/',views.index,name='form'),
    path('',views.form,name='index'),
    path('register/',views.registration,name='registration'),
]