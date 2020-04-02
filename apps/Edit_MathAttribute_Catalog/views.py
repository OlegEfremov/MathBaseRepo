from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
import json


from apps.Edit_MathAttribute_Catalog.sub_views.edit_math_attribute_tree import move_folder, rename_folder, copy_mathattr, \
    move_mathattr, rename_mathattr, delete_folder, delete_mathattr, create_mathattr, create_folder, soft_delete_mathattr
from apps.Main.constants import path
from apps.Main.decorators import admin_check
from apps.Main.lib import get_current_user
from apps.Main.models import MathAttribute_Folder, MathAttribute


@user_passes_test(admin_check)
def main_page(request):
    return render(request, 'Edit_MathAttribute_Catalog/main_page.html', {'path': path})


def edit_mathattr_tree(request):
    allmathattributes = makeAttributeTree(MathAttribute_Folder.objects.get(system_name='ROOT_MATHATTRIBUTES'))

    tree = [allmathattributes]
    tree_json = json.dumps(tree, ensure_ascii=False)

    return HttpResponse(tree_json, content_type='json')


def makeAttributeTree(node):
    a = dict()
    a["text"] = node.name
    a["data"] = node.name
    a["type"] = "AND"
    a["state"] = {"opened": False, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "MathAttribute_Folder", "dbID": str(node.id), "system_name": node.system_name}
    a["children"] = []
    for subfolder in node.subfolders.all():
        a["children"].append(makeAttributeTree(subfolder))
    for leaf in node.mathattributes.all():
        b = dict()
        b["text"] = leaf.name
        b["data"] = leaf.name
        b["type"] = 'MathAttr'
        b["state"] = {"opened": False, "disabled": False, "selected": False}
        b["a_attr"] = {"dbType": "MathAttribute", "dbID": str(leaf.id)}
        b["children"] = []
        a["children"].append(b)

    return a


def rename_node(request):
    data = json.loads(request.POST['data'])
    if data['dbType'] == 'MathAttribute_Folder':
        folder = MathAttribute_Folder.objects.get(id=data['dbID'])
        folder.name = data['new_name']
        folder.save()

    if data['dbType'] == 'MathAttribute':
        mathattr = MathAttribute.objects.get(id=data['dbID'])
        mathattr.name = data['new_name']
        mathattr.save()

    return HttpResponse('{}')


def copy_node(request):
    data = json.loads(request.POST['data'])

    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    if data['dbType'] == 'MathAttribute_Folder':
        new_folder = recurs_for_copy_folder(data['new_parent_dbID'], data['dbID'], current_user)

        return HttpResponse('{"dbID":"' + str(new_folder.id) + '"}')

    if data['dbType'] == 'MathAttribute':
        math_attr = MathAttribute.objects.get(id=data['dbID'])
        new_parent = MathAttribute_Folder.objects.get(id=data['new_parent_dbID'])
        math_attr.folders.add(new_parent)
        math_attr.save()

    return HttpResponse('{}')


def recurs_for_copy_folder(new_parent_dbID, dbID, current_user):

    new_parent = MathAttribute_Folder.objects.get(id=new_parent_dbID)
    folder = MathAttribute_Folder.objects.get(id=dbID)

    new_folder = MathAttribute_Folder(name=folder.name, parent=new_parent, author=current_user)
    new_folder.save()
    new_folder.mathattributes.add(*list(folder.mathattributes.all()))
    new_folder.save()

    for child in folder.subfolders.all():
        recurs_for_copy_folder(new_folder.id, child.id,current_user)

    return new_folder


def move_node(request):
    data = json.loads(request.POST['data'])
    if data['dbType'] == 'MathAttribute_Folder':
        folder = MathAttribute_Folder.objects.get(id=data['dbID'])
        new_parent = MathAttribute_Folder.objects.get(id=data['new_parent_dbID'])
        folder.parent = new_parent
        folder.save()

    if data['dbType'] == 'MathAttribute':

        mathattr = MathAttribute.objects.get(id=data['dbID'])
        new_parent = MathAttribute_Folder.objects.get(id=data['new_parent_dbID'])
        old_parent = MathAttribute_Folder.objects.get(id=data['old_parent_dbID'])

        if old_parent.system_name != 'ALL_MATHATTRIBUTES':
            mathattr.folders.remove(old_parent)

        mathattr.folders.add(new_parent)
        mathattr.save()

    return HttpResponse('{}')


def create_node(request):
    data = json.loads(request.POST['data'])

    user_id = request.user.id
    current_user = User.objects.get(id=user_id)

    if data['dbType'] == 'MathAttribute_Folder':
        if data['parent_dbID'] != 'NONE':
            parent_folder = MathAttribute_Folder.objects.get(id=data['parent_dbID'])
            new_folder = MathAttribute_Folder(name=data['new_name'], system_name='from_edit_mathattr_tree',
                                              parent=parent_folder, author=current_user)
        else:
            root_folder = MathAttribute_Folder.objects.get(system_name='ROOT_MATHATTRIBUTES')
            new_folder = MathAttribute_Folder(name=data['new_name'], system_name='from_edit_mathattr_tree',
                                              parent=root_folder, author=current_user)
        new_folder.save()
        return HttpResponse('{"dbID":"' + str(new_folder.id) + '"}')

    if data['dbType'] == 'MathAttribute':
        all_mathattr_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
        new_mathattribute = MathAttribute(name=data['new_name'], author=current_user)
        new_mathattribute.save()
        if data['parent_dbID'] != "NONE":
            parent_folder = MathAttribute_Folder.objects.get(id=data['parent_dbID'])
            new_mathattribute.folders.add(parent_folder)
        else:
            parent_folder = MathAttribute_Folder.objects.get(system_name='ROOT_MATHATTRIBUTES')
            new_mathattribute.folders.add(parent_folder)
        new_mathattribute.folders.add(all_mathattr_folder)

        return HttpResponse('{"dbID":"' + str(new_mathattribute.id) + '"}')

    return HttpResponse('{}')

def delete_node_from_db(request):
    data = json.loads(request.POST['data'])
    if data['dbType'] == 'MathAttribute':
        mathattr = MathAttribute.objects.get(id=data['dbID'])
        mathattr.delete()

    if data['dbType'] == 'MathAttribute_Folder':
        folder = MathAttribute_Folder.objects.get(id=data['dbID'])
        folder.delete()
    return HttpResponse('{}')


# Delete mathattribute from folder, but not from database
def remove_node_from_folder(request):
    data = json.loads(request.POST['data'])
    if data['dbType'] == 'MathAttribute':
        mathattr = MathAttribute.objects.get(id=data['dbID'])
        parent_folder_dbID = data['parent_dbID']
        parent_folder = MathAttribute_Folder.objects.get(id = parent_folder_dbID)
        mathattr.folders.remove(parent_folder)

    return HttpResponse('{}')


def create_mathattr_folder(request):
    parent_dbID = request.POST.get('parent_dbID')
    if parent_dbID != 'NONE':
        parent_folder = MathAttribute_Folder.objects.get(id = int(parent_dbID))
        new_folder = MathAttribute_Folder(name = 'Новая папка', system_name = 'from_edit_mathattr_tree', parent = parent_folder, author = get_current_user(request))
    else:
        root_folder = MathAttribute_Folder.objects.get(system_name = 'ROOT_MATHATTRIBUTES')
        new_folder = MathAttribute_Folder(name='Новая папка', system_name='from_edit_mathattr_tree', parent = root_folder, author = get_current_user(request))
    new_folder.save()
    return HttpResponse('{"dbID":"' + str(new_folder.id) + '"}')


def create_mathattr(request):
    parent_dbID = request.POST.get('parent_dbID')
    all_mathattr_folder = MathAttribute_Folder.objects.get(system_name='ALL_MATHATTRIBUTES')
    new_mathattribute = MathAttribute(name='Новый атрибут', author=get_current_user(request))
    new_mathattribute.save()
    if parent_dbID != "NONE":
        parent_folder = MathAttribute_Folder.objects.get(id=parent_dbID)
        new_mathattribute.folders.add(parent_folder)
    else:
        parent_folder = MathAttribute_Folder.objects.get(system_name='ROOT_MATHATTRIBUTES')
        new_mathattribute.folders.add(parent_folder)
    new_mathattribute.folders.add(all_mathattr_folder)
    return HttpResponse('{"dbID":"' + str(new_mathattribute.id) + '"}')
