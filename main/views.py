from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
import json
from django.http import HttpResponse


# Create your views here.

def home(request):
    homePage = 'home.html'
    # Declare context to return the token each time, to secure the form from CSRF attacks
    # Also return the todos list and error if there is any
    context = {'csrf_token': request.META['CSRF_COOKIE'], 'todos': [], 'error': None}
    # Create method
    if(request.method == 'POST'):
        # extract the data from the form
        form = TodoForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # save the data to database, you need to declere the form with Meta tag, check the forms.py
            form.save()
            # redirect to the home page so it can read the data from the database and display it
            return redirect('/')
        else:
            context['error'] = 'Invalid form'
            return render(request,homePage,context)
    # Update method
    elif(request.method == 'PUT'):
        # extract the data from the request body
        json_data = json.loads(request.body)
        # get the specific todo object from the database by his id (searching by id)
        todo = Todo.objects.get(id=json_data['todo_id'])
        if(todo):
            # check if the action is none, if it is none then change it to done, else change it to none
            if todo.action == 'none':
                todo.action = 'done'
            else:
                todo.action = 'none'
            # save the changes to the database
            todo.save()
            # return updated data
            context['todos'] = Todo.objects.order_by('created_at')
            return render(request,homePage,context)
        # return error if the object doesn't exist
        else:
            context['error'] = 'Invalid id'
            return render(request,homePage,context)
    # Delete Method
    elif(request.method == 'DELETE'):
        # extract the data from the request body
        json_data = json.loads(request.body)
        # get the specific todo object from the database by his id (searching by id)
        todo = Todo.objects.get(id=json_data['todo_id'])
        # delete the object from the database if it's exist
        if(todo):
            todo.delete()
            context['todos'] = Todo.objects.order_by('created_at')
            return render(request,homePage,context)    # Read
        # return error if the object doesn't exist
        else:
            context['error'] = 'Invalid id'
            return render(request,homePage,context)
    # Read the whole list
    else:
        # get all the data from the database and order it by the created_at field
        context['todos'] = Todo.objects.order_by('created_at')
        return render(request,homePage,context)

def about(request):
    return render(request,'about.html')