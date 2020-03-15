from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('task/<slug:slug>/', views.task_view, name='task_view'),
    path('test/', views.test, name='codetest'),
]
