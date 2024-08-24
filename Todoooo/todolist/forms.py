from django import forms

class TaskForm(forms.Form):
    foooorm = forms.CharField(label="Название задачи", max_length=100)