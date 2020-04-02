

def makeTaskSourceTree(node):
    a={}
    a["text"] = "Источники задачи"
    a["data"] = node.id
    a["type"] = "Task"
    a["state"] = {"opened": True, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "Task", "dbID": str(node.id)}
    a["children"] = []
    for leaf in node.taskNumber.all():
        b = {}
        b["text"] = leaf.source.name+', №'+leaf.body
        b["data"] = leaf.body
        b["type"] = "TaskNumber"
        b["state"] = {"opened": False, "disabled": False, "selected": False}
        b["a_attr"] = {"dbType" : "taskNumber", "dbID" : str(leaf.id)}
        b["children"] = []
        a["children"].append(b)
    return a


def makeChapterTree(node):
    a={}
    a["text"] = node.name
    a["data"] = node.name
    a["type"] = "Chapter"
    a["state"] = {"opened": False, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "Chapter", "dbID": str(node.id)}
    a["children"] = []
    if len(node.subchapters.all()) > 0 or len(node.tasknumbers.all()) > 0:
        a["children"] = True
    # for subchapter in node.subchapters.all():
    #     a["children"].append(makeChapterTree(subchapter))
    # if False:
    #     for tnleaf in node.tasknumbers.all().order_by('order'):
    #         b = {}
    #         b["text"] = tnleaf.body
    #         b["data"] = tnleaf.body
    #         b["type"] = "TaskNumber"
    #         b["state"] = {"opened": False, "disabled": False, "selected": False}
    #         b["a_attr"] = {"dbType": "TaskNumber", "dbID": str(tnleaf.id)}
    #         b["children"] = []
    #         a["children"].append(b)
    return a



def makeSourceTree(node):
    a={}
    a["text"] = node.name
    a["data"] = node.name
    a["type"] = "Folder"
    a["state"] = {"opened": False, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "Source_Folder", "dbID": str(node.id)}
    a["children"] = True
    # if len(node.subfolders.all()) > 0 or len(node.sources.all()) >0:
    #     a["children"] = True
    # for subfolder in node.subfolders.all():
    #    a["children"].append(makeSourceTree(subfolder))
    # for leaf in node.sources.all().order_by('name'):
    #     b = {}
    #     b["text"] = leaf.name
    #     b["data"] = leaf.name
    #     b["type"] = "Source"
    #     b["state"] = {"opened": False, "disabled": False, "selected": False}
    #     b["a_attr"] = {"dbType" : "Source", "dbID" : str(leaf.id)}
    #     b["children"] = []
    #     for chapter_leaf in leaf.chapters.all():
    #         if chapter_leaf.parent is None:
    #             b["children"].append(makeChapterTree(chapter_leaf))
    #         pass
    #     if False:
    #         for tnleaf in leaf.tasknumbers.all().order_by('order'):
    #             if tnleaf.chapter is None:
    #                 c = {}
    #                 c["text"] = tnleaf.body
    #                 c["data"] = tnleaf.body
    #                 c["type"] = "TaskNumber"
    #                 c["state"] = {"opened": False, "disabled": False, "selected": False}
    #                 c["a_attr"] = {"dbType": "TaskNumber", "dbID": str(tnleaf.id)}
    #                 c["children"] = []
    #                 b["children"].append(c)
    #     a["children"].append(b)
    return [a]