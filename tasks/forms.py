from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Añade una nueva tarea ..'}))

    class Meta:

        model = Task
        fields = '__all__'
