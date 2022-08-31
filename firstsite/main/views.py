from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')[:3]
    return render(request, "main/index.html", {'title': 'Главная страница сайта', 'tasks': tasks})


def review(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Неизвестная ошибка"

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, "main/review.html", context)