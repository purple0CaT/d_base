from django.db import models

# Create your models here.
class Todo(models.Model):
    ACTION_CHOICES = (
        ('done', 'Done'),
        ('none', 'None'),
    )
    name = models.CharField(max_length=255)
    action = models.CharField(max_length=4, choices=ACTION_CHOICES, default='none')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class Feedback(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    user_type = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
