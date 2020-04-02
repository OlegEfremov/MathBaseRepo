import json

from django.http import HttpResponse
from django.shortcuts import render

from apps.Main.constants import path
from apps.Main.lib import get_current_user
from apps.Main.models import Test_Folder, Test_Generated


def get_user_test_folder_root(current_user):
    test_folders = Test_Folder.objects.all()
    test_folders_root = test_folders.filter(system_name='ROOT_CATALOG')
    test_folder_user_root_is_exists = test_folders_root.filter(author=current_user)

    if not test_folder_user_root_is_exists:
        new_test_folder_user_root = Test_Folder(name='Созданные работы', system_name='ROOT_CATALOG', parent=None,
                                                   author=current_user)
        new_test_folder_user_root.save()

    test_folders = Test_Folder.objects.all()
    test_folders_root = test_folders.filter(system_name='ROOT_CATALOG')
    test_folder_user_root = test_folders_root.get(author=current_user)
    return test_folder_user_root

def get_test_folder_tree(request):
    current_user = get_current_user(request)
    test_folder_user_root = get_user_test_folder_root(current_user)

    tree = [make_test_folder_tree(test_folder_user_root)]
    tree_json = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(tree_json, content_type='json')


def make_test_folder_tree(rootElement):
    a = dict()
    #тут есть проблемы с переименованием вершин - счетчик вклеивается в название папки и множится
    #это дырка, которую надо править
    # solutions = rootElement.solution.all()
    # tasks = Task.objects.filter(solutions__in=solutions)
    # number_of_tasks = len(tasks)
    # if number_of_tasks == 0:
    #     a["text"] = rootElement.name
    # else:
    #     a["text"] = rootElement.name + ' (' + str(number_of_tasks) + ')'
    #конец лажового кода
    a["text"] = rootElement.name
    a["data"] = rootElement.name
    a["type"] = 'Folder'
    a["state"] = {"opened": False, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "Test_Folder", "dbID": str(rootElement.id), 'system_name': rootElement.system_name}
    a["children"] = []
    for child in rootElement.subfolders.all().order_by('name'):
        a['children'].append(make_test_folder_tree(child))

    return a



def test_folder_new_child_chapter(request):
    current_test_folder_dbID = request.POST.get('current_test_folder_dbID')
    current_user = get_current_user(request)

    current_test_folder = Test_Folder.objects.get(id=current_test_folder_dbID)
    new_test_folder = Test_Folder(name='Новая папка', parent=current_test_folder, system_name='DEFAULT', author=current_user)
    new_test_folder.save()

    print(current_test_folder)
    return HttpResponse(current_test_folder_dbID)


def rename_test_folder(request):
    dbID = request.POST.get('dbID')
    new_name = request.POST.get('new_name')
    test_folder = Test_Folder.objects.get(id=dbID)
    test_folder.name = new_name
    test_folder.save()

    return HttpResponse('{}')


def copy_test_folder(request):
    node_dbID=request.POST.get('node_dbID')
    new_parent_dbID = request.POST.get('new_parent_dbID')

    test_folder = Test_Folder.objects.get(id=node_dbID)
    new_parent = Test_Folder.objects.get(id=new_parent_dbID)

    return HttpResponse('{}')

def move_test_folder(request):
    node_dbID= request.POST.get('node_dbID')
    new_parent_dbID = request.POST.get('new_parent_dbID')
    old_parent_dbID = request.POST.get('old_parent_dbID')

    test_folder = Test_Folder.objects.get(id=node_dbID)
    new_parent = Test_Folder.objects.get(id=new_parent_dbID)
    old_parent = Test_Folder.objects.get(id=old_parent_dbID)

    test_folder.parent = new_parent
    test_folder.save()

    return HttpResponse('{}')

def delete_test_folder_from_db(request):
    dbID = request.POST.get('dbID')
    test_folder = Test_Folder.objects.get(id=dbID)
    test_folder.delete()
    return HttpResponse('{}')

def show_tests_in_folder(request):
    current_test_fodler_dbID = request.POST.get('current_test_folder_dbID')
    current_test_folder = Test_Folder.objects.get(id=current_test_fodler_dbID)

    tests = current_test_folder.test.all().order_by('-id')

    template_path = "Test_Generated/tests_in_test_folder.html"
    return render(request, template_path,
                  {'path': path, 'tests': tests})

def show_all_user_tests(request):

    tests = Test_Generated.objects.filter(author=get_current_user(request)).order_by('-id')

    template_path = "Test_Generated/tests_in_test_folder.html"

    return render(request, template_path,
                  {'path': path, 'tests': tests})

def show_user_tests_outside_folders(request):

    tests = Test_Generated.objects.filter(author=get_current_user(request))
    all_folders = Test_Folder.objects.all()
    tests_in_folder = tests.filter(test_folders__in=all_folders)
    tests_outside_folders = tests.exclude(id__in=tests_in_folder).order_by('-id')

    template_path = "Test_Generated/tests_in_test_folder.html"

    return render(request, template_path,
                  {'path': path, 'tests': tests_outside_folders})


def move_test_to_another_folder(request):
    test_id = request.POST.get('test_id')
    target_test_folder_id = request.POST.get('target_test_folder_id')

    print(target_test_folder_id)
    target_test_folder = Test_Folder.objects.get(id=target_test_folder_id)
    test = Test_Generated.objects.get(id=test_id)

    folders = test.test_folders.all()
    for folder in folders:
        folder.test.remove(test)

    target_test_folder.test.add(test)


    return HttpResponse(test_id)

