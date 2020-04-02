import json

from apps.Main.constants import NODE_MATH_TYPE, NODE_MATH_TYPE_EXCLUDE
from apps.Main.models import SavedFilter


def make_attr_tree(node):
    a = dict()
    a["text"] = node.name
    a["data"] = node.name
    a["type"] = "AND"
    a["state"] = {"opened": False, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "MathAttribute_Folder", "dbID": str(node.id), "system_name": node.system_name}
    a["children"] = []

    for subfolder in node.subfolders.all():
        a["children"].append(make_attr_tree(subfolder))

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


# Рекурсивная функция, которая находит в базе решения, которые соответствуют запросу node
def filterQuery(node,q):
    p = set()
    t=q

    if (node['type'] == 'AND'):
        for c in node['children']:
            t = set(t) & set(filterQuery(c,q))
        return set(t)
    elif (node['type'] == 'OR'):
        for c in node['children']:
            p = set(p) | set(filterQuery(c,q))
        return set(p)
    elif (node['type'] == 'NOT-AND'):
        for c in node['children']:
            t = set(t) & set(filterQuery(c,q))
        return set(q) - set(t)
    elif (node['type'] == 'NOT-OR'):
        for c in node['children']:
           p = set(p) | set(filterQuery(c,q))
        return set(q)- set(p)

    elif (node['type'] == 'SavedFilter'):
        dbID = node['a_attr']['dbID']
        savedfilter = SavedFilter.objects.get(id=dbID)
        fulljson = json.loads(savedfilter.body)[0]
        fulljson = clean_tree(fulljson)
        p = filterQuery(fulljson, q)
        return set(p)

    elif (node['type'] == 'EXCLUDE_SavedFilter'):
        dbID = node['a_attr']['dbID']
        savedfilter = SavedFilter.objects.get(id=dbID)
        fulljson = json.loads(savedfilter.body)[0]
        fulljson = clean_tree(fulljson)
        t = filterQuery(fulljson, q)
        return set(q) - set(t)

    elif (node['type'] in NODE_MATH_TYPE):
        dbID = node['a_attr']['dbID']
        if (node['a_attr']['dbType'] == 'MathAttribute'):
            t = t.filter(mathAttribute__id=dbID)
        elif (node['a_attr']['dbType'] == 'Solution'):
            t = t.filter(id=dbID)
        return t

    elif (node['type'] in NODE_MATH_TYPE_EXCLUDE):
        dbID = node['a_attr']['dbID']
        if (node['a_attr']['dbType'] == 'MathAttribute'):
            t = t.exclude(mathAttribute__id=dbID)
        elif (node['a_attr']['dbType'] == 'Solution'):
            t = t.exclude(id=dbID)
        return t
    else: print(node['type'])

    return False


# Очищает Json дерева от служебных атрибутов jstree
def clean_tree(node, close_all=True):
    if 'li_attr' in node:
        del node['li_attr']
    if 'id' in node:
        del node['id']
    if 'href' in node['a_attr']:
        del node['a_attr']['href']
    if 'id' in node['a_attr']:
        del node['a_attr']['id']
    node['state']['selected'] = False
    if (close_all):
        node['state']['opened'] = False
    if node['children'] != []:
        for element in node['children']:
            clean_tree(element)
    return node

# Get tree for all mathattribute in filtered tasks
def makeMathAttributeTree(mathattribute):
    a=[]
    for attr in mathattribute:
        b = dict()
        b["text"] = attr.name
        b["data"] = attr.name
        b["type"] = 'MathAttr'
        b["state"] = {"opened": False, "disabled": False, "selected": False}
        b["a_attr"] = {"dbType": "MathAttribute", "dbID": str(attr.id)}
        b["children"] = []
        a.append(b)
    return a