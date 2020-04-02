import os
import shutil

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
import json

# Create your views here.
from apps.Main.constants import path
from apps.Main.decorators import admin_check
from apps.Main.lib import get_current_user
from apps.Main.models import Solution, Task, Solution_Folder
from apps.Main.views import get_or_create_star_folder, generate_key, make_tex, make_pdf, get_tex_with_pics
from apps.Solution_Catalog.views import getzip


def main_page(request):

    template_path = "Export/main_page.html"
    return render(request, template_path, {'path': path })


@user_passes_test(admin_check)
def main_page_system(request):

    template_path = "Export/main_page_system.html"
    return render(request, template_path, {'path': path })


def show_tasks_cart(request):
    user = get_current_user(request)
    if user.is_authenticated:
        star_folder = get_or_create_star_folder(user)
        checkbox_values = json.loads(star_folder.checkbox_values)
        tasks = star_folder.get_tasks()
        solutions_set =star_folder.get_solutions()

    else:
        data = json.loads(request.POST['data'])
        checkbox_values = data['checkbox_values']

        list_of_tasks_id = []
        list_of_sols_id = []
        for key, value in checkbox_values.items():
            if value:
                if 'task' in key:
                    list_of_tasks_id.append(key.replace('checkbox_task_',''))
                if 'sol' in key:
                    list_of_sols_id.append(key.replace('checkbox_sol_',''))

        solutions_set = Solution.objects.filter(id__in=list_of_sols_id)
        tasks = Task.objects.filter(solutions__in=solutions_set).distinct()

    template_path = "Export/export_table_of_tasks.html"

    return render(request, template_path,
                  {'path': path, 'tasks': tasks, 'solutions_set': solutions_set})



def get_list_of_tasks_id_by_folder(sol_folder):
    tasks_order = json.loads(sol_folder.tasks_order)

    for key in tasks_order:
        tasks_order[key] = int(tasks_order[key])
    a = sorted(tasks_order.items(), key=lambda x: x[1])
    list_of_tasks_id = []
    for i in a:
        list_of_tasks_id.append(str(i[0]))

    return list_of_tasks_id

def get_list_of_sols_id_by_folder(sol_folder):
    solutions_set = sol_folder.solution.all()
    list_of_sols_id = []
    for sol in solutions_set:
        list_of_sols_id.append(str(sol.id))

    return list_of_sols_id

def get_list_of_another_sols_id_by_folder(sol_folder):
    solutions_set = sol_folder.solution.all()
    tasks = Task.objects.filter(solutions__in=solutions_set)
    all_sols = Solution.objects.filter(task__in=tasks)
    another_sols = set(all_sols) - set(solutions_set)

    list_of_another_sols_id = []
    for sol in another_sols:
        list_of_another_sols_id.append(str(sol.id))

    return list_of_another_sols_id



def export_folder_to_pdf(request):
    folder_id = request.POST.get('folder_id')
    sol_folder = Solution_Folder.objects.get(id=folder_id)

    settings = {
        'list_of_sols_id': get_list_of_sols_id_by_folder(sol_folder),
        'list_of_another_sols_id': get_list_of_another_sols_id_by_folder(sol_folder),
        'list_of_tasks_id': get_list_of_tasks_id_by_folder(sol_folder),
        'checkbox_values': json.loads(request.POST.get('settings'))
    }

    filename = generate_key(40) #without extension
    path = 'static/tex_files/' + filename + '/'
    if not os.path.exists(path):
        os.makedirs(path)

    make_tex(settings, path, filename)

    success_pdf = make_pdf(path, filename)

    # make response
    if success_pdf:
        res = FileResponse(open(path+'/'+filename+'.pdf', "rb"), content_type = "application/pdf")
        res['Content-Disposition'] = 'attachment; filename=%s' % '1.pdf'
    else:
        res =  HttpResponse('')

    # remove folder
    shutil.rmtree(path)
    return res


def export_folder_to_tex(request):
    folder_id = request.POST.get('folder_id')
    sol_folder = Solution_Folder.objects.get(id=folder_id)

    settings = {
        'list_of_sols_id': get_list_of_sols_id_by_folder(sol_folder),
        'list_of_another_sols_id': get_list_of_another_sols_id_by_folder(sol_folder),
        'list_of_tasks_id': get_list_of_tasks_id_by_folder(sol_folder),
        'checkbox_values': json.loads(request.POST.get('settings'))
    }


    filenames, tex_inner = get_tex_with_pics(settings)

    res = getzip(filenames, tex_inner)

    return res





