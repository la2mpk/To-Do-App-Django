from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks:index')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/index.html', context)


def update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks:index')

    context = {'form': form}
    return render(request, 'tasks/update.html', context)


def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')

    context = {'task': task}
    return render(request, 'tasks/delete.html', context)
