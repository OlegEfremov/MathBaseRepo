$(function() {
	$('#source_tree').jstree({
		'plugins' : [ 'dnd', 'types', 'contextmenu', "state"],
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
				// "url" : "source_tree",
                "url" : function (node) {

                    // return 'source_tree'
                    if (node.id === '#'){return 'source_tree'}
                        return 'source_tree/'+node['a_attr']['dbType']+'/'+node['a_attr']['dbID'];
                      },
                'data' : function (node) {return { 'id' : node.id }},
                "dataType" : "json"
            },
			'themes': {'dots' : false},
			'dblclick_toggle' : false,
            'multiple': false,
		    'expand_selected_onload' : true,
		},
		"contextmenu": {
            "items": {
                    "import": {
                        "separator_before": false,
                        "separator_after": false,
                        "_disabled": function (data) {
                            var inst = $.jstree.reference(data.reference),
                                node = inst.get_node(data.reference);
                            if (node['a_attr']['dbType'] === 'Source_Folder'){return true}
                            if (node['a_attr']['dbType'] === 'TaskNumber'){return true}
                            return false
                        },
                        "label": "Импорт",
                        "action": function (data) {
                            import_tasks_show_modal()
                        }
                    },
                    "new_child_chapter": {
                        "separator_before": false,
                        "separator_after": false,
                        "_disabled": function (data) {
                            var inst = $.jstree.reference(data.reference),
                                node = inst.get_node(data.reference);
                            if (node['a_attr']['dbType'] === 'Source_Folder'){return true}
                            if (node['a_attr']['dbType'] === 'TaskNumber'){return true}
                            return false
                        },
                        "label": "Новая глава-потомок",
                        "action": function (data) {
                            create_chapter()
                        }
                    },
                    "rename": {
                        "separator_before": false,
                        "separator_after": false,
                        "_disabled": false,
                        "label": "Переименовать",
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
                        "label": "Удалить из БД",
                        "action": function (data) {
                            var inst = $.jstree.reference(data.reference),
                            node = inst.get_node(data.reference);

                            delete_node_from_db(node);

                            // reset_current_folder();
                            //
                        }
                    },
                    //remove source from folder
                    "remove": {
                        "separator_before": false,
                        "icon": false,
                        "separator_after": false,
                        "_disabled": function (data) {
                            var inst = $.jstree.reference(data.reference),
                            node = inst.get_node(data.reference),
                            parent_jstree_id = inst.get_parent(data.reference),
                            parent = inst.get_node(parent_jstree_id);

                            if (node['a_attr']['dbType'] === "Source_Folder"){return true}
                            if (node['a_attr']['dbType'] === "TaskNumber"){return true}
                            if (node['a_attr']['dbType'] === "Chapter"){return true}

                            return false
                        },
                        "label": "Удалить из папки",
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
                        "label": "Вырезать",
                        "_disabled": function (data) {
                            var inst = $.jstree.reference(data.reference),
                            node = inst.get_node(data.reference),
                            parent_jstree_id = inst.get_parent(data.reference),
                            parent = inst.get_node(parent_jstree_id);

                            if (node['a_attr']['dbType'] === "TaskNumber"){return true}

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
                        "label": "Копировать",
                        "_disabled": function (data) {
                            var inst = $.jstree.reference(data.reference),
                            node = inst.get_node(data.reference),
                            parent_jstree_id = inst.get_parent(data.reference),
                            parent = inst.get_node(parent_jstree_id);

                            if (node['a_attr']['dbType'] === "TaskNumber"){return true}

                            return false
                        },
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
                        "label": "Вставить",
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
				"valid_children" : ['Source', 'Folder']
			},
			"Source" : {
				"icon" : 'fas fa-book',
				"valid_children" : ['Chapter', 'TaskNumber']
			},
			"TaskNumber" : {
				"icon" : 'fas fa-circle fa-xs',
				"valid_children" : []
			},
            "Chapter" : {
				"icon" : 'fas fa-list',
				"valid_children" : ['Chapter', 'TaskNumber']
			}
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
            //
            // reset_current_folder();
            // //which node need to select after refresh tree
            // node_to_select_dbID = "NONE"
  		})
		.bind('select_node.jstree', function (e, data) {
			create_data['node_dbID'] = data['node']['a_attr']['dbID'];
		    create_data['node_dbType'] = data['node']['a_attr']['dbType'];
            create_data['parent_dbID'] = get_parent_dbID(data);
            create_data['parent_dbType'] = get_parent_dbType(data);

            let selected_node_dbType = data['node']['a_attr']['dbType'],
                selected_node_dbID = data['node']['a_attr']['dbID'];

            var pathname = window.location.pathname; // Returns path only
            if (pathname.indexOf('/edit_task/main_page') === -1) {
                action_data['view_folder'] = selected_node_dbID;
                show_tasks(selected_node_dbID, 1, selected_node_dbType);
            }

            disable_create_buttons()

  		})
        .bind('refresh.jstree', function (e, data) {
            // select_created_node(node_to_select_dbID)
        })
});
