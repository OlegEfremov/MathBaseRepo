import json

from apps.Main.models import MathAttribute_Folder
from apps.Main.models import MathAttribute


def move_folder(node):
    folder = MathAttribute_Folder.objects.get(id=node['dbID'])
    new_parent = MathAttribute_Folder.objects.get(id=node['new_parent_dbID'])
    folder.parent = new_parent
    folder.save()
    return True

def rename_folder(node):
    folder = MathAttribute_Folder.objects.get(id=node['dbID'])
    folder.name = node['new_name']
    folder.save()
    return True

def delete_folder(node):
    folder = MathAttribute_Folder.objects.get(id=node['dbID'])
    folder.delete()
    return True

def create_folder(node):
    if node['parent_dbID'] != 'NONE':
        parent_folder = MathAttribute_Folder.objects.get(id = node['parent_dbID'])
        new_folder = MathAttribute_Folder(name = node['new_name'], system_name = 'from_edit_mathattr_tree', parent = parent_folder)
    else:
        root_folder = MathAttribute_Folder.objects.get(system_name = 'ROOT_MATHATTRIBUTES')
        new_folder = MathAttribute_Folder(name=node['new_name'], system_name='from_edit_mathattr_tree', parent = root_folder)
    new_folder.save()
    return '{"dbID":"' + str(new_folder.id) + '"}'


def copy_mathattr(node):
    math_attr = MathAttribute.objects.get(id=node['dbID'])
    new_parent = MathAttribute_Folder.objects.get(id=node['new_parent_dbID'])
    math_attr.folders.add(new_parent)
    math_attr.save()
    return True

def move_mathattr(node):
    mathattr = MathAttribute.objects.get(id=node['dbID'])
    new_parent = MathAttribute_Folder.objects.get(id=node['new_parent_dbID'])
    old_parent = MathAttribute_Folder.objects.get(id=node['old_parent_dbID'])

    if old_parent.system_name != 'ALL_MATHATTRIBUTES':
        mathattr.folders.remove(old_parent)

    mathattr.folders.add(new_parent)
    mathattr.save()

    return True

def rename_mathattr(node):
    mathattr = MathAttribute.objects.get(id=node['dbID'])
    mathattr.name = node['new_name']
    mathattr.save()
    return True

def delete_mathattr(node):
    mathattr = MathAttribute.objects.get(id=node['dbID'])
    mathattr.delete()
    return True


def soft_delete_mathattr(node):
    mathattr = MathAttribute.objects.get(id=node['dbID'])
    parent_folder_dbID = node['new_parent_dbID']
    parent_folder = MathAttribute_Folder.objects.get(id = parent_folder_dbID)
    mathattr.folders.remove(parent_folder)
    return True

def create_mathattr(node):
    all_mathattr_folder = MathAttribute_Folder.objects.get(system_name = 'ALL_MATHATTRIBUTES')
    new_mathattribute = MathAttribute(name=node['new_name'])
    new_mathattribute.save()
    if node['parent_dbID'] != "NONE":
        parent_folder = MathAttribute_Folder.objects.get(id=node['parent_dbID'])
        new_mathattribute.folders.add(parent_folder)
    else:
        parent_folder = MathAttribute_Folder.objects.get(system_name = 'ROOT_MATHATTRIBUTES')
        new_mathattribute.folders.add(parent_folder)
    new_mathattribute.folders.add(all_mathattr_folder)

    return '{"dbID":"'+str(new_mathattribute.id) + '"}'