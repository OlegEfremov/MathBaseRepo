from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
import json

from apps.Main.constants import path
from apps.Main.decorators import friends_check, admin_check
from apps.Main.models import Source_Folder, Source, TaskNumber, Solution, Task, Chapter, Solution_Folder
from apps.Solution_Catalog.views import end_of_show_tasks


@user_passes_test(friends_check)
def main_page(request):
    sources = Source.objects.all()
    return render(request, 'Edit_Source_Catalog/main_page.html', {'path': path, 'sources': sources})


def rename_node(request):
    data = json.loads(request.POST['data'])
    if data['dbType'] == 'Source_Folder':
        folder = Source_Folder.objects.get(id=data['dbID'])
        folder.name = data['new_name']
        folder.save()

    if data['dbType'] == 'Source':
        source = Source.objects.get(id=data['dbID'])
        source.name = data['new_name']
        source.save()

    if data['dbType'] == 'TaskNumber':
        task_number = TaskNumber.objects.get(id=data['dbID'])
        task_number.body = data['new_name']
        task_number.save()

    if data['dbType'] == 'Chapter':
        chapter = Chapter.objects.get(id=data['dbID'])
        chapter.name = data['new_name']
        chapter.save()

    return HttpResponse('{}')


def copy_node(request):
    data = json.loads(request.POST['data'])

    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    if data['dbType'] == 'Source':
        source = Source.objects.get(id=data['dbID'])
        new_parent = Source_Folder.objects.get(id=data['new_parent_dbID'])
        source.folders.add(new_parent)
        source.save()

    if data['dbType'] == 'Source_Folder':
        new_folder = recurs_for_copy_folder(data['new_parent_dbID'], data['dbID'], current_user)

    if data['dbType'] == 'Task_Number':
        print(data['new_parent_dbID'])
        print(data['dbID'])
        print(data['old_parent_dbID'])

    return HttpResponse('{}')


def recurs_for_copy_folder(new_parent_dbID, dbID, current_user):
    folder = Source_Folder.objects.get(id=dbID)

    name = folder.name
    parent = Source_Folder.objects.get(id=new_parent_dbID)

    new_folder = Source_Folder(name=name, parent=parent, author=current_user)
    new_folder.save()

    for child in folder.sources.all():
        child.folders.add(new_folder)

    for child in folder.subfolders.all():
        recurs_for_copy_folder(new_folder.id, child.id, current_user)

    return new_folder


def move_node(request):
    data = json.loads(request.POST['data'])

    if data['dbType'] == 'Source_Folder':
        folder = Source_Folder.objects.get(id=data['dbID'])
        new_parent = Source_Folder.objects.get(id=data['new_parent_dbID'])
        folder.parent = new_parent
        folder.save()

    if data['dbType'] == 'Source':
        source = Source.objects.get(id=data['dbID'])
        new_parent = Source_Folder.objects.get(id=data['new_parent_dbID'])
        old_parent = Source_Folder.objects.get(id=data['old_parent_dbID'])

        if old_parent.system_name != 'ALL_SOURCES':
            source.folders.remove(old_parent)

        source.folders.add(new_parent)
        source.save()

    if data['dbType'] == 'Chapter':
        chapter = Chapter.objects.get(id=data['dbID'])

        new_parent_dbType = data['new_parent_dbType']
        if new_parent_dbType == 'Source':
            new_parent = Source.objects.get(id=data['new_parent_dbID'])
        elif new_parent_dbType == 'Chapter':
            new_parent = Chapter.objects.get(id=data['new_parent_dbID'])
        else:
            return HttpResponse('{}')

        # old_parent_dbType = data['old_parent_dbType']
        # if old_parent_dbType == 'Source':
        #     old_parent = Source.objects.get(id=data['old_parent_dbID'])
        # elif old_parent_dbType == 'Chapter':
        #     old_parent = Chapter.objects.get(id=data['old_parent_dbID'])
        # else:
        #     return HttpResponse('{}')

        chapter.parent = new_parent
        chapter.save()

    if data['dbType'] == 'TaskNumber':

        tasknumber = TaskNumber.objects.get(id=data['dbID'])

        if (data['new_parent_dbType'] == 'Chapter'):
            new_parent = Chapter.objects.get(id=data['new_parent_dbID'])
            tasknumber.chapter = new_parent
            tasknumber.source = new_parent.source
            tasknumber.save()
        elif (data['new_parent_dbType'] == 'Source'):
            new_parent = Source.objects.get(id=data['new_parent_dbID'])
            tasknumber.chapter = None
            tasknumber.source = new_parent
            tasknumber.save()

    return HttpResponse('{}')


def create_source_folder(request):
    data = json.loads(request.POST['data'])

    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    parent_folder = Source_Folder.objects.get(id=data['node_dbID'])

    new_folder = Source_Folder(name='Новый источник', author=current_user)
    new_folder.save()
    new_folder.parent = parent_folder
    new_folder.save()

    return HttpResponse('{"dbID": "' + str(new_folder.id) + '", "dbType": "Source_Folder"}')


def create_source(request):
    data = json.loads(request.POST['data'])

    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    parent_folder = Source_Folder.objects.get(id=data['node_dbID'])

    new_source = Source(name='Новый источник', author=current_user)
    new_source.save()
    new_source.folders.add(parent_folder)

    return HttpResponse('{"dbID": "' + str(new_source.id) + '", "dbType": "Source"}')


def create_task_number(request):
    data = json.loads(request.POST['data'])

    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    if data['node_dbType'] == 'TaskNumber':
        source = Source.objects.get(id=data['parent_dbID'])
        chapter = None
    if data['node_dbType'] == 'Source':
        source = Source.objects.get(id=data['node_dbID'])
        chapter = None
    if data['node_dbType'] == 'Chapter':
        chapter = Chapter.objects.get(id=data['node_dbID'])
        source = chapter.source

    new_task_number = TaskNumber(body='Новый номер задачи', source=source, author=current_user, chapter=chapter)
    new_task_number.save()

    return HttpResponse('{"dbID": "' + str(new_task_number.id) + '", "dbType": "TaskNumber"}')


def create_chapter(request):
    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    data = json.loads(request.POST.get('data'))
    node_dbType = data['node_dbType']
    node_dbID = data['node_dbID']
    parent_dbType = data['parent_dbType']
    parent_dbID = data['parent_dbID']
    if node_dbType == 'Source':
        source = Source.objects.get(id=node_dbID)
        new_chapter = Chapter(name='Новая глава', parent=None, source=source, system_name='DEFAULT',
                              author=current_user, order='00000')
        new_chapter.save()
    elif node_dbType == 'Chapter':
        chapter = Chapter.objects.get(id=node_dbID)
        new_chapter = Chapter(name='Новая глава', parent=chapter, source=chapter.source, system_name='DEFAULT',
                              author=current_user, order='00000')
        new_chapter.save()

    return HttpResponse('{}')


def create_task(request):
    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    data = json.loads(request.POST.get('data'))
    node_dbType = data['node_dbType']
    node_dbID = data['node_dbID']
    parent_dbType = data['parent_dbType']
    parent_dbID = data['parent_dbID']

    if node_dbType == 'Source':
        source = Source.objects.get(id=node_dbID)

        new_task_number = TaskNumber(body='Новый номер задачи', source=source, author=current_user, chapter=None,
                                     order='9999999')
        new_task_number.save()
        new_task = Task(body='Новая задача', ans='ответ не заполнен', author=current_user)
        new_task.save()
        new_task.taskNumber.add(new_task_number)
        new_task.save()
        new_sol = Solution(name='Новое решение', body='Решение не заполнено', task=new_task, author=current_user)
        new_sol.save()

    elif node_dbType == 'Chapter':
        chapter = Chapter.objects.get(id=node_dbID)

        new_task_number = TaskNumber(body='Новый номер задачи', source=chapter.source, author=current_user,
                                     chapter=chapter, order='9999999')
        new_task_number.save()
        new_task = Task(body='Новая задача', ans='ответ не заполнен', author=current_user)
        new_task.save()
        new_task.taskNumber.add(new_task_number)
        new_task.save()
        new_sol = Solution(name='Новое решение', body='Решение не заполнено', task=new_task, author=current_user)
        new_sol.save()

    elif node_dbType == 'TaskNumber':
        pass

    return HttpResponse('{}')


def delete_node_from_db(request):
    data = json.loads(request.POST['data'])
    if data['dbType'] == 'Source':
        mathattr = Source.objects.get(id=data['dbID'])
        mathattr.delete()

    if data['dbType'] == 'Source_Folder':
        folder = Source_Folder.objects.get(id=data['dbID'])
        folder.delete()

    if data['dbType'] == 'TaskNumber':
        task_number = TaskNumber.objects.get(id=data['dbID'])
        task_number.delete()

    if data['dbType'] == 'Chapter':
        chapter = Chapter.objects.get(id=data['dbID'])
        chapter.delete()

    return HttpResponse('{}')


# Delete source from folder, but not from database
def remove_node_from_folder(request):
    data = json.loads(request.POST['data'])

    if data['dbType'] == 'Source':
        source = Source.objects.get(id=data['dbID'])
        parent_folder_dbID = data['parent_dbID']
        parent_folder = Source_Folder.objects.get(id=parent_folder_dbID)
        source.folders.remove(parent_folder)

    return HttpResponse('{}')


def get_all_tasknumbers_in_chapter_tree(chapter, tasknumber_set):
    tasknumber_set = set(chapter.tasknumbers.all()) | tasknumber_set
    for subchapter in chapter.subchapters.all():
        tasknumber_set = tasknumber_set | get_all_tasknumbers_in_chapter_tree(subchapter, tasknumber_set)
    return tasknumber_set


def get_all_sols_from_catalog(root_folder, sols_set):
    sols_set = sols_set | set(root_folder.solution.all())
    for subfolder in root_folder.subfolders.all():
        sols_set = sols_set | get_all_sols_from_catalog(subfolder, sols_set)

    return sols_set


def show_tasks(request):
    dbID = request.POST.get('dbID')
    dbType = request.POST.get('dbType')

    if dbType == 'Chapter':
        chapter = Chapter.objects.get(id=dbID)
        task_numbers = get_all_tasknumbers_in_chapter_tree(chapter, set())
        all_tasks = Task.objects.filter(taskNumber__in=task_numbers)
        solutions_set = Solution.objects.filter(task__in=all_tasks)
        url = 'Chapter'
    elif dbType == 'Source':
        source = Source.objects.get(id=dbID)
        task_numbers = source.tasknumbers.all()
        all_tasks = Task.objects.filter(taskNumber__in=task_numbers)
        solutions_set = Solution.objects.filter(task__in=all_tasks)
        url = 'Source'
    elif dbType == 'TaskNumber':
        task_number = TaskNumber.objects.get(id=dbID)
        all_tasks = task_number.tasks.all()
        solutions_set = Solution.objects.filter(task__in=all_tasks)
        url = 'TaskNumber'
    else:
        all_tasks = []
        solutions_set = []
        url = 'Source_Folder'

    template_path = 'Table_Of_Tasks/table_of_tasks.html'

    tasks_only_outside_catalog = request.POST.get('tasks_only_outside_catalog')

    if tasks_only_outside_catalog == 'true':
        sol_folders = Solution_Folder.objects.all()
        sol_folders_root = sol_folders.get(system_name='SYSTEM_ROOT_CATALOG')
        sols_in_catalog = get_all_sols_from_catalog(sol_folders_root, set())

        solutions_set = set(solutions_set) - sols_in_catalog
        all_tasks = all_tasks.filter(solutions__in=solutions_set)

    data = {'all_tasks': all_tasks, 'solutions_set': solutions_set, 'request': request,
            'template_path': template_path, 'url': url, 'tasks_order': '', 'sol_folder': None}

    return end_of_show_tasks(data)


#
#
# def show_tasks(request):
#     data = json.loads(request.POST['data'])
#     dbID = data['solution_folder_dbID']
#     sol_folder = Solution_Folder.objects.get(id=dbID)
#
#     solutions_set = sol_folder.solution.all()
#     all_tasks = Task.objects.filter(solutions__in=solutions_set).distinct().order_by('id')
#
#     tasks_order = json.loads(sol_folder.tasks_order)
#
#
#     # match if all_tasks and tasks_order the same
#     tasks_order_new = match_tasks_order_and_all_tasks_in_sol_folder(all_tasks, tasks_order)
#     if tasks_order != tasks_order_new:
#         tasks_order = tasks_order_new
#         sol_folder.tasks_order = json.dumps(tasks_order)
#         sol_folder.save()
#
#
#     for key in tasks_order:
#         tasks_order[key] = int(tasks_order[key])
#
#     a = sorted(tasks_order.items(), key=lambda x: x[1])
#     b = []
#     for i in  a:
#         b.append(Task.objects.get(id=i[0]))
#
#     template_path = 'Table_Of_Tasks/table_of_tasks.html'
#     url = 'show_tasks'
#
#     # if request.path.count('view_user_catalog/show_tasks') == 1:
#     #     # template_path = 'Solution_Catalog/view_user_catalog/Table_Of_Tasks/table_of_tasks.html'
#     #     template_path = 'Table_Of_Tasks/table_of_tasks.html'
#     #
#     # if request.path.count('view_system_catalog/show_tasks') == 1:
#     #     # template_path = 'Solution_Catalog/view_system_catalog/Table_Of_Tasks/table_of_tasks.html'
#     #     template_path = 'Table_Of_Tasks/table_of_tasks.html'
#     #
#     # if request.path.count('edit_system_catalog/show_tasks') == 1:
#     #     # template_path = 'Solution_Catalog/edit_system_catalog/Table_Of_Tasks/table_of_tasks.html'
#     #
#
#     data = {'all_tasks': b, 'solutions_set': solutions_set, 'request': request,
#             'template_path': template_path, 'url': url, 'tasks_order': json.dumps(tasks_order)}
#
#     return end_of_show_tasks(data)
#
#
# def end_of_show_tasks(data):
#     all_tasks = data['all_tasks']
#     solutions_set = data['solutions_set']
#     request = data['request']
#     template_path = data['template_path']
#     url = data['url']
#     tasks_order = data['tasks_order']
#
#     all_checkboxes = ''
#     for t in all_tasks:
#         all_checkboxes += 'checkbox_task_' + str(t.id) + ';'
#
#     for t in solutions_set:
#         all_checkboxes += 'checkbox_sol_' + str(t.id) + ';'
#
#     if all_checkboxes != '':
#         all_checkboxes = all_checkboxes[0:-1]
#
#     page = request.POST.get('page')
#     per_page = request.POST.get('per_page')
#
#     paginator = Paginator(all_tasks, per_page)
#     tasks = paginator.get_page(page)
#     sols = Solution.objects.filter(task__in=tasks)
#
#     all_sols = Solution.objects.filter(task__in=all_tasks)
#     another_solutions = set(all_sols) - set(solutions_set)
#     return render(request, template_path,
#                   {'path': path, 'tasks': tasks, 'solutions_set': solutions_set,
#                    'url': url, 'all_checkboxes': all_checkboxes, 'tasks_order': tasks_order,
#                    'sols': sols, 'all_tasks': all_tasks, 'all_sols': solutions_set, 'another_solutions': another_solutions})


def import_tasks(request):
    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    data = json.loads(request.POST.get('data'))
    node_dbType = data['node_dbType']
    node_dbID = data['node_dbID']
    parent_dbType = data['parent_dbType']
    parent_dbID = data['parent_dbID']

    csv_text = request.POST.get('csv_text')
    task_strings = csv_text.split('@end_string@')
    for task_string in task_strings:
        if task_string != '':  # last element can be empty string because of last @end_string@
            task_fields = task_string.split('@')
            task_number_order = task_fields[2]
            task_number_body = task_fields[3]
            task_body = task_fields[4]
            task_ans = task_fields[5]
            sol_instruction = task_fields[6]

            if node_dbType == 'Chapter':
                chapter = Chapter.objects.get(id=int(node_dbID))
                source = chapter.source
            if node_dbType == 'Source':
                chapter = None
                source = Source.objects.get(id=int(node_dbID))

            new_task_number = TaskNumber(body=task_number_body, source=source, author=current_user, chapter=chapter,
                                         order=task_number_order)
            new_task_number.save()
            new_task = Task(body=task_body, ans=task_ans, author=current_user)
            new_task.save()
            new_task.taskNumber.add(new_task_number)
            new_task.save()
            new_sol = Solution(name='Новое решение', body='Решение не заполнено', task=new_task, author=current_user,
                               instruction=sol_instruction)
            new_sol.save()

    return HttpResponse('{}')


def export_tasknumbers_csv(request):
    dbID = request.POST['dbID']
    dbType = request.POST['dbType']

    if dbType == 'Source':
        source = Source.objects.get(id=dbID)
        tasknumber_set = source.tasknumbers.all()
    elif dbType == 'Chapter':
        chapter = Chapter.objects.get(id=dbID)
        tasknumber_set = get_all_tasknumbers_in_chapter_tree(chapter, set())
    elif dbType == 'TaskNumber':
        tasknumber_set = TaskNumber.objects.get(id=dbID)

    DELIMITER = '@'
    csv = ''
    csv += 'id@body@order@source@chapter@author'
    for tn in tasknumber_set:
        line = ''
        line += str(tn.id) + DELIMITER
        line += str(tn.body) + DELIMITER
        line += str(tn.order) + DELIMITER
        line += str(tn.source.id) + DELIMITER
        line += str(tn.chapter.id) + DELIMITER
        line += str(tn.author.id)
        csv += '\n' + line
    resp = HttpResponse(csv, content_type='text/plain')
    resp['Content-Disposition'] = 'attachment; filename=tasknumbers'
    return resp


def export_tasks_csv(request):
    dbID = request.POST['dbID']
    dbType = request.POST['dbType']

    if dbType == 'Source':
        source = Source.objects.get(id=dbID)
        tasknumber_set = source.tasknumbers.all()
    elif dbType == 'Chapter':
        chapter = Chapter.objects.get(id=dbID)
        tasknumber_set = get_all_tasknumbers_in_chapter_tree(chapter, set())
    elif dbType == 'TaskNumber':
        tasknumber_set = TaskNumber.objects.get(id=dbID)

    tasks = Task.objects.filter(taskNumber__in=tasknumber_set).distinct()

    DELIMITER = '@'
    csv = ''
    csv += 'id@body@ans@taskNumber@author@comment@pic_task@mpfile_task@pic1@pic2@mpfile1@mpfile2'
    for t in tasks:

        line = ''
        line += str(t.id) + DELIMITER
        line += '#' + str(t.body) + '#' + DELIMITER
        line += '#' + str(t.ans) + '#' + DELIMITER

        tn_ids = []
        for tn in t.taskNumber.all():
            tn_ids.append(str(tn.id))
        tn_ids_all = ','.join(tn_ids)

        line += '#' + str(tn_ids_all) + '#' + DELIMITER
        line += str(t.author.id) + DELIMITER
        line += '#' + str(t.comment) + '#' + DELIMITER
        line += str(t.pic_task) + DELIMITER
        line += str(t.mpfile_task) + DELIMITER
        line += str(t.pic1) + DELIMITER
        line += str(t.pic2) + DELIMITER
        line += str(t.mpfile1) + DELIMITER
        line += str(t.mpfile2)
        csv += '\n' + line

    resp = HttpResponse(csv, content_type='text/plain')
    resp['Content-Disposition'] = 'attachment; filename=tasks'
    return resp


def find_task_by_source_and_number(request):
    source_name = request.POST['source']
    tasknumber = request.POST['tasknumber']

    all_t = Task.objects.all().filter(taskNumber__source__name__icontains=source_name)

    if len(tasknumber) > 2 and tasknumber[-1] == '@' and tasknumber[0] == '@':
        tasknumber = tasknumber[1:-1]
        all_tasks = all_t.filter(taskNumber__body=tasknumber)
    else:
        all_tasks = all_t.filter(taskNumber__body__icontains=tasknumber)

    solutions = Solution.objects.all().filter(task__in=all_tasks)

    all_sols = Solution.objects.filter(task__in=all_tasks)
    another_solutions = set(all_sols) - set(solutions)

    tasks = all_tasks
    sols = solutions

    template_path = 'Table_Of_Tasks/table_of_tasks.html'

    data = {'all_tasks': all_tasks, 'solutions_set': solutions, 'request': request,
            'template_path': template_path, 'url': 'find_task_by_source_and_number', 'tasks_order': '',
            'sol_folder': None}

    return end_of_show_tasks(data)
    # return render(request, 'Table_Of_Tasks/table_of_tasks.html',
    #               {'another_solutions': another_solutions, 'all_sols': all_sols,
    #                'all_tasks': all_tasks, 'tasks': tasks, 'sols': sols, 'solutions_set': solutions, 'path': path})


@user_passes_test(admin_check)
def edit_and_import(request):
    sources = Source.objects.all()
    return render(request, 'Edit_Source_Catalog/edit_and_import.html', {'path': path, 'sources': sources})


def test_csv(request):
    csv_text = request.POST['csv_text']

    task_strings = csv_text.split('@end_string@')
    for task_string in task_strings:
        if task_string != '':  # last element can be empty string because of last @end_string@
            task_fields = task_string.split('@')
            task_number_order = task_fields[2]
            task_number_body = task_fields[3]
            task_body = task_fields[4]
            task_ans = task_fields[5]
            sol_instruction = task_fields[6]

    return HttpResponse(csv_text)
