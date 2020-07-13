from django.urls import path

from BDA import views

urlpatterns = [
    path('',views.bdaloginpage,name='bdaloginpage')
]