$(function() {
	$('#mathattr_tree').jstree({
		'plugins' : [ 'dnd', 'types', 'search' ],
        'search': {'show_only_matches' : true},
		'core' : {
		    'expand_selected_onload' : false,
			'check_callback' :  function(operation, node, node_parent, node_position, more) {
                    // operation can be 'create_node', 'rename_node', 'delete_node', 'move_node' or 'copy_node'
                    // in case of 'rename_node' node_position is filled with the new node name

                    // if (operation === "move_node") {
						// return false
                    // }
                    return false;  //allow all other operations
                },
			'data' : {
                "url" : "mathattr_tree",
                "dataType" : "json" // needed only if you do not supply JSON headers
            },
			'themes': {'dots' : false},
			'dblclick_toggle' : false
		},
		"types" : {
			"#" : {
				"valid_children" : []
			},
			"Folder" : {
				"icon" : "jstree-folder",
				"valid_children" : ['MathAttr', 'Folder']
			},
			"MathAttr" : {
				"icon" : PATH_JSTREE_PIC + "mathattr.png",
				"valid_children" : []
			},
		}
	});
});
