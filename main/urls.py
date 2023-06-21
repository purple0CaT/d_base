from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('todo/<str:method_type>', views.handle_update_delete),
    path('about/', views.about),
]