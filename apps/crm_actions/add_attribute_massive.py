import json

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from apps.Main.decorators import editor_check
from apps.Main.models import MathAttribute
from apps.crm_actions.views import get_tasks_and_sols_from_values_list


def get_mathattr_from_tree(tree):
    mathattr_dbIDs = []
    children = tree[0]['children']
    for p in children:
        mathattr_dbIDs.append(p['a_attr']['dbID'])
    mathattributes = MathAttribute.objects.filter(id__in=mathattr_dbIDs)

    return mathattributes


@user_passes_test(editor_check)
def add_attributes_to_solution(solution, mathattributes):

    solution.mathAttribute.add(*list(mathattributes))
    solution.save()


@user_passes_test(editor_check)
def add_attribute_massive(request):
    mathattr_tree_data = json.loads(request.POST.get('attributes_to_add'))
    mathattributes = get_mathattr_from_tree(mathattr_tree_data)

    list_values = json.loads(request.POST.get('list_values'))
    tasks, solutions = get_tasks_and_sols_from_values_list(list_values)

    for solution in solutions:
        add_attributes_to_solution(solution, mathattributes)

    return HttpResponse('{}')