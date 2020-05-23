from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('task/<slug:slug>/', views.task_view, name='task_view'),
    path('test/', views.test, name='codetest'),
    path('paragraph/<int:class_id>/<int:paragraph_id>', views.all_tasks, name='all_tasks'),
    path('class/<int:class_id>', views.all_paragraphs, name='all_paragraphs'),
    path('', views.program, name='school_tasks'),
]
