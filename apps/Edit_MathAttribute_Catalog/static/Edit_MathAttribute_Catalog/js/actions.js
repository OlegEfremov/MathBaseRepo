function get_old_parent_dbID(data){
    let ref = $('#mathattr_tree').jstree(true);

    let old_parent_jstree_id = data['old_parent'],
		old_parent = ref.get_node(old_parent_jstree_id),
        old_parent_dbID = old_parent['a_attr']['dbID'];

    return old_parent_dbID
}

function get_new_parent_dbID(data){
    let ref = $('#mathattr_tree').jstree(true);

    let new_parent_jstree_id = data['parent'],
        new_parent = ref.get_node(new_parent_jstree_id),
        new_parent_dbID = new_parent['a_attr']['dbID'];

    return new_parent_dbID
}

function get_parent_dbID(data){
    let ref = $('#mathattr_tree').jstree(true);

    let parent_jstree_id = data['node']['parent'],
        parent = ref.get_node(parent_jstree_id),
        parent_dbID = parent['a_attr']['dbID'];

    return parent_dbID
}


function rename_node(data){
    let send_data = {
        'dbID' : data['node']['a_attr']['dbID'],
        'dbType' : data['node']['a_attr']['dbType'],
        'new_name' : data['node']['text']
        };

    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'rename_node',
        data: {'data': send_data},
        dataType: 'json',
        success: function(data){
            $('#mathattr_tree').jstree(true).refresh();
        },
        error : function(error) {console.log(error)}
    });
}


function copy_node(data){
    let send_data = {
        'old_parent_dbID': get_old_parent_dbID(data),
		'new_parent_dbID': get_new_parent_dbID(data),
        'dbID' : data['node']['a_attr']['dbID'],
        'dbType' : data['node']['a_attr']['dbType'],
        };

    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'copy_node',
        data: {'data': send_data},
        dataType: 'json',
        success: function(data){},
        error : function(error) {console.log(error)}
    });
}


function move_node(data){
    let send_data = {
        'old_parent_dbID': get_old_parent_dbID(data),
		'new_parent_dbID': get_new_parent_dbID(data),
        'dbID' : data['node']['a_attr']['dbID'],
        'dbType' : data['node']['a_attr']['dbType'],
        };

    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'move_node',
        data: {'data': send_data},
        dataType: 'json',
        success: function(data){},
        error : function(error) {console.log(error)}
    });
}


function delete_node_from_db(data){
    let send_data = {
        'dbID' : data['a_attr']['dbID'],
        'dbType' : data['a_attr']['dbType'],
    };

    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'delete_node_from_db',
        data: {'data': send_data},
        dataType: 'json',
        success: function(data){
            $('#mathattr_tree').jstree(true).refresh();
            node_to_select_dbID = 'NONE'
        },
        error : function(error) {console.log(error)}
    });
}


function remove_node_from_folder(data){
    let send_data = {
        'parent_dbID': get_parent_dbID(data),
        'dbID' : data['node']['a_attr']['dbID'],
        'dbType' : data['node']['a_attr']['dbType'],
        };

    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'remove_node_from_folder',
        data: {'data': send_data},
        dataType: 'json',
        success: function(data){},
        error : function(error) {console.log(error)}
    });
}



function create_node(){
    let new_name = document.getElementById("input_new_element_name").value,
        parent_dbID = document.getElementById('parent_folder').value,
        dbType = document.getElementById("input_dbType").value,
        mathype = 'None';

    if (mathtypes.indexOf(dbType) !== -1){
        mathype = dbType;
        dbType = 'MathAttribute'
    }

    let send_data = {
        'new_name': new_name,
        'dbType': dbType,
        'mathtype': mathype,
        'parent_dbID': parent_dbID
    };

    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'create_node',
        data: {'data': send_data},
        dataType: 'json',
        success: function(data){
            $('#mathattr_tree').jstree(true).refresh();
            node_to_select_dbID = data['dbID']
        },
        error : function(error) {console.log(error)}
    });
    document.getElementById("input_new_element_name").value = "";
}



