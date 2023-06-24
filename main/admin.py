from django.contrib import admin

# Register your models here.
from .models import Todo, Feedback


admin.site.register(Todo)
admin.site.register(Feedback)