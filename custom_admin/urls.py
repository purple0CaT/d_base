# In urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('', views.dashboard_view, name='custom_admin'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('raw_query/', views.raw_query, name='raw_query'),
]
