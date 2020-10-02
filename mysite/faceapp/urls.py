from django.contrib import admin
from django.urls import path
from faceapp import views

urlpatterns=[
 path('',views.faceapp),
 path('login/',views.login),
 path('register/',views.register),
 path('addFace/',views.addFace),
 path('welcome/(?P<face_id>\d+)/',views.welcome)
]
