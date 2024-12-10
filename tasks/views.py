from django.shortcuts import render
from .models import Task

# Create your views here.


def home(request):
  task = ''
  if request.method == 'POST':
    task = request.POST.get('task')
    new_task = Task(taskName=task)
    new_task.save()
    print(task)

    tasks = Task.objects.all()  # Retrieve all tasks to display
    return render(request, 'index.html', {'tasks': tasks})

  return render(request, 'index.html', {})