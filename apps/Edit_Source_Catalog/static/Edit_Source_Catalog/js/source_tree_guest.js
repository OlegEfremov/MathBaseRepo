$(function() {
	$('#source_tree').jstree({
		'plugins' : ['types', "state"],
		'core' : {
			'check_callback' :  function(operation, node, node_parent, node_position, more) {
			    return false;  //allow all other operations
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
		.bind('select_node.jstree', function (e, data) {
			create_data['node_dbID'] = data['node']['a_attr']['dbID'];
		    create_data['node_dbType'] = data['node']['a_attr']['dbType'];
            create_data['parent_dbID'] = get_parent_dbID(data);

            let selected_node_dbType = data['node']['a_attr']['dbType'],
                selected_node_dbID = data['node']['a_attr']['dbID'];

            action_data['view_folder'] = selected_node_dbID;

            show_tasks(selected_node_dbID, 1, selected_node_dbType);

            // if (selected_node_dbType === 'Source'){
            //     show_tasks_source(selected_node_dbID,1)
            // } else if (selected_node_dbType === 'Chapter'){
            //     console.log(selected_node_dbID);
            //     show_tasks_chapter(selected_node_dbID,1)
            // } else if (selected_node_dbType === 'TaskNumber'){
            //     show_tasks_task(selected_node_dbID,1)
            // }

  		})
        .bind('refresh.jstree', function (e, data) {
            // select_created_node(node_to_select_dbID)
        })
});