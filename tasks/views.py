from django.shortcuts import render,redirect,get_object_or_404
from .models import Tasks
# Create your views here.
from.forms import task_creationform


def tasklist(request):
    tasks=Tasks.objects.all().order_by('created_at')
    return render(request , 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method=='POST':
        form = task_creationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
         form = task_creationform()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        form = task_creationform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = task_creationform(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})