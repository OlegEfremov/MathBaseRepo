import json
from django.http import HttpResponse

from apps.Main.models import Solution_Folder, Solution, Task, MathAttribute

def add_task_to_tasks_order(sol_folder_dbID, task_number):
    sol_folder = Solution_Folder.objects.get(id= sol_folder_dbID)
    tasks_order = json.loads(sol_folder.tasks_order)
    if not task_number in tasks_order:
        tasks_order[task_number] = '1000000'

        for key in tasks_order:
            tasks_order[key] = int(tasks_order[key])
        a = sorted(tasks_order.items(), key=lambda x: x[1])

        i = 0
        for p in a:
            i = i + 1
            tasks_order[p[0]] = i

        sol_folder.tasks_order = json.dumps(tasks_order)
        sol_folder.save()
        return True
    return False


# def reorder_tasks(request):
#     data = json.loads(request.POST['data'])
#     solution_folder_dbID = data['solution_folder_dbID']
#     order_numbers = data['order_numbers']
#
#     sol_folder = Solution_Folder.objects.get(id=solution_folder_dbID)
#     tasks_order = json.loads(sol_folder.tasks_order)
#
#     for task_number in order_numbers:
#         tasks_order[task_number] = order_numbers[task_number]
#
#     for key in tasks_order:
#         tasks_order[key] = int(tasks_order[key])
#     a = sorted(tasks_order.items(), key=lambda x: x[1])
#
#     i = 0
#     for p in a:
#         i = i + 1
#         tasks_order[p[0]] = i
#
#     sol_folder.tasks_order = json.dumps(tasks_order)
#     sol_folder.save()
#
#     return HttpResponse('{}')

def remove_task_from_to_tasks_order(sol_folder_dbID, task_number):
    sol_folder = Solution_Folder.objects.get(id=sol_folder_dbID)
    tasks_order = json.loads(sol_folder.tasks_order)
    if str(task_number) in tasks_order:
        tasks_order.pop(str(task_number))
        sol_folder.tasks_order = json.dumps(tasks_order)
        sol_folder.save()
        return True
    return False


def task_copy(data):
    target_folder = Solution_Folder.objects.get(id=data['target_folder'])

    task_to_add = Task.objects.get(id=data['element_id'])
    solutions = Solution.objects.filter(task=task_to_add)

    target_folder.solution.add(*list(solutions))
    add_task_to_tasks_order(target_folder.id, task_to_add.id)

    return HttpResponse('{}')


def task_move(data):
    old_folder = Solution_Folder.objects.get(id=data['view_folder'])
    new_folder = Solution_Folder.objects.get(id=data['target_folder'])

    task_to_add = Task.objects.get(id=data['element_id'])
    solutions = Solution.objects.filter(task=task_to_add)

    new_folder.solution.add(*list(solutions))
    new_folder.save()

    add_task_to_tasks_order(new_folder.id, task_to_add.id)

    old_folder.solution.remove(*list(solutions))
    old_folder.save()

    remove_task_from_to_tasks_order(old_folder.id, task_to_add.id)
    return HttpResponse('{}')


def task_remove(data):
    view_folder = Solution_Folder.objects.get(id=data['view_folder'])

    task_to_remove = Task.objects.get(id=data['element_id'])
    solutions = Solution.objects.filter(task=task_to_remove)

    view_folder.solution.remove(*list(solutions))
    view_folder.save()

    remove_task_from_to_tasks_order(view_folder.id, task_to_remove.id)
    return HttpResponse('{}')


def solution_copy(data):
    target_folder = Solution_Folder.objects.get(id=data['target_folder'])
    solution = Solution.objects.get(id=data['element_id'])

    target_folder.solution.add(solution)

    add_task_to_tasks_order(target_folder.id, solution.task.id)

    return HttpResponse('{}')


def solution_move(data):
    old_folder = Solution_Folder.objects.get(id=data['view_folder'])
    new_folder = Solution_Folder.objects.get(id=data['target_folder'])

    solution = Solution.objects.get(id=data['element_id'])

    new_folder.solution.add(solution)
    new_folder.save()

    add_task_to_tasks_order(new_folder.id, solution.task.id)

    old_folder.solution.remove(solution)
    old_folder.save()

    remove_task_from_to_tasks_order(old_folder.id, solution.task.id)
    return HttpResponse('{}')


def solution_remove(data):
    view_folder = Solution_Folder.objects.get(id=data['view_folder'])

    solution = Solution.objects.get(id=data['element_id'])

    view_folder.solution.remove(solution)
    view_folder.save()

    remove_task_from_to_tasks_order(view_folder.id, solution.task.id)

    return HttpResponse('{}')


def get_mathattr_from_tree(tree):
    mathattr_dbIDs = []
    children = tree['children']
    for p in children:
        mathattr_dbIDs.append(p['a_attr']['dbID'])
    return mathattr_dbIDs


def add_attribute_to_solution(data):

    mathattr_dbIDs = get_mathattr_from_tree(data['attr_to_add'][0])
    mathattributes = MathAttribute.objects.filter(id__in=mathattr_dbIDs)
    sol = Solution.objects.get(id=data['element_id'])
    sol.mathAttribute.add(*list(mathattributes))
    sol.save()


def massive_action(data):
    print(data)
    for p in data['checkbox_values']:
        print(1)
        if data['checkbox_values'][p]:
            print(2)
            if p.count('sol') != 0:
                print(3)
                sol_id = p.split('_')[-1]
                temp_data = {'element_id': sol_id, 'target_folder': data['target_folder'],
                             'view_folder': data['view_folder'], 'attr_to_add': data['attr_to_add']}

                if data['action_type'] == 'massive_copy':
                    solution_copy(temp_data)
                if data['action_type'] == 'massive_move':
                    solution_move(temp_data)
                if data['action_type'] == 'massive_remove':
                    solution_remove(temp_data)
                if data['action_type'] == 'massive_add_attribute_to_solution':
                    print(4)
                    add_attribute_to_solution(temp_data)

    return HttpResponse('{}')


