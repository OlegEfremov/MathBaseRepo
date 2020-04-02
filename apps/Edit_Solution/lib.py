
def makeSolAttrTree(node):
    a={}
    a["text"] = "Атрибуты решения"
    a["data"] = node.id
    a["type"] = "Solution"
    a["state"] = {"opened": True, "disabled": False, "selected": False}
    a["a_attr"] = {"dbType": "Solution", "dbID": str(node.id)}
    a["children"] = []
    for leaf in node.mathAttribute.all():
        b = {}
        b["text"] = leaf.name
        b["data"] = leaf.name
        b["type"] = 'MathAttr'
        b["state"] = {"opened": False, "disabled": False, "selected": False}
        b["a_attr"] = {"dbType" : 'MathAttribute', "dbID" : str(leaf.id)}
        b["children"] = []
        a["children"].append(b)
    return a
