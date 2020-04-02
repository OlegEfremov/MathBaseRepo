var test_folder_action_data={},
    current_test_id='',
    target_test_folder_id='';



$(function () {
	$('#test_folder_tree').jstree(tree_inner()).bind('select_node.jstree', function (e, data) {
	    select_view_test_folder(e,data);
  	}).bind('rename_node.jstree', function (e, data) {
  	    rename_test_folder(e,data)
  	}).bind('copy_node.jstree', function (e, data) {
  	    let ref = $('#test_folder_tree').jstree(true);
        copy_test_folder(e,data, ref)
  	}).bind('move_node.jstree', function (e, data) {
  	    let ref = $('#test_folder_tree').jstree(true);
  	    move_test_folder(e,data, ref)
  	}).bind('delete_node.jstree', function (e, data) {
        delete_test_folder_from_db(e,data)
  	}).bind('refresh.jstree', function (e, data) {
  	    // select_created_node(node_to_select_dbID)
  	});
});


function copy_test_folder(e,data, ref){
    let new_parent_dbID = get_new_parent_dbID(ref, data),
        node_dbID = data['node']['a_attr']['dbID'];
    $.ajax({
        url: 'test_folder/copy_test_folder',
        type: "POST",
        data: {
            'new_parent_dbID': new_parent_dbID,
            'node_dbID': node_dbID
        },
        success: function(res) {

        },
        error: function(ts) {
            console.log(ts)
        }
    })
}

function move_test_folder(e,data, ref){
    let old_parent_dbID = get_old_parent_dbID(ref, data),
        new_parent_dbID = get_new_parent_dbID(ref, data),
        node_dbID = data['node']['a_attr']['dbID'];

    $.ajax({
        url: 'test_folder/move_test_folder',
        type: "POST",
        data: {
            'old_parent_dbID': old_parent_dbID,
            'new_parent_dbID': new_parent_dbID,
            'node_dbID': node_dbID
        },
        success: function(res) {

        },
        error: function(ts) {
            console.log(ts)
        }
    })
}

function rename_test_folder(e,data){
    $.ajax({
        type: 'POST',
        url: 'test_folder/rename_test_folder',
        data: {
            'dbID' : data['node']['a_attr']['dbID'],
            'dbType' : data['node']['a_attr']['dbType'],
            'new_name' : data['node']['text']
        },
        dataType: 'json',
        success: function(data){
            $('#choose_target_test_folder_tree').jstree(true).refresh();
        },
        error : function(error) {console.log(error)}
    });
}

function test_folder_new_child_chapter(current_test_folder_dbID){
    console.log(current_test_folder_dbID)

    $.ajax({
        url: get_root_path() + 'test_folder/test_folder_new_child_chapter',
        type: "POST",
        data: {'current_test_folder_dbID': current_test_folder_dbID},
        success: function(res) {
            if ($('#test_folder_tree').jstree(true)){
                $('#test_folder_tree').jstree(true).refresh();
            }

            if ($('#choose_target_test_folder_tree').jstree(true)){
                $('#choose_target_test_folder_tree').jstree(true).refresh();
            }

            if ($('#test_folder_tree_test_by_template').jstree(true)){
                $('#test_folder_tree_test_by_template').jstree(true).refresh();
            }
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}

function show_tests_in_folder(){
    $.ajax({
        url: 'test_folder/show_tests_in_folder',
        type: "POST",
        data: {
            'current_test_folder_dbID': test_folder_action_data['current_test_folder']
        },
        success: function(res) {
            var el = document.getElementById('tests_in_test_folder');
            el.innerHTML = res;
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}

function select_view_test_folder(e,data){
    let current_test_folder_dbID = data['node']['a_attr']['dbID'];
    test_folder_action_data['current_test_folder'] = current_test_folder_dbID;

    var pathname = window.location.pathname; // Returns path only
    console.log(pathname);
    if (pathname === '/test_generated/created_tests'){
        show_tests_in_folder()
    }
}

function delete_test_folder_from_db(e, data){
    $.ajax({
        type: 'POST',
        url: 'test_folder/delete_test_folder_from_db',
        data: {
            'dbID' : data['node']['a_attr']['dbID'],
        },
        success: function(data){},
        error : function(error) {console.log(error)}
    });
}

function show_all_user_tests(){
    $.ajax({
        type: 'POST',
        url: '../test_folder/show_all_user_tests',
        data: {},
        success: function(res){
            var el = document.getElementById('tests_in_test_folder');
            el.innerHTML = res;
        },
        error : function(error) {console.log(error)}
    });
}

function show_user_tests_outside_folders(){
    $.ajax({
        type: 'POST',
        url: '../test_folder/show_user_tests_outside_folders',
        data: {},
        success: function(res){
            var el = document.getElementById('tests_in_test_folder');
            el.innerHTML = res;
        },
        error : function(error) {console.log(error)}
    });
}

function move_test_to_another_folder(){
    $.ajax({
        type: 'POST',
        url: '../test_folder/move_test_to_another_folder',
        data: {
            'test_id': current_test_id,
            'target_test_folder_id': target_test_folder_id

        },
        success: function(res){
            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('created_tests') === -1){
                var test_folder_name = $("#choose_target_test_folder_tree").jstree("get_selected", true)[0]['text'];
                document.getElementById("test_folder_name").innerText = test_folder_name
            }
            else{
                show_tests_in_folder()
            }
        },
        error : function(error) {console.log(error)}
    });
}

function show_choose_target_test_fodler_modal(){
    $('#choose_target_test_folder_modal').modal('show');
}


$(function () {
	$('#choose_target_test_folder_tree').jstree(tree_inner()).bind('select_node.jstree', function (e, data) {
	    target_test_folder_id = data['node']['a_attr']['dbID'];
  	}).bind('rename_node.jstree', function (e, data) {
  	    rename_test_folder(e,data)
  	}).bind('copy_node.jstree', function (e, data) {
        // copy_solution_folder(e,data)
  	}).bind('move_node.jstree', function (e, data) {
  	    // move_solution_folder(e,data)
  	}).bind('delete_node.jstree', function (e, data) {
        delete_test_folder_from_db(e,data)
  	}).bind('refresh.jstree', function (e, data) {
  	    // select_created_node(node_to_select_dbID)
  	});
});

$(function () {
	$('#test_folder_tree_test_by_template').jstree(tree_inner()).bind('select_node.jstree', function (e, data) {
	    target_test_folder_id = data['node']['a_attr']['dbID'];
  	}).bind('rename_node.jstree', function (e, data) {
  	    rename_test_folder(e,data)
  	}).bind('copy_node.jstree', function (e, data) {
        // copy_solution_folder(e,data)
  	}).bind('move_node.jstree', function (e, data) {
  	    // move_solution_folder(e,data)
  	}).bind('delete_node.jstree', function (e, data) {
        delete_test_folder_from_db(e,data)
  	}).bind('refresh.jstree', function (e, data) {
  	    // select_created_node(node_to_select_dbID)
  	});
});


function tree_inner(){
    return {
		'plugins': [ 'dnd', 'types', 'contextmenu', 'state'],
		'core': {
			'data': {
				"url": function(){
				    var pathname = window.location.pathname; // Returns path only
				    if (pathname.indexOf('test_generated') !== -1){
				        return "../../test_folder/get_test_folder_tree"
                    }
				    return "test_folder/get_test_folder_tree"
                },
				"dataType": "json"
			},
			'dblclick_toggle': false,
			'multiple': false,
			'expand_selected_onload': true,
			'check_callback': function (operation, node, node_parent, node_position, more) {
                if (operation == 'copy_node') {
                    return false
                }
                return true
            },
            'themes':{'dots': false},
		},
		"contextmenu": {
            "items": function($node) {
                var tree = $("#tree").jstree(true);
                return {
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
                },
                    //delete item from database
                    "remove": {
                    "separator_before": false,
                        "icon": false,
                        "separator_after": false,
                        "_disabled": function (data) {
                        let inst = $.jstree.reference(data.reference),
                            node = inst.get_node(data.reference);

                        if (node['a_attr']['system_name']==='ROOT_CATALOG'){return true}

                        return false
                    },
                    "label": "Удалить из базы данных",
                        "action": function (data) {
                        let inst = $.jstree.reference(data.reference),
                            obj = inst.get_node(data.reference);
                        if (inst.is_selected(obj)) {
                            inst.delete_node(inst.get_selected());
                        }
                        else {
                            inst.delete_node(obj);
                        }
                    }
                },
                    "cut": {
                    "separator_before": true,
                        "separator_after": false,
                        "label": "Cut",
                        "_disabled": function (data) {
                        let inst = $.jstree.reference(data.reference),
                            node = inst.get_node(data.reference);

                        if (node['a_attr']['system_name']==='ROOT_CATALOG'){return true}

                        return false
                    },
                    "action": function (data) {
                        let inst = $.jstree.reference(data.reference),
                            obj = inst.get_node(data.reference);
                        if (inst.is_selected(obj)) {
                            inst.cut(inst.get_top_selected());
                        }
                        else {
                            inst.cut(obj);
                        }
                    }
                },
                //     "copy": {
                //     "separator_before": false,
                //         "icon": false,
                //         "separator_after": false,
                //         "label": "Copy",
                //         "_disabled": function (data) {
                //         let inst = $.jstree.reference(data.reference),
                //             node = inst.get_node(data.reference);
                //
                //         if (node['a_attr']['system_name']==='ROOT_CATALOG'){return true}
                //
                //         return false
                //     },
                //     "action": function (data) {
                //         let inst = $.jstree.reference(data.reference),
                //             obj = inst.get_node(data.reference);
                //         if (inst.is_selected(obj)) {
                //             inst.copy(inst.get_top_selected());
                //         }
                //         else {
                //             inst.copy(obj);
                //         }
                //     }
                // },
                    "paste": {
                    "separator_before": false,
                        "icon": false,
                        "_disabled": function (data) {
                        return !$.jstree.reference(data.reference).can_paste();
                    },
                    "separator_after": false,
                        "label": "Paste",
                        "action": function (data) {
                        let inst = $.jstree.reference(data.reference),
                            obj = inst.get_node(data.reference);
                        inst.paste(obj);
                    }
                },
                    "new_child_chapter": {
                    "separator_before": false,
                        "separator_after": false,
                        "_disabled": function (data) {
                        // var inst = $.jstree.reference(data.reference),
                        //     node = inst.get_node(data.reference);
                        // if (node['a_attr']['dbType'] === 'Source_Folder'){return true}
                        // if (node['a_attr']['dbType'] === 'TaskNumber'){return true}
                        return false
                    },
                    "label": "Создать подпапку",
                    "action": function (data) {
                        let current_test_folder_dbID = $node['a_attr']['dbID'];
                        test_folder_new_child_chapter(current_test_folder_dbID)
                    }
                },

                }
            }
            },
		"types": {
			"#": {
				"valid_children": [],
			},
			"Folder": {
				"icon": PATH_JSTREE_PIC + "folder.png",
				"valid_children": ['Folder']
			}
		}
	}
}

function get_old_parent_dbID(ref, data){
    // let ref = $('#source_tree').jstree(true);

    let old_parent_jstree_id = data['old_parent'],
		old_parent = ref.get_node(old_parent_jstree_id),
        old_parent_dbID = old_parent['a_attr']['dbID'];

    return old_parent_dbID
}

function get_old_parent_dbType(ref, data){
    // let ref = $('#source_tree').jstree(true);

    let old_parent_jstree_id = data['old_parent'],
		old_parent = ref.get_node(old_parent_jstree_id),
        old_parent_dbType = old_parent['a_attr']['dbType'];

    return old_parent_dbType
}

function get_new_parent_dbType(ref, data){
    // let ref = $('#source_tree').jstree(true);

    let new_parent_jstree_id = data['parent'],
        new_parent = ref.get_node(new_parent_jstree_id),
        new_parent_dbType = new_parent['a_attr']['dbType'];

    return new_parent_dbType
}

function get_new_parent_dbID(ref, data){
    // let ref = $('#source_tree').jstree(true);

    let new_parent_jstree_id = data['parent'],
        new_parent = ref.get_node(new_parent_jstree_id),
        new_parent_dbID = new_parent['a_attr']['dbID'];

    return new_parent_dbID
}

function get_parent_dbID(ref, data){
    // let ref = $('#source_tree').jstree(true);
    let parent_jstree_id = data['node']['parent'];
    if (parent_jstree_id === '#'){
        let parent_dbID = 'ROOT';
        return parent_dbID
    }
    else{
        let parent = ref.get_node(parent_jstree_id),
        parent_dbID = parent['a_attr']['dbID'];
        return parent_dbID
    }
}

function get_parent_dbType(ref, data){
    // let ref = $('#source_tree').jstree(true);
    let parent_jstree_id = data['node']['parent'];
    if (parent_jstree_id === '#'){
        let parent_dbType = 'ROOT';
        return parent_dbType
    }
    else{
        let parent = ref.get_node(parent_jstree_id),
        parent_dbType = parent['a_attr']['dbType'];
        return parent_dbType
    }
}