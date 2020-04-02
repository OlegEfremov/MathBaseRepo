$(function () {
        $('#user_solution_catalog').jstree({
            'plugins': ['types', 'state', 'contextmenu'],
            'core': {
                'data': {
                    "url": "get_user_tree",
                    "dataType": "json"
                },
                'dblclick_toggle': false,
                'multiple': false,
                'expand_selected_onload': true,
                'check_callback': true,
                'themes':{'dots': false},
            },
            "contextmenu": {
                "items": {
                    "rename": {
                        "separator_before": false,
                        "separator_after": false,
                        "_disabled": function (data) {
                        	let inst = $.jstree.reference(data.reference),
                            node = inst.get_node(data.reference);

                            if (node['a_attr']['system_name']==='ROOT_CATALOG'){return true}

								return false
						},
                        "label": "Rename",
                        "action": function (data) {
                            let inst = $.jstree.reference(data.reference),
                                obj = inst.get_node(data.reference);
                            inst.edit(obj);
                        }
                    }
                }
            },
            "types": {
                "#": {"valid_children": []},
                "Folder": {
                    "icon": PATH_JSTREE_PIC + "folder.png",
                    "valid_children": ['Folder']
                }
            }
        }).bind('select_node.jstree', function (e, data) {
            action_data['target_folder'] = data['node']['a_attr']['dbID'];
            enable_disable_start_action_button_in_modal()
        }).bind('refresh.jstree', function (e, data) {
  	        select_created_node_in_modal(node_to_select_dbID_in_modal)
  	    }).bind('rename_node.jstree', function (e, data) {
  	        rename_solution_folder_in_modal(e,data)
  	    })
    });

function rename_solution_folder_in_modal(e,data){
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
            // $('#system_solution_catalog').jstree(true).refresh();
        },
        error: function(ts) {
        }
    })
}

function create_solution_folder_in_modal(){
    let send_data = {
        'new_name': 'Новая папка',
        'current_folder': action_data['target_folder']
    };

    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'create_solution_folder',
        data: {'data': send_data},
        dataType: 'json',
        success: function(data){
            node_to_select_dbID_in_modal = data['dbID'];
            // $('#system_solution_catalog').jstree(true).refresh();
            $('#user_solution_catalog').jstree(true).refresh();
        },
        error : function(error) {console.log(error)}
    });
}

//select new node after creation node
//connected to refresh_tree_event
function select_created_node_in_modal(dbID){
	let v = $('#user_solution_catalog').jstree(true).get_json('#', {flat: true})
	if (node_to_select_dbID_in_modal !== "ROOT") {
        let v = $('#user_solution_catalog').jstree(true).get_json('#', {flat: true}),
            id = find_node_by_dbID(v, dbID);
        $('#user_solution_catalog').jstree('activate_node', id);
    }
}




