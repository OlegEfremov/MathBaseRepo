import os
import shutil
import subprocess

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
import json

# Create your views here.
from django.urls import reverse

from apps.Main.constants import path
from apps.Main.decorators import admin_check
from apps.Main.lib import get_current_user
from apps.Main.models import Solution, Task, Solution_Folder
from apps.Main.pdfcrow import Pdfcrow, img_to_html
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

    list_cookie = ('id_number', 'task_body', 'sources', 'answer', 'solutions', 'another_solutions', 'mathattr', 'ans_table')
    dict_cookie = dict()
    for lc in list_cookie:
        dict_cookie[lc] = request.COOKIES.get(lc, 'none')
    print(dict_cookie)

    res = render(request, template_path, {'path': path, 'tasks': tasks, 'solutions_set': solutions_set})
    # сбрасываем галочки
    res.set_cookie("id_number", "block")
    res.set_cookie("task_body", "block")

    list_cookie = ('sources', 'answer', 'solutions', 'another_solutions', 'mathattr', 'ans_table')
    for lc in list_cookie:
        res.set_cookie(lc, 'none')

    return res
#    return render(request, template_path,
#                  {'path': path, 'tasks': tasks, 'solutions_set': solutions_set})


# Запуск PhantomJs для конверсии страницы в pdf
def phantomjs_to_pdf(request):
    filename = generate_key(20) + ".pdf"
    path = 'static/pdf_files'
    if not os.path.exists(path):
        os.makedirs(path)

    original_dir = os.getcwd()
    os.chdir(path)
    args = ["phantomjs", "/usr/share/doc/phantomjs/examples/rasterize.js", reverse("show_tasks_for_pdf"), filename]
    reply = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')

    if reply.returncode == 0:
        print(reply.stdout)
        res = FileResponse(open(path + '/' + filename, "rb"), content_type="application/pdf")
        res['Content-Disposition'] = 'attachment; filename=%s' % '1.pdf'
    else:
        print(reply.stderr)
        res = HttpResponse('')

#    subprocess.call('pdflatex -halt-on-error '+filename+'.tex', shell=True)
    os.chdir(original_dir)
#    success_pdf = os.path.isfile(path + '/' + filename + '.pdf')

    # make response
#    if success_pdf:
#    else:

    return res

def convert_to_pdf(request):
    return Pdfcrow.convert(request)


# Показывает страницу со списком задач (для pdf экспорта)
def show_tasks_for_pdf(request):
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

    list_cookie = ('id_number', 'task_body', 'sources', 'answer', 'solutions', 'another_solutions', 'mathattr', 'ans_table')
    dict_cookie = dict()
    for lc in list_cookie:
        dict_cookie[lc] = request.COOKIES.get(lc, 'none')
#    print(dict_cookie)

    taskbodies = compile_image(tasks)
    solbodies = compile_image(solutions_set)

    template_path = "Export/pdf_table_of_tasks.html"

#    return render(request, template_path,
#            {'path': path, 'tasks': tasks, 'solutions_set': solutions_set, 'checkboxes': dict_cookie, 'taskbodies': taskbodies, 'solbodies': solbodies})

    return Pdfcrow.render(request, template_path,
            {'path': path, 'tasks': tasks, 'solutions_set': solutions_set, 'checkboxes': dict_cookie, 'taskbodies': taskbodies, 'solbodies': solbodies})


# Компилим рисунки в задачах и решениях
def compile_image(textblocks):
    ret = dict()
    for tb in textblocks:
        ret[tb.pk] = img_to_html(tb.body)

    return ret

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





