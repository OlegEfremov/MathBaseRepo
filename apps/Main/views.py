from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

import json
import re

# Create your views here.
from django.urls import reverse

from apps.Edit_Task.forms import TaskImagesUploadForm
from apps.Edit_Solution.forms import SolutionImagesUploadForm
from apps.Main.constants import path
from apps.Main.lib import get_current_user
from apps.Main.models import Solution, Task, Star_Folder
from apps.Solution_Catalog.views import svg2png, getzip
from LBBASE_v_0_40.settings import MEDIA_ROOT
from shutil import copyfile


def main_page(request):

    return redirect('../accounts/login/')


def read_checkbox_values(request):
    user = get_current_user(request)
    if user.is_authenticated:
        star_folder = get_or_create_star_folder(user)
        checkbox_values = json.loads(star_folder.checkbox_values)
        return JsonResponse(checkbox_values)
    else:
        return HttpResponse('user_not_auth')

def write_checkbox_values(request):
    checkbox_values = request.POST.get('checkbox_values')
    user = get_current_user(request)
    if user.is_authenticated:
        user.star_folder.checkbox_values = checkbox_values
        user.star_folder.save()
        return HttpResponse('true')
    else:
        return HttpResponse('user_not_auth')

def get_or_create_star_folder(user):
    try:
        star_folder = user.star_folder
    except:
        new_star_folder = Star_Folder()
        new_star_folder.user = user
        new_star_folder.checkbox_values = json.dumps({})
        new_star_folder.save()
        star_folder = new_star_folder
    return star_folder


def set_star_folder(checkbox_values, request):
    user = get_current_user(request)
    star_folder = get_or_create_star_folder(user)
    star_folder.checkbox_values = json.dumps(checkbox_values)

    return True


def get_list_of_sols_id_in_task(request):
    task_id = request.POST.get('task_id')
    task = Task.objects.get(id=task_id)
    sols = task.solutions.all()
    list_of_sols_id = []
    for sol in sols:
        list_of_sols_id.append(str(sol.id))
    list_of_sols_id = ','.join(list_of_sols_id)
    return HttpResponse(list_of_sols_id)


def count_checkboxes(request):
    user = get_current_user(request)
    if user.is_authenticated:
        star_folder = get_or_create_star_folder(user)
        checkbox_values = json.loads(star_folder.checkbox_values)
    else:
        checkbox_values = request.POST.get('checkbox_values')
        checkbox_values = json.loads(checkbox_values)

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
    another_tasks = Task.objects.filter(id__in=list_of_tasks_id)

    tasks = set(tasks) | set(another_tasks)

    return HttpResponse(str(len(tasks))+ '('+str(len(solutions_set))+')')

def count_squares(request):
    square_values = request.POST.get('square_values')

    square_values = json.loads(square_values)

    list_of_tasks_id = []
    list_of_sols_id = []
    for key, value in square_values.items():
        if value:
            if 'task' in key:
                list_of_tasks_id.append(key.replace('square_task_',''))
            if 'sol' in key:
                list_of_sols_id.append(key.replace('square_sol_',''))

    solutions_set = Solution.objects.filter(id__in=list_of_sols_id)

    tasks = Task.objects.filter(solutions__in=solutions_set).distinct()
    another_tasks = Task.objects.filter(id__in=list_of_tasks_id)

    tasks = set(tasks) | set(another_tasks)

    s = '' + str(len(tasks)) + '(' + str(len(solutions_set)) + ')'

    return HttpResponse(s)

def try_page(request):
    return render(request, 'Main/try.html', {'path': path})


import random
import string
import os
import shutil
import sys
import subprocess
import io

def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


# generate tex inner, data - is settings to compile
def get_tex_with_pics(data):
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
                print(sol)
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

    return filenames, file_inner

#write tex file to path directory
def make_tex(settings, path, filename):
    path_to_pics, tex_file_inner = get_tex_with_pics(settings)

    for fpath in path_to_pics:
        fdir, fname = os.path.split(fpath)
        copyfile(fpath, path + fname)

    f = io.open(path + filename+'.tex', mode = 'w+', encoding='utf8')
    f.write(tex_file_inner)
    f.close()

    return filename+'.tex'

def make_pdf(path, filename):
    original_dir = os.getcwd()
    os.chdir(path)
    subprocess.call('pdflatex -halt-on-error '+filename+'.tex', shell=True)
    os.chdir(original_dir)

    success_pdf = os.path.isfile(path + '/' + filename + '.pdf')

    return success_pdf


def export_as_file(request):

    filename = generate_key(40) #without extension
    path = 'static/tex_files/' + filename + '/'
    if not os.path.exists(path):
        os.makedirs(path)

    settings = json.loads(request.POST.get('data'))
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


# Загрузка рисунков условий задач
def task_image_upload(request, task_id):
    form = TaskImagesUploadForm()
    if request.method == 'POST':
        form = TaskImagesUploadForm(request.POST, request.FILES)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.task = Task.objects.get(pk=task_id)
            frm.save()
            return HttpResponseRedirect(reverse("task_main_page", args=[task_id]))
        else:
            return HttpResponse("Ошибка проверки ввода")

    else:
        context = {"form": form, 'task_id': task_id}
        return render(request, 'Main/image_upload.html',  context)


# Загрузка рисунков решений
def sol_image_upload(request, sol_id):
    form = SolutionImagesUploadForm()
    if request.method == 'POST':
        form = SolutionImagesUploadForm(request.POST, request.FILES)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.solution = Solution.objects.get(pk=sol_id)
            frm.save()
            return HttpResponseRedirect(reverse("sol_main_page", args=[sol_id]))
    else:
        context = {"form": form}
        return render(request, 'Main/image_upload.html',  context)
