from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'done'
    task.save()
    return redirect('task_list')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # После сохранения возвращаемся к списку задач
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})


def task_list(request):
    tasks = Task.objects.all()

    # Настраиваем пагинатор (например, 5 задач на странице)
    paginator = Paginator(tasks, 5)  # 5 объектов на странице
    page_number = request.GET.get('page')  # Получаем текущий номер страницы из параметра URL
    page_obj = paginator.get_page(page_number)  # Получаем текущую страницу
    # return render(request, 'tasks/task_list.html', {'tasks': tasks})
    print("Render function is:", render)  # Проверяем, что такое render
    return render(request, 'tasks/task_list.html', {'page_obj': page_obj})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})
