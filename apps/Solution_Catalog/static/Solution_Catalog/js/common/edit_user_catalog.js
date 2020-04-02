//function bind to view_task jstree events

function rename_solution_folder(e,data){
    let send_data = {
        'dbID' : data['node']['a_attr']['dbID'],
        'new_name': data['text']
    };
    send_data = JSON.stringify(send_data);

    $.ajax({
        url: "rename_solution_folder",
        type: "POST",
        data: {'data': send_data},
        success: function(res) {
            $('#user_solution_catalog').jstree(true).refresh();
        },
        error: function(ts) {
        }
    })
}

function copy_solution_folder(e,data){
	let ref = $('#system_solution_catalog').jstree(true),
		new_parent_jstree_id = data['parent'],
		new_parent = ref.get_node(new_parent_jstree_id),
		new_parent_dbID = new_parent['a_attr']['dbID'],
		dbID = data['node']['a_attr']['dbID'];

	let send_data = {
		'new_parent_dbID': new_parent_dbID,
		'dbID': dbID,
	};
	send_data = JSON.stringify(send_data);
	$.ajax({
		type: 'POST',
		url: 'copy_solution_folder',
		data: {'data': send_data},
		dataType: 'json',
		success: function(data){
		    $('#system_solution_catalog').jstree(true).refresh();
		    $('#user_solution_catalog').jstree(true).refresh();
            node_to_select_dbID = data['dbID']
        },
		error : function(error) {console.log(error)}
	});
}

function move_solution_folder(e,data){
	let ref = $('#system_solution_catalog').jstree(true),
		new_parent_jstree_id = data['parent'],
		new_parent = ref.get_node(new_parent_jstree_id),
		new_parent_dbID = new_parent['a_attr']['dbID'],
		dbID = data['node']['a_attr']['dbID'];

	let send_data = {
		'new_parent_dbID': new_parent_dbID,
		'dbID': dbID,
	};

	send_data = JSON.stringify(send_data);
	$.ajax({
		type: 'POST',
		url: 'move_solution_folder',
		data: {'data': send_data},
		dataType: 'json',
		success: function(data){
		    $('#system_solution_catalog').jstree(true).refresh();
		    $('#user_solution_catalog').jstree(true).refresh();
        },
		error : function(error) {console.log(error)}
	});
}

function delete_solution_folder(e,data){
			let send_data = {
                'dbID': data['node']['a_attr']['dbID'],
            };
			send_data = JSON.stringify(send_data);
			$.ajax({
				type: 'POST',
				url: 'delete_solution_folder',
				data: {'data': send_data},
				dataType: 'json',
				success: function(data){
				    $('#user_solution_catalog').jstree(true).refresh();
                },
				error : function(error) {console.log(error)}
			});
}

function create_solution_folder(){
    let send_data = {
        'new_name': 'Новая папка',
        'current_folder': action_data['view_folder']
    };

    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'create_solution_folder',
        data: {'data': send_data},
        dataType: 'json',
        success: function(data){
            node_to_select_dbID = data['dbID'];
            $('#system_solution_catalog').jstree(true).refresh();
            $('#user_solution_catalog').jstree(true).refresh();
        },
        error : function(error) {console.log(error)}
    });
}

//find node in the tree by dbID
// tree_instance must be from
// var v = $('#mathattr_tree').jstree(true).get_json('#', {flat: true}),
//it is needed in select_created_node function - when new node is created
function find_node_by_dbID(tree_instance, dbID) {
    for (i in tree_instance) {
        let node = tree_instance[i];
        if (node['a_attr']['dbID'] === dbID) {
            return node['id']
        }
    }
    return '#'
}

//select new node after creation node
//connected to refresh_tree_event
function select_created_node(dbID){
	let v = $('#system_solution_catalog').jstree(true).get_json('#', {flat: true})
	if (node_to_select_dbID !== "ROOT") {
        let v = $('#system_solution_catalog').jstree(true).get_json('#', {flat: true}),
            id = find_node_by_dbID(v, dbID);
        $('#system_solution_catalog').jstree('activate_node', id);
    }
}
