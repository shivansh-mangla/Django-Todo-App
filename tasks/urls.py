from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='main-page'),
  path('update-task/<int:task_id>/', views.updateTask, name='update_task'),
  path('delete-task/<int:task_id>/', views.deleteTask, name='delete_task'),
]