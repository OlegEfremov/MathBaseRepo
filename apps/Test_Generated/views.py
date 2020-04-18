import random

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.Main.constants import path
from apps.Main.decorators import reader_check
from apps.Main.lib import get_current_user
from apps.Main.models import Test_Generated, Solution_Folder, Task, Solution, Test_Template, Test_Folder
from apps.Main.py.Test_Folder.test_folder_tree import get_user_test_folder_root
from apps.Solution_Catalog.views import make_solution_folders_tree

import json

from apps.Test_Generated.forms import TestTemplateForm


def view_test(request, test_id):

    if len(Test_Generated.objects.filter(id=test_id))==0:

        template_path = "Test_Generated/main_page.html"
        return render(request, template_path,
               {'path': path, 'tasks': [], 'test': [], 'test_exists': False})
    else:
        test = Test_Generated.objects.get(id=test_id)
        tasks = []
        for task_id in test.tasks_order.split(','):
            tasks.append(Task.objects.filter(id=task_id))

        template_path = "Test_Generated/main_page.html"

        test_folders = test.test_folders.all()

        return render(request, template_path,
                      {'path': path, 'tasks': tasks, 'test': test, 'test_exists': True, 'test_folders': test_folders})

def make_new_test(request):
    num = int(request.POST.get('number_of_tasks_in_new_test'))
    sol_folder_id = request.POST.get('view_folder')
    sol_folder = Solution_Folder.objects.get(id=sol_folder_id)
    solutions_set = sol_folder.solution.all()
    tasks = Task.objects.filter(solutions__in=solutions_set).distinct()
    random.seed()


    new_test = Test_Generated(author=get_current_user(request))
    new_test.save()

    lla = list(tasks)
    random.shuffle(lla)

    tasks_order = ''
    for i in range(num):
        new_test.task.add(lla[i])
        tasks_order += ',' + str(lla[i].id)

    tasks_order = tasks_order[1:]
    new_test.tasks_order = tasks_order
    new_test.name = request.POST.get('test_name')
    new_test.comment = request.POST.get('test_comment')
    new_test.save()


    return HttpResponse(new_test.id)


@user_passes_test(reader_check)
def test_from_many_folders(request):

    user = get_current_user(request)
    templates = Test_Template.objects.filter(author=user)

    template_path = "Test_Generated/test_from_many_folders.html"
    return render(request, template_path,
                  {'path': path, 'templates': templates})

def get_all_solutions_set_from_all_subfolders(sol_folder, solutions_set):

    solutions_set = set(solutions_set) | set(sol_folder.solution.all())
    for subfolder in sol_folder.subfolders.all():
        solutions_set = set(solutions_set) | set(get_all_solutions_set_from_all_subfolders(subfolder, solutions_set))

    return solutions_set

def create_test_from_many_folders(request):
    string_of_folders_dbID = request.POST.get('data')
    folders_dbID = string_of_folders_dbID.split(',')

    string_numbers_of_tasks_from_folders = request.POST.get('array_of_inputs_values')
    numbers_of_tasks_from_folders = string_numbers_of_tasks_from_folders.split(',')

    test_template = []
    for i in range(len(folders_dbID)):
        test_template.append([folders_dbID[i],numbers_of_tasks_from_folders[i]])

    new_test = create_test_by_template_string(request, test_template)

    new_test.name = request.POST.get('test_name')
    new_test.comment = request.POST.get('test_comment')
    new_test.save()

    #create not named test template. user will not see it, but can recompile test
    folders = folders_dbID = string_of_folders_dbID.split(',')
    num_of_tasks = numbers_of_tasks_from_folders
    new_template = Test_Template()
    new_template.author = get_current_user(request)
    new_template.name = 'DEFAULT'
    new_template.comment = 'DEFAULT'

    folders_and_numbers =  []
    for i in range(len(folders)):
        folders_and_numbers.append(folders[i]+','+num_of_tasks[i])

    new_template.folders_and_numbers = '@'.join(folders_and_numbers)
    new_template.is_permanent = False
    new_template.save()

    new_test.template = new_template
    new_test.save()

    # user_test_folder_root = get_user_test_folder_root(get_current_user(request))
    # user_test_folder_root.test.add(new_test)

    current_test_folder_id = request.POST.get('current_test_folder')
    current_test_folder = Test_Folder.objects.get(id=current_test_folder_id)
    current_test_folder.test.add(new_test)

    return HttpResponse(new_test.id)

def create_test_template(request):
    folders = request.POST.get('folders').split(',')
    num_of_tasks = request.POST.get('inputs_values').split(',')


    new_template = Test_Template()
    new_template.author = get_current_user(request)
    new_template.name = request.POST.get('template_name')
    new_template.comment = request.POST.get('template_comment')

    folders_and_numbers =  []
    for i in range(len(folders)):
        folders_and_numbers.append(folders[i]+','+num_of_tasks[i])

    new_template.folders_and_numbers = '@'.join(folders_and_numbers)
    new_template.is_permanent = True
    new_template.save()

    return HttpResponse(str(new_template.name)+'@'+str(new_template.id))


@user_passes_test(reader_check)
def created_tests(request):

    tests = Test_Generated.objects.filter(author=get_current_user(request))

    template_path = "Test_Generated/created_tests.html"
    return render(request, template_path,
                  {'path': path, 'tests': tests})


@user_passes_test(reader_check)
def create_test_from_cart(request):

    current_test_folder_id= request.POST.get('current_test_folder')
    test_name = request.POST.get('test_name')
    test_comment = request.POST.get('test_comment')

    task_order = request.POST['data']
    tasks_id = task_order.split(',')
    tasks = []
    for task_id in tasks_id:
        task = Task.objects.get(id=task_id)
        tasks.append(task)

    new_test = Test_Generated(author=get_current_user(request))
    new_test.name = test_name
    new_test.comment = test_comment
    new_test.save()

    for task in tasks:
        new_test.task.add(task)

    new_test.tasks_order = task_order

    test_folder = Test_Folder.objects.get(id=current_test_folder_id)
    test_folder.test.add(new_test)

    new_test.save()

    return HttpResponse(new_test.id)


def recompile_test(request):
    test_id = request.POST.get('test_id')

    test = Test_Generated.objects.get(id=test_id)

    template = test.template

    folders_and_numbers = template.folders_and_numbers.split('@')
    for i in range(len(folders_and_numbers)):
        folders_and_numbers[i] = folders_and_numbers[i].split(',')



    task_array = []

    test_template = template.folders_and_numbers.split('@')
    for i in range(len(test_template)):
        folder_dbID = test_template[i].split(',')[0]
        num_of_tasks = test_template[i].split(',')[1]

        sol_folder = Solution_Folder.objects.get(id=folder_dbID)
        solutions_set = sol_folder.solution.all()
        solutions_set = get_all_solutions_set_from_all_subfolders(sol_folder, [])
        tasks = Task.objects.filter(solutions__in=solutions_set).distinct()
        random.seed()

        lla = list(tasks)
        if len(lla) == 0:
            return 'Folder is empty'

        random.shuffle(lla)
        for j in range(int(num_of_tasks)):
            task_array.append(lla[j])

    test.task.clear()
    task_order = ''
    for task in task_array:
        task_order += ','+str(task.id)
        test.task.add(task)
    task_order = task_order[1:]
    test.tasks_order = task_order

    test.save()

    return HttpResponse(test.id)

def create_test_by_template(request):
    template_id = request.POST.get('template_id')

    template = Test_Template.objects.get(id=template_id)

    folders_and_numbers = template.folders_and_numbers.split('@')
    for i in range(len(folders_and_numbers)):
        folders_and_numbers[i] = folders_and_numbers[i].split(',')

    new_test = create_test_by_template_string(request, folders_and_numbers)

    # new_test.name = template.name
    # new_test.comment = template.comment

    new_test.name = request.POST.get('test_name')
    new_test.comment = request.POST.get('test_comment')
    new_test.template = template

    new_test.save()

    current_test_folder_id = request.POST.get('current_test_folder')
    print(current_test_folder_id)
    current_test_folder = Test_Folder.objects.get(id = current_test_folder_id)
    current_test_folder.test.add(new_test)

    return HttpResponse(new_test.id)



def create_test_by_template_string(request, test_template):
    new_test = Test_Generated(author=get_current_user(request))
    task_array = []

    for i in range(len(test_template)):
        folder_dbID = test_template[i][0]
        num_of_tasks = test_template[i][1]

        sol_folder = Solution_Folder.objects.get(id=folder_dbID)
        solutions_set = sol_folder.solution.all()
        solutions_set = get_all_solutions_set_from_all_subfolders(sol_folder, [])
        tasks = Task.objects.filter(solutions__in=solutions_set).distinct()
        random.seed()

        lla = list(tasks)
        if len(lla) == 0:
            return 'Folder is empty'

        random.shuffle(lla)
        for j in range(int(num_of_tasks)):
            task_array.append(lla[j])

    new_test.save()
    task_order = ''
    for task in task_array:
        task_order += ','+str(task.id)
        new_test.task.add(task)
    task_order = task_order[1:]
    new_test.tasks_order = task_order

    new_test.save()

    return new_test

def save_test_name_and_comment(request):

    new_test_name = request.POST.get('test_name')
    new_test_comment = request.POST.get('test_comment')
    test_id = request.POST.get('test_id')


    test = Test_Generated.objects.get(id=str(test_id))
    user = get_current_user(request)
    if user == test.author:
        test.name = new_test_name
        test.comment = new_test_comment
        test.save()

    return HttpResponse('{}')

def archive_test(request):
    test_id = request.POST.get('test_id')
    test = Test_Generated.objects.get(id=test_id)

    test.is_archived = not test.is_archived
    test.save()

    return HttpResponse('success')

def random_change_task_in_test(request):
    task_number = int(request.POST.get('task_number'))

    test_id = request.POST.get('test_id')
    test = Test_Generated.objects.get(id=test_id)
    template = test.template

    folders_and_numbers = template.folders_and_numbers.split('@')
    for i in range(len(folders_and_numbers)):
        folders_and_numbers[i] = folders_and_numbers[i].split(',')

    task_array = []

    # template.solders_and_numbers = '123,3@234,4@folder_id, num_of_tasks_from_this_folder'
    test_template = template.folders_and_numbers.split('@')
    test_template_full = []
    for i in range(len(test_template)):
        folder_dbID = test_template[i].split(',')[0]
        num_of_tasks = int(test_template[i].split(',')[1])
        for j in range(num_of_tasks):
            test_template_full.append(folder_dbID)

    folder_dbID = test_template_full[task_number-1]
    sol_folder = Solution_Folder.objects.get(id=folder_dbID)
    solutions_set = sol_folder.solution.all()
    solutions_set = get_all_solutions_set_from_all_subfolders(sol_folder, [])
    tasks = Task.objects.filter(solutions__in=solutions_set).distinct()
    random.seed()
    lla = list(tasks)
    if len(lla) == 0:
        return 'Folder is empty'

    tasks_order = test.tasks_order.split(',')
    new_task_is_unique = False
    while new_task_is_unique != True:
        random.shuffle(lla)
        new_task = lla[0]
        if str(new_task.id) in tasks_order:
            new_task_is_unique = False
        else:
            new_task_is_unique = True

    # tasks_order = '123,1234,523,task_id,...'
    tasks_order = test.tasks_order.split(',')
    tasks_order[task_number-1] = str(new_task.id)

    test.task.clear()
    for task_id in tasks_order:
        task = Task.objects.get(id=task_id)
        test.task.add(task)
    test.tasks_order = ','.join(tasks_order)

    test.save()

    return HttpResponse(test.id)

def  open_test_answers(request):
    test_id = request.POST.get('test_id')
    is_open = request.POST.get('is_open')

    test = Test_Generated.objects.get(id=test_id)

    if is_open == 'true':
        test.open_answers = True
    else:
        test.open_answers = False

    test.save()

    return HttpResponse('{}')


class TestTemplateUpdateView(UpdateView):
    template_name = 'Test_Generated/template_update.html'
    model = Test_Template
    form_class = TestTemplateForm
    success_url = reverse_lazy(test_from_many_folders)

