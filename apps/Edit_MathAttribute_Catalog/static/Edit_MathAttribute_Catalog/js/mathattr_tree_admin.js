$(function() {
	$('#mathattr_tree').jstree({
		'plugins' : [ 'dnd', 'types', 'contextmenu', 'state'],
		'core' : {
			'check_callback' :  function(operation, node, node_parent, node_position, more) {
                if (more) {
                    if (more.is_multi) {
                        // prevent copy from task to source catalog
                        return false
                    } else {
                        more.origin.settings.dnd.always_copy = false;
                    }
                }

			    return true;  //allow all other operations
                },
			'data' : {
				"url" : "edit_mathattr_tree",
                "dataType" : "json"
            },
			'themes': {'dots' : false},
			'dblclick_toggle' : false,
            'multiple': false,
		    'expand_selected_onload' : true,
		},
		"contextmenu": {
            "items": {
                    "rename": {
                        "separator_before": false,
                        "separator_after": false,
                        "_disabled": false,
                        "label": "Rename",
                        "action": function (data) {
                            var inst = $.jstree.reference(data.reference),
                                obj = inst.get_node(data.reference);
                            inst.edit(obj);
                        }
                    },
                    //delete item from database
                    "delete": {
                        "separator_before": false,
                        "icon": false,
                        "separator_after": false,
                        "_disabled": function (data) {
                            var inst = $.jstree.reference(data.reference),
                                node = inst.get_node(data.reference),
                                parent_jstree_id = inst.get_parent(data.reference),
                                parent = inst.get_node(parent_jstree_id),
                                children_length = node['children'].length;

                            // //if node is system - restrict deleting
                            if (folders_system_names.indexOf(node['a_attr']['system_name']) !== -1){return true}

                            return false
                        },
                        "label": "Delete from DB",
                        "action": function (data) {
                            var inst = $.jstree.reference(data.reference),
                            node = inst.get_node(data.reference);

                            delete_node_from_db(node);

                            reset_current_folder();

                        }
                    },
                    "remove": {
                        "separator_before": false,
                        "icon": false,
                        "separator_after": false,
                        "_disabled": function (data) {
                            var inst = $.jstree.reference(data.reference),
                            node = inst.get_node(data.reference),
                            parent_jstree_id = inst.get_parent(data.reference),
                            parent = inst.get_node(parent_jstree_id);

                            //restrict removing if
                            // node is a Folder, node has children, node is a mathattribute in system folder
                            if (node['a_attr']['dbType'] === "MathAttribute_Folder"){return true}
                            if (node['children'].length !== 0){return true}
                            if (node['a_attr']['dbType'] === "MathAttribute" && parent['a_attr']['system_name'] === 'ALL_MATHATTRIBUTES'){return true}

                            return false
                        },
                        "label": "Remove from folder",
                        "action": function (data) {
                            var inst = $.jstree.reference(data.reference),
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
                            var inst = $.jstree.reference(data.reference),
                            node = inst.get_node(data.reference),
                            parent_jstree_id = inst.get_parent(data.reference),
                            parent = inst.get_node(parent_jstree_id);

                            //restrict cut if
                            // node is a system Folder, node has children, node is a mathattribute in system folder
                            if (folders_system_names.indexOf(node['a_attr']['system_name']) !== -1){return true}
                            if (node['children'].length !== 0){return true}
                            if (node['a_attr']['dbType'] === "Edit_MathAttribute_Catalog" && parent['a_attr']['system_name'] === 'ALL_MATHATTRIBUTES'){;return true}

                            return false
                        },
                        "action": function (data) {
                            var inst = $.jstree.reference(data.reference),
                                obj = inst.get_node(data.reference);
                            if (inst.is_selected(obj)) {
                                inst.cut(inst.get_top_selected());
                            }
                            else {
                                inst.cut(obj);
                            }
                        }
                    },
                    "copy": {
                        "separator_before": false,
                        "icon": false,
                        "separator_after": false,
                        "label": "Copy",
                        "action": function (data) {
                            var inst = $.jstree.reference(data.reference),
                                obj = inst.get_node(data.reference);
                            if (inst.is_selected(obj)) {
                                inst.copy(inst.get_top_selected());
                            }
                            else {
                                inst.copy(obj);
                            }
                        }
                    },
                    "paste": {
                        "separator_before": false,
                        "icon": false,
                        "_disabled": function (data) {
                            return !$.jstree.reference(data.reference).can_paste();
                        },
                        "separator_after": false,
                        "label": "Paste",
                        "action": function (data) {
                            var inst = $.jstree.reference(data.reference),
                                obj = inst.get_node(data.reference);
                            inst.paste(obj);
                        }
                    }
                }
            },
		"types" : {
			"#" : {
				"valid_children" : []
			},
			"ROOT" : {
				"valid_children" : ['Folder']
			},
			"Folder" : {
				"icon" : "jstree-folder",
				// "valid_children" : ['Object', 'Fact', 'Method', 'Feature', 'TaskType', 'Folder']
                "valid_children" : ['MathAttr', 'Folder']
			},
            "MathAttr" : {
				"icon" : PATH_JSTREE_PIC+"mathattr.png",
				"valid_children" : []
			},
		}
	})
        .bind('copy_node.jstree', function(e, data) {
        	copy_node(data)
		})
		.bind('move_node.jstree', function (e, data) {
		    move_node(data)
  		})
		.bind('rename_node.jstree', function (e, data) {
            rename_node(data)
		})
		.bind('delete_node.jstree', function (e, data) {

		    remove_node_from_folder(data);

            reset_current_folder();

            //which node need to select after refresh tree
            node_to_select_dbID = "NONE"
  		})
		.bind('select_node.jstree', function (e, data) {
			var type = data['node']['type'];
			var parent_dbID = '';
			if (type === 'Folder' || type === 'default'){
				document.getElementById('parent_folder').innerHTML = data['node']['text'];
				parent_dbID = data['node']['a_attr']['dbID'];
			}
			else if (type === 'ROOT'){
				document.getElementById('parent_folder').innerHTML = 'Корневой каталог';
				parent_dbID = "NONE";
			}
			else {
				var ref =$('#mathattr_tree').jstree(true),
				parent = ref.get_node(data['node']['parent']);
				document.getElementById('parent_folder').innerHTML = parent['text'];
				parent_dbID = parent['a_attr']['dbID'];
			}

			document.getElementById('parent_folder').value = parent_dbID;

  		})
        .bind('refresh.jstree', function (e, data) {
            select_created_node(node_to_select_dbID)
        })
});

