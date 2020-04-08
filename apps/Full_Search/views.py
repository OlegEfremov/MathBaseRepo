import json
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from apps.Full_Search.lib import make_attr_tree, filterQuery, makeMathAttributeTree
from apps.Main.constants import path
from apps.Main.models import MathAttribute_Folder, Solution, MathAttribute, Task
from apps.Main.decorators import admin_check, log_file
from django.contrib.auth.decorators import user_passes_test

def user_main_page(request):

    return render(request, 'Full_Search/user/main_page.html', {'path': path})


@user_passes_test(admin_check)
def sys_main_page(request):

    return render(request, 'Full_Search/system/main_page.html', {'path': path})


#формирует и отдает json для дерева атрибутов на странице 'Расширенного фильтра'
def attr_tree(request):

    tree = []

    # Выделяем папки в корне дерева атрибутов. От них будет строиться дерево
    all_folders = MathAttribute_Folder.objects.all()
    root_folders = all_folders.exclude(parent__in=all_folders)

    for folder in root_folders:
        tree.append(make_attr_tree(folder))

    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')


# Принимает json текущего фильтра со страницы Расширенного поиска, ищет в базе все подходящие решения
# Возвращает таблицу условий и решений
def show_tasks(request):

    json_tree = request.POST['json_tree']
    json_tree = json.loads(json_tree)
    solutions = filterQuery(json_tree[0], Solution.objects.all())
    all_tasks = Task.objects.all().filter(solutions__in=solutions).distinct()
    all_tasks = all_tasks.order_by('id')

    all_sols=Solution.objects.filter(task__in=all_tasks)
    another_solutions = set(all_sols)-set(solutions)

    page = request.POST.get('page')
    per_page = request.POST.get('per_page')

    paginator = Paginator(all_tasks, per_page)
    tasks = paginator.get_page(page)
    sols = Solution.objects.filter(task__in=tasks)


    # mathattributes = MathAttribute.objects.all().filter(solutions__in = solutions).distinct()

    # if request.path.count('system/show_tasks') == 1:
        # return render(request, 'Solution_Catalog/edit_system_catalog/Table_Of_Tasks/table_of_tasks.html', {'all_tasks': all_tasks, 'tasks': tasks, 'solutions_set': solutions, 'path': path})

    # return render(request, 'Table_Of_Tasks/table_of_tasks.html',
    #               {'all_tasks': all_tasks, 'tasks': tasks, 'solutions_set': solutions, 'path': path})
    # if request.path.count('user/show_tasks') == 1:
    return render(request, 'Table_Of_Tasks/table_of_tasks.html',
                      {'another_solutions': another_solutions, 'all_sols': all_sols,
                       'all_tasks': all_tasks, 'tasks': tasks, 'sols': sols, 'solutions_set': solutions, 'path': path})

def get_json_all_mathattr_in_filter(request):
    json_tree = request.POST['json_tree']
    json_tree = json.loads(json_tree)
    solutions = filterQuery(json_tree[0], Solution.objects.all())
    tasks = Task.objects.all().filter(solutions__in=solutions).distinct()
    mathattributes = MathAttribute.objects.all().filter(solutions__in = solutions).distinct()

    tree = (makeMathAttributeTree(mathattributes))

    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Принимает json текущего фильтра со страницы Расширенного поиска, ищет в базе все подходящие решения
# Возвращает таблицу условий и решений
def find_task_by_id(request):

    task_id = request.POST['task_id']
    log_file("post: " + task_id)

    if not is_int(task_id):
        all_tasks = Task.objects.all().filter(id=0)
    else:
        all_tasks = Task.objects.all().filter(id=task_id)


    solutions = Solution.objects.all().filter(task__in=all_tasks)

    all_sols=Solution.objects.filter(task__in=all_tasks)
    another_solutions = set(all_sols)-set(solutions)

    tasks = all_tasks
    sols = solutions

    for ts in tasks:
        log_file("task id: "+str(ts.pk))

    return render(request, 'Table_Of_Tasks/table_of_tasks.html',
                      {'another_solutions': another_solutions, 'all_sols': all_sols,
                       'all_tasks': all_tasks, 'tasks': tasks, 'sols': sols, 'solutions_set': solutions, 'path': path})
