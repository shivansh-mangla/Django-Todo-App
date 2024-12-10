from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.


def home(request):
  task = ''
  if request.method == 'POST':
    task = request.POST.get('task')
    new_task = Task(taskName=task)
    new_task.save()

  tasks = Task.objects.all()  # Retrieve all tasks to display
  return render(request, 'index.html', {'tasks': tasks})


def deleteTask(request, task_id):
  task = get_object_or_404(Task, id=task_id)
  task.delete()  # Delete the task
  return redirect('main-page')


def updateTask(request, task_id):
  task = get_object_or_404(Task, id=task_id)
  task.completed = not task.completed
  task.save()
  return redirect('main-page')