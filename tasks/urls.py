from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),  # Новый маршрут для добавления задач
    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),
]
