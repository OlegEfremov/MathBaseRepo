from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

# Create your views here.
from apps.Edit_Source_Catalog.lib import makeChapterTree_node, makeSourceTree_node, makeSourceFolderTree_node
from apps.Edit_Task.forms import TaskForm
from apps.Edit_Task.lib import makeTaskSourceTree, makeSourceTree, makeChapterTree
from apps.Main.constants import path
from apps.Main.models import TaskNumber, Task, Solution, Source_Folder, Chapter, Source

import os

def main_page(request, task_id):
    task = Task.objects.get(id=task_id)
    taskform = TaskForm(request.POST or None, initial={'body':task.body, 'ans':task.ans})
    taskform.is_valid()

    if (taskform.is_valid()):
        newbody = taskform.cleaned_data.get('body')
        newans = taskform.cleaned_data.get('ans')
        Task.objects.filter(pk=task_id).update(body=newbody, ans=newans)
        # return redirect(advsearch)

    task = Task.objects.get(id=task_id)
    all_solutions = Solution.objects.all()

    return render(request, 'Edit_Task/main_page.html', {'task': task, 'tasks': [task], 'taskform':taskform, 'path': path, 'solutions_set': all_solutions})


def source_tree(request):
    tree = makeSourceTree(Source_Folder.objects.get(system_name='ROOT_SOURCES'))
    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')

def source_node_tree(request, dbID):

    tree = makeSourceTree_node(Source.objects.get(id=dbID))

    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')


def chapter_node_tree(request, dbID):

    tree = makeChapterTree_node(Chapter.objects.get(id=dbID))

    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')


def source_folder_node_tree(request, dbID):

    tree = makeSourceFolderTree_node(Source_Folder.objects.get(id=dbID))
    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')


def tasksource_tree(request, task_id=0):
    task = Task.objects.get(id=task_id)
    tasksourcetree = makeTaskSourceTree(task)

    tree=[]
    tree.append(tasksourcetree)
    print(3434567)
    print(tree)
    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')


def delete_tasknumber_from_task(request):

    data = request.POST

    node_dbType = data['node_dbType']
    node_dbID = data['node_dbID']
    taskid = data['taskid']

    task = Task.objects.get(id=taskid)
    if node_dbType == 'taskNumber':
        node = TaskNumber.objects.get(id=node_dbID)
        task.taskNumber.remove(node)

    return HttpResponse('hi')


def add_task_number_to_task(request):

    data = request.POST

    node_dbType = data['node_dbType']
    node_dbID = data['node_dbID']
    taskid = data['taskid']

    task = Task.objects.get(id=taskid)

    if node_dbType == 'TaskNumber':
        node = TaskNumber.objects.get(id=node_dbID)
        task.taskNumber.add(node)

    return HttpResponse('hi')


def deletetask(request, task_id=0):
    task = Task.objects.get(id=task_id)
    Solution.objects.all().filter(task = task).delete()
    task.delete()


def show_tasks(request):
    data = json.loads(request.GET['data'])
    task_id = data['task_id']

    tasks = [Task.objects.get(id=task_id)]
    solutions_set = tasks[0].solutions.all()


    return render(request, 'Edit_Task/table_of_tasks.html',
                  {'path': path, 'tasks': tasks, 'solutions_set': solutions_set})


def save_task(request):
    data = json.loads(request.POST['data'])

    task = Task.objects.get(id=data['task_id'])
    task.body = data['new_body']
    task.ans = data['new_ans']
    task.save()
    # os.mkdir('static/images/for_tasks_and_sols/')

    return HttpResponse('{}')


def create_new_solution(request):
    data = json.loads(request.POST['data'])

    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    task = Task.objects.get(id=data['task_id'])
    newsol = Solution(task = task, name='Новое Решение', body='Заполните решение', author = current_user)
    newsol.save()

    return HttpResponse('{}')

def delete_solution(request):
    data = json.loads(request.POST['data'])

    sol = Solution.objects.get(id=data['sol_id'])
    sol.delete()
    return HttpResponse('hi')
