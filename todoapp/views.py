from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TodoForm
from .models import Todo

# Create your views here.
def home(request):
    todo = Todo.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = TodoForm()

    content = {
        "form":form,
        "todo":todo
    }
    return render(request, 'todoapp/home.html',content)


def remove(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('home')


def update(request,pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST,instance = todo)
        if form.is_valid():
            form.save()
            return redirect("home")


    content = {
        'form':form
    }

    return render(request, 'todoapp/update.html', content)