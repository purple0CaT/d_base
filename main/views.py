from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
import json
from django.http import HttpResponse


# Create your views here.

def home(request):
    # Declare context to return the the todos list and error if there is any
    context = {'todos': [], 'error': None}
    home_page = 'home.html'
    # Wrapping the code with try and except to catch any error
    try:
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
                return render(request,home_page,context)
        # Read the whole list - Get request
        else:
            # get all the data from the database table Todo and order it by the created_at field
            context['todos'] = Todo.objects.order_by('created_at')
            return render(request, home_page, context)
    # Catch any error and return it
    except Exception as e:
        print(e)
        context['error'] = 'Invalid method'
        return render(request,home_page,context)

def handle_update_delete(request, method_type):
    # Declare context to return the todos list and error if there is any
    context = {'todos': [], 'error': None}
    home_page = 'home.html'
    # Wrapping the code with try and except to catch any error
    try:
        # Declare context object that will return the token (to secure the form from CSRF attacks) and
        # also will return aditional information that we will render in html (todos list, and errors if there is any)
        if(request.method == 'POST'):
                # extract the data from the form
                todo_id = request.POST.get('todo_id')
                # get the specific todo object from the database by his id (searching by id)
                todo = Todo.objects.get(id=todo_id)
                # Update method
                if(method_type == 'update'):
                    # check if the action is none, if it's none then change it to done, else change it to none
                    if todo.action == 'none':
                        todo.action = 'done'
                    else:
                        todo.action = 'none'
                    # save the changes to the database
                    todo.save()
                    # redirect to the specific url
                    return redirect('/')

                # Delete Method
                elif(method_type == 'delete'):
                    # delete the object from the database
                    todo.delete()
                    return redirect('/')
                else:
                    context['error'] = 'Invalid method!'
                    return render(request,home_page,context)
        else:
            context['error'] = 'Invalid request'
            return render(request,home_page,context)
    # Catch any error and return it
    except Exception as e:
        print(e)
        context['error'] = 'Invalid request'
        return render(request,home_page,context)


def about(request):
    return render(request,'about.html')