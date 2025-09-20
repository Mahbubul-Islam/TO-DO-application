from django.shortcuts import render, redirect, get_object_or_404
from . models import Task

# Create your views here.
# 1. Task list:
def task_list(request): # this function will handel list and filter of tasks
    status_filter = request.GET.get('status', 'all') # get the request from the user. get('key', 'value') by default the value is all
    category_filter = request.GET.get('category', 'all')

    tasks = Task.objects.filter(user = request.user) # get the tasks of the user
    
    if status_filter != 'all':
        tasks = tasks.filter(is_completed = (status_filter == 'completed'))
    if category_filter != 'all':
        tasks = tasks.filter(category = category_filter)
        
    completed_task = tasks.filter(is_completed = True)
    pending_task = tasks.filter(is_completed = False)
    
    return render(request, '', {
        'status_filter':status_filter,
        'category_filter': category_filter,
        'completed_task': completed_task,
        'pending_task': pending_task
    })