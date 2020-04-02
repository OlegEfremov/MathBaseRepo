def makeChapterTree_node(node):
    a={}
    a["text"] = node.name
    a["data"] = node.name
    a["type"] = "Chapter"
    a["state"] = {"opened": False, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "Chapter", "dbID": str(node.id)}
    a["children"] = []
    for subchapter in node.subchapters.all():
        b = {}
        b["text"] = subchapter.name
        b["data"] = subchapter.name
        b["type"] = "Chapter"
        b["state"] = {"opened": False, "disabled": False, "selected": False}
        b["a_attr"] = {"dbType": "Chapter", "dbID": str(subchapter.id)}
        b["children"] = []
        if len(subchapter.subchapters.all()) > 0 or len(subchapter.tasknumbers.all()) > 0:
            b["children"] = True
        a["children"].append(b)
    if True:
        for tnleaf in node.tasknumbers.all().order_by('order'):
            b = {}
            b["text"] = tnleaf.body
            b["data"] = tnleaf.body
            b["type"] = "TaskNumber"
            b["state"] = {"opened": False, "disabled": False, "selected": False}
            b["a_attr"] = {"dbType": "TaskNumber", "dbID": str(tnleaf.id)}
            b["children"] = []
            a["children"].append(b)
    return a["children"]



def makeSourceFolderTree_node(node):
    a={}
    a["text"] = node.name
    a["data"] = node.name
    a["type"] = "Folder"
    a["state"] = {"opened": False, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "Source_Folder", "dbID": str(node.id)}
    a["children"] = []
    for subfolder in node.subfolders.all():
        b = {}
        b["text"] = subfolder.name
        b["data"] = subfolder.name
        b["type"] = "Folder"
        b["state"] = {"opened": False, "disabled": False, "selected": False}
        b["a_attr"] = {"dbType": "Source_Folder", "dbID": str(subfolder.id)}
        b["children"] = []
        if len(subfolder.subfolders.all()) > 0 or len(subfolder.sources.all()) > 0:
            b["children"] = True
        a["children"].append(b)
    for leaf in node.sources.all().order_by('name'):
        b = {}
        b["text"] = leaf.name
        b["data"] = leaf.name
        b["type"] = "Source"
        b["state"] = {"opened": False, "disabled": False, "selected": False}
        b["a_attr"] = {"dbType" : "Source", "dbID" : str(leaf.id)}
        b["children"] = []
        if len(leaf.chapters.all()) > 0 or len(leaf.tasknumbers.all()) > 0:
            b["children"] = True
        a["children"].append(b)
    print(a['children'])
    return a['children']


def makeSourceTree_node(node):
    print(node)
    a={}
    a["text"] = node.name
    a["data"] = node.name
    a["type"] = "Source"
    a["state"] = {"opened": False, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "Source", "dbID": str(node.id)}
    a["children"] = []
    for chapter in node.chapters.all().order_by('name'):
        if chapter.parent is None:
            b = {}
            b["text"] = chapter.name
            b["data"] = chapter.name
            b["type"] = "Chapter"
            b["state"] = {"opened": False, "disabled": False, "selected": False}
            b["a_attr"] = {"dbType" : "Chapter", "dbID" : str(chapter.id)}
            b["children"] = []
            if len(chapter.subchapters.all()) > 0 or len(chapter.tasknumbers.all()) > 0:
                b["children"] = True
            a['children'].append(b)

    for tnleaf in node.tasknumbers.all().order_by('order'):
        if tnleaf.chapter is None:
            c = {}
            c["text"] = tnleaf.body
            c["data"] = tnleaf.body
            c["type"] = "TaskNumber"
            c["state"] = {"opened": False, "disabled": False, "selected": False}
            c["a_attr"] = {"dbType": "TaskNumber", "dbID": str(tnleaf.id)}
            c["children"] = []
            a["children"].append(c)
    print(a['children'])

    return a['children']