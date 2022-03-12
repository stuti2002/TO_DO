from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('',views.home,name='home'),
    path('tasks/',views.tasks,name='tasks'),
    path('delete/<str:pk>/',views.delete,name='delete')
]           