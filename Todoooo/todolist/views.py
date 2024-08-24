from django.shortcuts import render
from .forms import TaskForm
from django.http import HttpResponseRedirect

def pressstart(request):
    if request.method == 'POST':
        start = TaskForm(request.POST)
        if start.is_valid():
            can = start.cleaned_data['foooorm']
            tasks = request.session.get('tasks', [])
            tasks.append({'foooorm':can, 'completed':False})
            request.session['tasks'] = tasks
            return HttpResponseRedirect('/')
    else:
        start = TaskForm()
        tasks = request.session.get('tasks', []) 
    return render(request, 'aswd/work.html', {'start': start, 'tasks': tasks})