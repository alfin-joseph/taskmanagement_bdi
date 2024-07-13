from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task', views.add_task, name='add_task'),
    path('edit_task', views.edit_task, name='edit_task'),
    path('tasks/', views.TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
]
