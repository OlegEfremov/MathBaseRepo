import json

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseForbidden

from apps.Main.decorators import reader_check, editor_check, sol_folder_check
from apps.Main.models import Solution, Task, Solution_Folder
from apps.Solution_Catalog.sub_views.copy_move_remove_task_or_solution import add_task_to_tasks_order, \
    remove_task_from_to_tasks_order


def get_tasks_and_sols_from_values_list(values_list):
    list_of_tasks_id = []
    list_of_sols_id = []
    for key, value in values_list.items():
        if value:
            if 'task' in key:
                id = key.replace('checkbox_task_', '')
                id = id.replace('square_task_', '')
                list_of_tasks_id.append(id)
            elif 'sol' in key:
                id = key.replace('checkbox_sol_', '')
                id = id.replace('square_sol_', '')
                list_of_sols_id.append(id)
    solutions = Solution.objects.filter(id__in=list_of_sols_id)
    tasks = Task.objects.filter(id__in=list_of_tasks_id)

    additional_tasks = Task.objects.filter(solutions__in=solutions)
    additional_sols = Solution.objects.filter(task__in=tasks)

    solutions = set(solutions) | set(additional_sols)
    tasks = set(tasks) | set(additional_tasks)

    return tasks, solutions


def copy_massive(request):
    if not sol_folder_check(request.user, request.POST.get('target_folder')):
        return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции копирования задач')

    list_values = json.loads(request.POST.get('list_values'))
    target_folder = Solution_Folder.objects.get(id = request.POST.get('target_folder'))
    print(list_values)
    tasks, solutions = get_tasks_and_sols_from_values_list(list_values)

    for solution in solutions:
        copy_solution(solution, target_folder)

    return HttpResponse('{}')


def move_massive(request):
    if not sol_folder_check(request.user, request.POST.get('current_folder')):
        return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции перемещения задач')

    list_values = json.loads(request.POST.get('list_values'))
    target_folder = Solution_Folder.objects.get(id = request.POST.get('target_folder'))
    current_folder = Solution_Folder.objects.get(id = request.POST.get('current_folder'))
    tasks, solutions = get_tasks_and_sols_from_values_list(list_values)

    for solution in solutions:
        move_solution(solution, current_folder, target_folder)

    return HttpResponse('{}')


def erase_massive(request):
    if not sol_folder_check(request.user, request.POST.get('current_folder')):
        return HttpResponseForbidden('У Вас недостаточно прав для выполнения операции перемещения задач')

    list_values = json.loads(request.POST.get('list_values'))
    current_folder = Solution_Folder.objects.get(id = request.POST.get('current_folder'))
    tasks, solutions = get_tasks_and_sols_from_values_list(list_values)

    for solution in solutions:
        erase_solution(solution, current_folder)
    return HttpResponse('{}')


def copy_solution(solution, target_folder):

    if type(solution) == int or type(solution) == str:
        solution = Solution.objects.get(id=solution)

    if type(target_folder) == int or type(target_folder) == str:
        target_folder = Solution_Folder.objects.get(id=target_folder)

    target_folder.solution.add(solution)
    add_task_to_tasks_order(target_folder.id, solution.task.id)
    return HttpResponse('{}')


def move_solution(solution, old_folder, new_folder):

    if type(solution) == int or type(solution) == str:
        solution = Solution.objects.get(id=solution)

    if type(new_folder) == int or type(new_folder) == str:
        new_folder = Solution_Folder.objects.get(id=new_folder)

    if type(old_folder) == int or type(old_folder) == str:
        old_folder = Solution_Folder.objects.get(id=old_folder)

    new_folder.solution.add(solution)
    new_folder.save()
    add_task_to_tasks_order(new_folder.id, solution.task.id)
    old_folder.solution.remove(solution)
    old_folder.save()
    remove_task_from_to_tasks_order(old_folder.id, solution.task.id)
    return HttpResponse('{}')


def erase_solution(solution, current_folder):

    if type(solution) == int or type(solution) == str:
        solution = Solution.objects.get(id=solution)

    if type(current_folder) == int or type(current_folder) == str:
        current_folder = Solution_Folder.objects.get(id=current_folder)

    current_folder.solution.remove(solution)
    current_folder.save()
    remove_task_from_to_tasks_order(current_folder.id, solution.task.id)
    return HttpResponse('{}')

