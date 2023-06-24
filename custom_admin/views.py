from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user.is_superuser:
            login(request, user)
            return redirect('/custom_admin/')
        else:
            return redirect('/custom_admin/login/')
    else:
        return render(request, 'login.html')


@login_required(login_url="login/")
def dashboard_view(request):
    if not request.user.is_superuser:
        logout(request)
        return redirect('/custom_admin/login')
    else:
        
        return render(request,'dash.html')



@login_required(login_url="/custom_admin/login/")
def logout_view(request):
    logout(request)
    return redirect('/custom_admin/login')