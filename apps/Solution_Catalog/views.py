import json
import os
import re
import io
import zipfile
import cairosvg
import random

from django.contrib.auth.decorators import user_passes_test

from apps.Main.decorators import admin_check, reader_check, editor_check, sol_folder_check

random.seed()

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
import io

# Create your views here.
from LBBASE_v_0_40.settings import MEDIA_ROOT
from apps.Main.constants import path
from apps.Main.lib import get_current_user
from apps.Main.models import Solution_Folder, Task, Solution, MathAttribute, Test_Generated
from apps.Solution_Catalog.sub_views.copy_move_remove_task_or_solution import task_copy, \
    task_move, task_remove, solution_copy, solution_move, solution_remove, massive_action, add_attribute_to_solution


def main_page(request):
    if request.path.count('view_user_catalog/main_page') == 1:
        if reader_check(request.user):
            return render(request, 'Solution_Catalog/view_user_catalog/main_page.html', {'path': path})
        else:
            return HttpResponseForbidden('У вас недостаточно прав для доступа.')

    if request.path.count('view_system_catalog/main_page') == 1:
        return render(request, 'Solution_Catalog/view_system_catalog/main_page.html', {'path': path})

    if request.path.count('edit_system_catalog/main_page') == 1:
        if admin_check(request.user):
            return render(request, 'Solution_Catalog/edit_system_catalog/main_page.html', {'path': path})

    return HttpResponse('{}')


def make_solution_folders_tree(rootElement):
    a = dict()
    #тут есть проблемы с переименованием вершин - счетчик вклеивается в название папки и множится
    #это дырка, которую надо править
    solutions = rootElement.solution.all()
    tasks = Task.objects.filter(solutions__in=solutions)
    number_of_tasks = len(tasks)
    if number_of_tasks == 0:
        a["text"] = rootElement.name
    else:
        a["text"] = rootElement.name + ' (' + str(number_of_tasks) + ')'
    #конец лажового кода
    # a["text"] = rootElement.name
    a["data"] = rootElement.name
    a["type"] = 'Folder'
    a["state"] = {"opened": False, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "Solution_Folder", "dbID": str(rootElement.id), 'system_name': rootElement.system_name}
    a["children"] = []
    for child in rootElement.subfolders.all().order_by('name'):
        a['children'].append(make_solution_folders_tree(child))

    return a


def get_main_tree(request):
    sol_folders = Solution_Folder.objects.all()
    sol_folders_root = sol_folders.get(system_name='SYSTEM_ROOT_CATALOG')

    tree = [make_solution_folders_tree(sol_folders_root)]
    tree_json = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(tree_json, content_type='json')


def get_user_tree(request):
    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    sol_folders = Solution_Folder.objects.all()
    sol_folders_root = sol_folders.filter(system_name='ROOT_CATALOG')
    sol_folder_user_root_is_exists = sol_folders_root.filter(author=current_user)

    if not sol_folder_user_root_is_exists:
        new_sol_folder_user_root = Solution_Folder(name='Мой каталог', system_name='ROOT_CATALOG', parent=None,
                                                   author=current_user)
        new_sol_folder_user_root.save()

    sol_folders = Solution_Folder.objects.all()
    sol_folders_root = sol_folders.filter(system_name='ROOT_CATALOG')
    sol_folder_user_root = sol_folders_root.get(author=current_user)

    tree = [make_solution_folders_tree(sol_folder_user_root)]
    tree_json = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(tree_json, content_type='json')


def copy_move_remove_task_or_solution(request):
    data = json.loads(request.POST['data'])
    print(data)

    if data['action_type'] == 'task_copy':
        if sol_folder_check(request.user, data['target_folder']):
            task_copy(data)
        else:
            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции копирования задачи')

    if data['action_type'] == 'task_move':
        if sol_folder_check(request.user, data['view_folder']):
            task_move(data)
        else:
            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции перемещения задачи')

    if data['action_type'] == 'task_remove':
        if sol_folder_check(request.user, data['view_folder']):
            task_remove(data)
        else:
            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции удаления задачи')

    if data['action_type'] == 'solution_copy':
#        if sol_folder_check(request.user, data['target_folder']):
            solution_copy(data)
#        else:
#            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции копирования решения')

    if data['action_type'] == 'solution_move':
        if sol_folder_check(request.user, data['target_folder']):
            solution_move(data)
        else:
            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции перемещения решения')

    if data['action_type'] == 'solution_remove':
        if sol_folder_check(request.user, data['view_folder']):
            solution_remove(data)
        else:
            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции удаления решения')

    if data['action_type'] == 'add_attribute_to_solution':
        if editor_check(request.user):
            add_attribute_to_solution(data)
        else:
            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции добаления атрибутов решений')

    if data['action_type'] == 'massive_copy':
#        if sol_folder_check(request.user, data['target_folder']):
            massive_action(data)
#        else:
#            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции копирования решения')

    if data['action_type'] == 'massive_move':
        if sol_folder_check(request.user, data['target_folder']):
            massive_action(data)
        else:
            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции перемещения решения')
    if data['action_type'] == 'massive_remove':
        if sol_folder_check(request.user, data['view_folder']):
            massive_action(data)
        else:
            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции удаления решения')
    if data['action_type'] == 'massive_add_attribute_to_solution':
        if editor_check(request.user):
            massive_action(data)
        else:
            return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции добаления атрибутов решений')

    return HttpResponse('{}')


@user_passes_test(reader_check)
def recurs_for_copy_solution_folder(new_parent_dbID, dbID):
    new_parent = Solution_Folder.objects.get(id=new_parent_dbID)
    sol_folder = Solution_Folder.objects.get(id=dbID)

    new_sol_folder = Solution_Folder(name=sol_folder.name, parent=new_parent, author=sol_folder.author)
    new_sol_folder.save()
    new_sol_folder.solution.add(*list(sol_folder.solution.all()))
    new_sol_folder.save()

    for child in sol_folder.subfolders.all():
        recurs_for_copy_solution_folder(new_sol_folder.id, child.id)

    return new_sol_folder


def copy_solution_folder(request):
    data = json.loads(request.POST['data'])

    if not sol_folder_check(request.user, data['new_parent_dbID']):
        return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции копирования каталога решений')

    new_sol_folder = recurs_for_copy_solution_folder(data['new_parent_dbID'], data['dbID'])

    return HttpResponse('{"dbID":"' + str(new_sol_folder.id) + '"}')


def move_solution_folder(request):
    data = json.loads(request.POST['data'])

    if not sol_folder_check(request.user, data['dbID']):
        return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции перемещения каталога решений')

    new_parent = Solution_Folder.objects.get(id=data['new_parent_dbID'])
    sol_folder = Solution_Folder.objects.get(id=data['dbID'])

    sol_folder.parent = new_parent
    sol_folder.save()

    return HttpResponse('{}')

def delete_solution_folder(request):
    data = json.loads(request.POST['data'])
    dbID = data['dbID']

    if not sol_folder_check(request.user, dbID):
        return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции удаления каталога решений')

    sol_folder = Solution_Folder.objects.get(id=dbID)
    sol_folder.delete()

    return HttpResponse('{}')

def rename_solution_folder(request):
    data = json.loads(request.POST['data'])

    if not sol_folder_check(request.user, data['dbID']):
        return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции переименования каталога решений')

    sol_folder = Solution_Folder.objects.get(id=data['dbID'])
    sol_folder.name = data['new_name']
    sol_folder.save()

    return HttpResponse('{}')


@user_passes_test(reader_check)
def create_solution_folder(request):
    node = json.loads(request.POST['data'])

    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    sol_folders = Solution_Folder.objects.all()
    sol_folders_root = sol_folders.filter(system_name='ROOT_CATALOG')
    sol_folder_user_root = sol_folders_root.get(author=current_user)

    if node['current_folder'] == 'ROOT':
        parent_folder = sol_folder_user_root
    else:
        parent_folder = Solution_Folder.objects.get(id=node['current_folder'])

    new_sol_folder = Solution_Folder(name=node['new_name'], parent=parent_folder, author=current_user)
    new_sol_folder.save()

    return HttpResponse('{"dbID":"' + str(new_sol_folder.id) + '"}')


def show_tasks_without_solution(request):
    tasks = Task.objects.all()
    solutions_set = Solution.objects.all()
    notEmptyTask = tasks.filter(solutions__in=solutions_set)
    emptyTasks = tasks.exclude(id__in=notEmptyTask).order_by('id')

    all_tasks = emptyTasks

    tasks_order = ''
    template_path = ''
    url = 'show_tasks_without_solution'

    # if request.path.count('edit_system_catalog/show_tasks') == 1:
    #     template_path = 'Solution_Catalog/edit_system_catalog/Table_Of_Tasks/table_of_tasks.html'
    template_path = 'Table_Of_Tasks/table_of_tasks.html'

    data = {'all_tasks': all_tasks, 'solutions_set': solutions_set, 'request': request,
            'template_path': template_path,
            'url': url, 'tasks_order': tasks_order, 'sol_folder': ''}

    return end_of_show_tasks(data)

@user_passes_test(editor_check)
def create_solution_for_empty_tasks(request):
    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    tasks = Task.objects.all()
    solutions = Solution.objects.all()
    notEmptyTask = tasks.filter(solutions__in=solutions)
    emptyTask = tasks.exclude(id__in=notEmptyTask)
    k = 0
    for t in emptyTask:
        newsol = Solution(name='Новое решение', body='Решение не заполнено', task=t, author=current_user)
        newsol.save()
        k = k + 1

    return HttpResponse('Cоздано ' + str(k) + ' новых решений.')


def show_tasks_outside_folders(request):
    solution_folders = Solution_Folder.objects.all()
    solutions_inside_folders = Solution.objects.all().filter(solution_folders__in=solution_folders)
    solutions_set = Solution.objects.all().exclude(id__in=solutions_inside_folders)
    all_tasks = Task.objects.all().filter(solutions__in=solutions_set)

    tasks_order = ''
    template_path = ''
    url = 'show_tasks_outside_folders'

    # if request.path.count('edit_system_catalog/show_tasks') == 1:
    #     template_path = 'Solution_Catalog/edit_system_catalog/Table_Of_Tasks/table_of_tasks.html'

    template_path = 'Table_Of_Tasks/table_of_tasks.html'

    data = {'all_tasks': all_tasks, 'solutions_set': solutions_set, 'request': request,
            'template_path': template_path,
            'url': url, 'tasks_order': tasks_order, 'sol_folder': ''}

    return end_of_show_tasks(data)


def match_tasks_order_and_all_tasks_in_sol_folder(all_tasks, tasks_order):
    excepting_tasks_number = []
    for task in all_tasks:
        if not str(task.id) in tasks_order:
            print(task)
            tasks_order[str(task.id)] = '1000000'
            excepting_tasks_number.append(str(task.id) + ' was added')

    tasks_in_task_order_but_not_in_all_task = []
    for task in tasks_order:
        if not all_tasks.filter(id=task):
            excepting_tasks_number.append(task)
            tasks_in_task_order_but_not_in_all_task.append(task)

    for task in tasks_in_task_order_but_not_in_all_task:
        del tasks_order[task]

    if excepting_tasks_number:
        print('all_task and tasks_order are not the same set')
        print(excepting_tasks_number)
        print(tasks_order)

    return tasks_order


def show_tasks(request):
    data = json.loads(request.POST['data'])
    dbID = data['solution_folder_dbID']
    sol_folder = Solution_Folder.objects.get(id=dbID)

    solutions_set = sol_folder.solution.all()
    all_tasks = Task.objects.filter(solutions__in=solutions_set).distinct().order_by('id')

    tasks_order = json.loads(sol_folder.tasks_order)

    # match if all_tasks and tasks_order the same
    tasks_order_new = match_tasks_order_and_all_tasks_in_sol_folder(all_tasks, tasks_order)

    # if tasks_order != tasks_order_new:
    #     print(True)
    #     tasks_order = tasks_order_new
    sol_folder.tasks_order = json.dumps(tasks_order)
    sol_folder.save()

    for key in tasks_order:
        tasks_order[key] = int(tasks_order[key])

    a = sorted(tasks_order.items(), key=lambda x: x[1])
    b = []
    for i in a:
        b.append(Task.objects.get(id=i[0]))
        # if (Task.objects.filter(id=i[0]).exists()):
        #     b.append(Task.objects.get(id=i[0]))
        # else:
        #     pass

    template_path = 'Table_Of_Tasks/table_of_tasks.html'
    url = 'show_tasks'

    data = {'all_tasks': b, 'solutions_set': solutions_set, 'request': request,
            'template_path': template_path, 'url': url, 'tasks_order': json.dumps(tasks_order), 'sol_folder': sol_folder}

    return end_of_show_tasks(data)


def end_of_show_tasks(data):
    all_tasks = data['all_tasks']
    solutions_set = data['solutions_set']
    request = data['request']
    template_path = data['template_path']
    url = data['url']
    tasks_order = data['tasks_order']

    all_checkboxes = ''
    for t in all_tasks:
        all_checkboxes += 'checkbox_task_' + str(t.id) + ';'

    for t in solutions_set:
        all_checkboxes += 'checkbox_sol_' + str(t.id) + ';'

    if all_checkboxes != '':
        all_checkboxes = all_checkboxes[0:-1]

    page = request.POST.get('page')
    per_page = request.POST.get('per_page')

    paginator = Paginator(all_tasks, per_page)
    tasks = paginator.get_page(page)
    sols = Solution.objects.filter(task__in=tasks)

    all_sols = Solution.objects.filter(task__in=all_tasks)
    another_solutions = set(all_sols) - set(solutions_set)
    return render(request, template_path,
                  {'path': path, 'tasks': tasks, 'solutions_set': solutions_set,
                   'url': url, 'all_checkboxes': all_checkboxes, 'tasks_order': tasks_order,
                   'sols': sols, 'all_tasks': all_tasks, 'all_sols': solutions_set,
                   'another_solutions': another_solutions, 'sol_folder': data['sol_folder']})


@user_passes_test(editor_check)
def reorder_tasks(request):
    data = json.loads(request.POST['data'])
    solution_folder_dbID = data['solution_folder_dbID']
    order_numbers = data['order_numbers']

    sol_folder = Solution_Folder.objects.get(id=solution_folder_dbID)
    tasks_order = json.loads(sol_folder.tasks_order)

    for task_number in order_numbers:
        tasks_order[task_number] = order_numbers[task_number]

    for key in tasks_order:
        tasks_order[key] = int(tasks_order[key])
    a = sorted(tasks_order.items(), key=lambda x: x[1])

    i = 0
    for p in a:
        i = i + 1
        tasks_order[p[0]] = i

    sol_folder.tasks_order = json.dumps(tasks_order)
    sol_folder.save()

    return HttpResponse('{}')


def export_folder(request, folder_id):
    # dbID = request.GET.get('sol_folder_dbID')
    # print(dbID)
    dbID = folder_id
    sol_folder = Solution_Folder.objects.get(id=dbID)

    solutions_set = sol_folder.solution.all()
    # all_tasks = Task.objects.filter(solutions__in=solutions_set).distinct().order_by('id')

    tasks_order = json.loads(sol_folder.tasks_order)

    for key in tasks_order:
        tasks_order[key] = int(tasks_order[key])

    # a = {(id, number),(id, number),(id,number)}
    # tasks = all_tasks in right order
    a = sorted(tasks_order.items(), key=lambda x: x[1])
    tasks = []
    for i in a:
        tasks.append(Task.objects.get(id=i[0]))

    template_path = "Solution_Catalog/common/export_page/main_export_page.html"

    return render(request, template_path,
                  {'path': path, 'tasks': tasks, 'solutions_set': solutions_set})


def download_dynamic_text(request):
    data = json.loads(request.POST['data'])

    list_of_tasks_id = data['list_of_tasks_id']
    list_of_sols_id = data['list_of_sols_id']
    list_of_another_sols_id = data['list_of_another_sols_id']
    checkbox_values = data['checkbox_values']

    all_tasks = Task.objects.filter(id__in=list_of_tasks_id)
    tasks = []
    for task_id in list_of_tasks_id:
        tasks.append(all_tasks.get(id=task_id))

    with io.open("apps/Solution_Catalog/static/Solution_Catalog/tex/template.tex", 'r', encoding='utf8') as f:
        template_tex = f.read()

    file_inner = ''
    for task in tasks:

        if checkbox_values['checkbox_id_numbers']:
            file_inner += "\n\n\\z (id-" + str(task.id) + '). ' + task.body.replace('\n', '\\ \\\\\n') + '\\ \\\\'
        else:
            file_inner += "\n\n\\z " + task.body.replace('\n', '\\ \\\\\n') + '\\ \\\\'

        if checkbox_values['checkbox_answers']:
            file_inner += '\n' + 'Ответ: ' + task.ans + '\\ \\\\'

        if 'checkbox_sources' in checkbox_values.keys():
            if checkbox_values['checkbox_sources']:
                sources = []
                for taskNumber in task.taskNumber.all():
                    sources.append(taskNumber.source.name + ', №' + taskNumber.body)
                sources = '; '.join(sources)
                file_inner += '\n' + 'Источники: ' + sources + '.' + '\\ \\\\'

        if checkbox_values['checkbox_solutions']:
            for sol in task.solutions.all():
                if str(sol.id) in list_of_sols_id:
                    file_inner += '\n' + sol.name + ':\\ \\\\\n' + sol.body + '\\ \\\\'

                    if checkbox_values['checkbox_math_attributes']:
                        math_attributes = []
                        for attr in sol.mathAttribute.all():
                            math_attributes.append(attr.name)
                        math_attributes = ', '.join(math_attributes) + '.'
                        file_inner += '\nАтрибуты: ' + math_attributes + '\\ \\\\'

        if checkbox_values['checkbox_another_solutions']:
            another_solutions = ''
            for sol in task.solutions.all():
                if str(sol.id) in list_of_another_sols_id:
                    another_solutions += '\n' + sol.name + ':\\\\\n' + sol.body + '\\ \\\\'

                    if checkbox_values['checkbox_math_attributes']:
                        math_attributes = []
                        for attr in sol.mathAttribute.all():
                            math_attributes.append(attr.name)
                        math_attributes = ', '.join(math_attributes) + '.'
                        another_solutions += '\nАтрибуты: ' + math_attributes
            if another_solutions != '':
                file_inner += '\nДругие решения: \n\\\\' + another_solutions + '\\ \\\\'

    file_inner = template_tex.replace('@body@', file_inner)

    pics_links = re.findall(r"@bimg@.*?@eimg@", file_inner)

    #Следующий блок собирает по внутренности экспортируемого tex файла все ссылки на рисунки, заменяет их на латеховский код
    #и собирает все картинки в zip для скачивания, попутно конвертируя svg в png
    filenames = []
    for link in pics_links:

        path_to_pic = re.findall(r"@bimg@(.*?)@size", link)[0]
        abs_path_to_pic = path_to_pic.replace('/media', MEDIA_ROOT)

        if path_to_pic[-3:] == 'svg':
            if not os.path.isfile(abs_path_to_pic):
                svg2png(abs_path_to_pic)
            path_to_pic = path_to_pic[:-3] + 'png'
            abs_path_to_pic = abs_path_to_pic[:-3] + 'png'

        pic_name = path_to_pic.replace('/media/','')
        pic_size = re.findall(r"@size=(.*?)@style", link)[0]

        filenames.append(abs_path_to_pic)

        tex_link = '\n\\begin{figure}[H]\n\\includegraphics[height='+pic_size+'pt]{'+pic_name+'}\n\\end{figure}\n'
        file_inner = file_inner.replace(link, tex_link)

    return getzip(filenames, file_inner)
    # return HttpResponse(file_inner)


@user_passes_test(editor_check)
def create_task_in_folder(request):
    #
    # user_id = request.user.id
    # current_user = User.objects.get(id=user_id)

    new_task = Task(body='Новая задача', ans='ответ не заполнен', author=get_current_user(request))
    new_task.save()
    new_sol = Solution(name='Новое решение', body='Решение не заполнено', task=new_task,
                       author=get_current_user(request))
    new_sol.save()

    data = {'target_folder': request.POST.get('view_folder'), 'element_id': new_task.id}
    task_copy(data)

    return HttpResponse('{}')


def view_folder_as_test(request, folder_id):

    if not Solution_Folder.objects.filter(id=folder_id):
        return HttpResponse('Нет такого теста')

    folder = Solution_Folder.objects.get(id=folder_id)

    access = folder.access

    if not access:
        return HttpResponse('Доступ к тесту закрыт')

    dbID = folder_id
    sol_folder = Solution_Folder.objects.get(id=dbID)
    solutions_set = sol_folder.solution.all()
    tasks_order = json.loads(sol_folder.tasks_order)

    for key in tasks_order:
        tasks_order[key] = int(tasks_order[key])
    a = sorted(tasks_order.items(), key=lambda x: x[1])
    tasks = []
    for i in a:
        tasks.append(Task.objects.get(id=i[0]))

    if get_current_user(request) != sol_folder.author:
        template_path = "Solution_Catalog/common/view_as_test/main_view_as_test.html"
    else:
        template_path = "Solution_Catalog/common/export_page/main_export_page.html"

    return render(request, template_path,
                  {'path': path, 'tasks': tasks, 'solutions_set': solutions_set})


@user_passes_test(admin_check)
def change_folder_access_status(request):
    access_status = (request.POST['access_status'])
    if access_status == 'true':
        access_status = True
    else:
        access_status = False

    folder_id = (request.POST['folder_id'])

    folder = Solution_Folder.objects.get(id=folder_id)
    folder.access = access_status
    folder.save()

    return HttpResponse('{}')

#filenames - array of path to files
# tex_inner - string
# return response with zipfile with file from filenames and tex_inner.tex inside
def getzip(filenames, tex_inner):
    # Files (local path) to put in the .zip
    # FIXME: Change this (get paths from DB etc)

    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = "problems"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = io.BytesIO()

    # The zip compressor

    with zipfile.ZipFile(s, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:

        for fpath in filenames:
            # Calculate path for file in zip
            fdir, fname = os.path.split(fpath)
            zip_path = os.path.join(zip_subdir, fname)
            zip_path = fname

            # Add file, at correct path
            zf.write(fpath, zip_path)

        zf.writestr('problems.tex', tex_inner)


    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp


def svg2png(svg):
    # assume that 'cairosvg' exists
    cairosvg.svg2png(url=svg, write_to=svg[:-4] + '.png', dpi=250)
    return svg[:-4] + '.png'


