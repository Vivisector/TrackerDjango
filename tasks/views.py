from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.status != 'done':  # Проверяем, что статус еще не "Done"
        task.status = 'done'
        task.progress = 100
        task.save()
    return redirect(f"{reverse('task_list')}?page={request.GET.get('page', 1)}")


    # Перенаправляем обратно на ту же страницу
    return HttpResponseRedirect(f"{reverse('task_list')}?page={current_page}")


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    current_page = request.GET.get('page', 1)  # Получаем номер текущей страницы (по умолчанию 1)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            # После сохранения возвращаемся на текущую страницу
            return HttpResponseRedirect(f"{reverse('task_list')}?page={current_page}")
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task, 'current_page': current_page})


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
