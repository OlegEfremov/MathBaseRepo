//node_to_select_dbID - which node need to select after refresh tree
let node_to_select_dbID = '',
    parent_dbID = "NONE";

$( document ).ready(function() {
   document.getElementById('parent_folder').value = parent_dbID;
});

//find node in the tree by dbID
// tree_instance must be from
// var v = $('#mathattr_tree').jstree(true).get_json('#', {flat: true}),
//it is needed in select_created_node function - when new node is created
function find_node_by_dbID(tree_instance, dbID) {
    for (i in tree_instance) {
        var node = tree_instance[i];
        if (node['a_attr']['dbID'] === dbID) {
            return node['id']
        }
    }
    return '#'
}

//select new node after creation
function select_created_node(dbID){
    if (node_to_select_dbID !== "NONE") {
        var v = $('#mathattr_tree').jstree(true).get_json('#', {flat: true}),
            id = find_node_by_dbID(v, dbID);
        $('#mathattr_tree').jstree('activate_node', id);
    }
}



//check if there is dbType node with name name in tree
//two node with differents dbTypes and the same names name can be in tree - and the function will return false
function is_name_in_tree(tree, dbType, name){

    for (var i in tree) {
        var node = tree[i];

        if (node['a_attr']['dbType'] === dbType && node['text'].toLowerCase() === name.toLowerCase()) {
            return true
        }
    }
    return false
}

//set current folder to root. needed after deleting node
function reset_current_folder(){
    document.getElementById('parent_folder').innerHTML = 'Корневой каталог';
    parent_dbID = "NONE";
    document.getElementById('parent_folder').value = parent_dbID;
}



