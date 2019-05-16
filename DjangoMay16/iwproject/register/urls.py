from .import views
from django.contrib import admin
from django.urls import path,include

urlpatterns=[
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',views.index,name='index'),
    path('',views.register,name='register'),
    path('submit/',views.submit,name='submit'),
    path('iwform/',views.iwform, name='iwform'),
    path('list/',views.list, name='list'),
]