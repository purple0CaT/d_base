from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # here i say that i want to extract the name field from the form request (the input tag should have name="name")
        # you can provide other fields but they must be in the model!
        fields = ['name']
