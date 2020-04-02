from django.shortcuts import render

# Create your views here.
from apps.Main.constants import path
from apps.Main.models import Task, Solution


def get_table_of_tasks(request):
    tasks = Task.objects.all()
    solutions_set = Solution.objects.all()
    return render(request, 'Table_Of_Tasks/table_of_tasks_page.html', {'path': path, 'tasks':tasks, 'solutions_set':solutions_set})