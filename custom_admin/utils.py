from django.shortcuts import redirect
from django.contrib.auth import logout


def check_if_admin(request):
        if not request.user.is_superuser:
            logout(request)
            return redirect('/custom_admin/login')