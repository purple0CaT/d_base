from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .utils import check_if_admin
from django.db import connection

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_superuser:
            login(request, user)
            return redirect('/custom_admin/')
        else:
            return redirect('/custom_admin/login/')
    else:
        return render(request, 'login.html')


@login_required(login_url="login/")
def dashboard_view(request):
    check_if_admin(request)

    return render(request,'dash.html')



@login_required(login_url="login/")
def logout_view(request):
    logout(request)
    return redirect('/custom_admin/login')


@login_required(login_url="login/")
def raw_query(request):
    context={'todos':[]}
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM main_todo")
        rows = cursor.fetchall()
        # Process the query results
        todos = []
        for row in rows:
            # Create a dictionary or an object to represent the todo
            todo = {
                'id': row[0],
                'name': row[1],
                'action': row[2],
                # ... Add other attributes as needed
            }
            todos.append(todo)
        context['todos']=todos

    return render(request,'dash.html',context)
