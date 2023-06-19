from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
import json
from django.http import HttpResponse


# Create your views here.

def home(request):
    homePage = 'home.html'
    context = {'csrf_token': request.META['CSRF_COOKIE'], 'todos': [], 'error': None}
    # Create
    if(request.method == 'POST'):
        form = TodoForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context['error'] = 'Invalid form'
            return render(request,homePage,context)
    # Update
    elif(request.method == 'PUT'):
        json_data = json.loads(request.body)
        todo = Todo.objects.get(id=json_data['todo_id'])
        if todo.action == 'none':
            todo.action = 'done'
        else:
            todo.action = 'none'
        todo.save()

        context['todos'] = Todo.objects.order_by('created_at')
        return render(request,homePage,context)   
    # Delete
    elif(request.method == 'DELETE'):
        json_data = json.loads(request.body)
        todo = Todo.objects.get(id=json_data['todo_id'])
        todo.delete()

        context['todos'] = Todo.objects.order_by('created_at')
        return render(request,homePage,context)    # Read
    else:
        context['todos'] = Todo.objects.order_by('created_at')
        return render(request,homePage,context)

def about(request):
    return render(request,'about.html')