from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
from django.views.decorators.csrf import csrf_exempt

from LBBase_v_0_36.install.lib import path
from apps.MathAttribute.models import MathAttribute
from apps.Solution.models import Solution
from apps.AdvSearch.lib import makeAttributeTree, filterQuery, makeMathAttributeTree
from apps.Folder.models import Folder
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# отдаёт основную странницу 'Расширенного фильтра'
from apps.Task.models import Task


def advsearch(request):

    return render(request, 'AdvSearch/advsearch.html', {'path': path})

#формирует и отдает json для дерева атрибутов на странице 'Расширенного фильтра'
def attr_tree(request):

    tree = []

    # Выделяем папки в корне дерева атрибутов. От них будет строиться дерево
    all_folders = Folder.objects.all()
    root_folders = all_folders.exclude(parent__in=all_folders)

    for folder in root_folders:
        tree.append(makeAttributeTree(folder))

    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')

# Принимает json текущего фильтра со страницы Расширенного поиска, ищет в базе все подходящие решения
# Возвращает таблицу условий и решений
def show_tasks(request):


    json_tree = request.GET['json_tree']
    json_tree = json.loads(json_tree)
    solutions = filterQuery(json_tree[0], Solution.objects.all())
    tasks = Task.objects.all().filter(solutions__in=solutions).distinct()
    tasks = tasks.order_by('id')

    mathattributes = MathAttribute.objects.all().filter(solutions__in = solutions).distinct()

    page = request.GET.get('page')
    per_page = request.GET.get('per_page')

    paginator = Paginator(tasks, per_page)
    tasks_per_page = paginator.get_page(page)

    return render(request, 'AdvSearch/filtered_view.html', {'objects': tasks_per_page, 'user': request.user,
                                                            'solutions_set': solutions, 'math_attributes': mathattributes,
                                                            'view_type_func': 'javascript:show_tasks'})

def get_json_all_mathattr_in_filter(request):
    json_tree = request.GET['json_tree']
    json_tree = json.loads(json_tree)
    solutions = filterQuery(json_tree[0], Solution.objects.all())
    tasks = Task.objects.all().filter(solutions__in=solutions).distinct()
    mathattributes = MathAttribute.objects.all().filter(solutions__in = solutions).distinct()

    tree = (makeMathAttributeTree(mathattributes))

    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')

# отдаёт задачи без решений

def show_tasks_without_solution(request):
    tasks = Task.objects.all()
    solutions = Solution.objects.all()
    notEmptyTask = tasks.filter(solutions__in=solutions)
    emptyTask = tasks.exclude(id__in=notEmptyTask).order_by('id')

    per_page = request.GET.get('per_page')
    paginator = Paginator(emptyTask, per_page)

    page = request.GET.get('page')
    emptyTask_per_page = paginator.get_page(page)

    return render(request, 'AdvSearch/filtered_view.html', {'objects': emptyTask_per_page, 'view_type_func': 'javascript:show_tasks_without_solution'})

# создаёт новые решения всем пустым задачам
def create_new_sol_for_empty_tasks(request):
    tasks = Task.objects.all()
    solutions = Solution.objects.all()
    notEmptyTask = tasks.filter(solutions__in=solutions)
    emptyTask = tasks.exclude(id__in=notEmptyTask)
    for t in emptyTask:
        newsol = Solution(name = 'Новое решение', body='Решение не заполнено', task = t)
        newsol.save()
    return redirect(advsearch)

