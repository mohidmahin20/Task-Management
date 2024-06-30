from django.shortcuts import render,redirect
from task.models import Task
from task.forms import TaskForm
def show_task(request):
    data = Task.objects.all()
    return render(request,'show_task.html',{'data': data})

def edit_task(request, id):
    task = Task.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect("show_task")
    return render(request, "add_task.html", {"form": task_form})

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect("show_task")