from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
from apps.Edit_MathAttribute_Catalog.views import makeAttributeTree
from apps.Edit_Solution.forms import SolutionForm
from apps.Edit_Solution.lib import makeSolAttrTree
from apps.Main.constants import path
from apps.Main.models import Solution, MathAttribute, MathAttribute_Folder


def main_page(request, sol_id):
    sol = Solution.objects.get(id=sol_id)
    solform = SolutionForm(request.POST or None, initial={'body': sol.body, 'name': sol.name})
    solform.is_valid()
    if (solform.is_valid()):
        newbody = solform.cleaned_data.get('body')
        newname = solform.cleaned_data.get('name')
        Solution.objects.filter(pk=sol_id).update(body=newbody, name=newname)

    sol = Solution.objects.get(id=sol_id)
    tasks = [sol.task]

    solutions_set = [sol]


    return render(request, 'Edit_Solution/main_page.html', {'tasks': tasks, 'solutions_set': solutions_set, 'sol': sol, 'solform': solform, 'path': path})


def edit_mathattr_tree(request):
    allmathattributes = makeAttributeTree(MathAttribute_Folder.objects.get(system_name='ROOT_MATHATTRIBUTES'))

    tree = []
    tree.append(allmathattributes)

    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')


def mathattr_tree(request):

    objects = makeAttributeTree(MathAttribute_Folder.objects.get(system_name='ROOT_MATHATTRIBUTES'))


    tree = []
    tree.append(objects)

    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')

def solattr_tree(request, sol_id=0):
    sol = Solution.objects.get(id=sol_id)
    solattrtree = makeSolAttrTree(sol)

    tree=[]
    tree.append(solattrtree)
    treeJson = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(treeJson, content_type='json')


def add_attr_to_sol(request):

    data = request.POST

    node_dbType = data['node_dbType']
    node_dbID = data['node_dbID']
    solid = data['solid']

    sol = Solution.objects.get(id=solid)

    if node_dbType == 'MathAttribute':
        node = MathAttribute.objects.get(id=node_dbID)
        sol.mathAttribute.add(node)

    return HttpResponse('hi')


def delete_mathattribue_from_solution(request):

    data = request.POST

    node_dbType = data['node_dbType']
    node_dbID = data['node_dbID']
    solid = data['solid']

    sol = Solution.objects.get(id=solid)
    if node_dbType == 'MathAttribute':
        node = MathAttribute.objects.get(id=node_dbID)
        sol.mathAttribute.remove(node)

    return HttpResponse('hi')


def delete_solution(request, sol_id):
    sol = Solution.objects.get(id=sol_id)
    sol.delete()
    return HttpResponse('hi')


def show_tasks(request):
    data = json.loads(request.GET['data'])
    sol_id = data['sol_id']

    sol = Solution.objects.get(id=sol_id)
    tasks = [sol.task]
    solutions_set = [sol]

    return render(request, 'Edit_Solution/table_of_tasks.html',
                  {'path': path, 'tasks': tasks, 'solutions_set': solutions_set})


def save_solution(request):
    data = json.loads(request.POST['data'])

    sol = Solution.objects.get(id=data['sol_id'])
    sol.body = data['new_body']
    sol.name = data['new_name']
    sol.save()

    return HttpResponse('{}')
