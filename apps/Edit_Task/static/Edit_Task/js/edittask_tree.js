//source_tree
$(function() {
	$('#source_tree').jstree({
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
                "url" : "source_tree",
                "dataType" : "json" // needed only if you do not supply JSON headers
            },
			'themes': {
            	'dots' : false
        	},
			'dblclick_toggle' : false

		},
		"types" : {
			// "#" : {
			// 	"valid_children" : []
			// },
			// "Folder" : {
			// 	"icon" : "jstree-folder",
			// 	"valid_children" : []
			// },
			// "Source" : {
			// 	"icon" : "fas fa-book",
			// 	"valid_children" : []
			// },
			// "TaskNumber" : {
			// 	"icon" : "fas fa-list-ol",
			// 	"valid_children" : []
			// }
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
	});
});

// function send_current_filter(data = false) {
// 	var sendData;
// 	if (data === false){sendData =$('#tasksource_tree').jstree('get_json', "#");}
// 	else {sendData = data;}
// 	sendData = JSON.stringify(sendData);
// 	$.ajax({
// 		type: 'POST',
// 		url: 'advsearch/current_filter',
// 		//dataType: "json",
// 		data: sendData,
// 		success: function(data){
// 		}
// 	});
//
// 	}
//
// function set_node_type(newType, node = false) {
// 	var ref = $('#tasksource_tree').jstree(true);
//     if (node === false){
// 		var	sel = ref.get_selected();
// 		if(!sel.length) { return false; }
// 		sel = sel[0];
// 		ref.set_type(sel, newType);}
// 	else {
// 		ref.set_type(node, newType);}
//    }
//
// function delete_node() {
// 	var ref = $('#tasksource_tree').jstree(true);
// 	var sel = ref.get_selected();
// 	if(!sel.length) { return false; }
// 	ref.delete_node(sel);
// 	}
//
// function create_new_node() {
// 	$('#filter_tree').jstree().create_node('j2_1', {'type':'AND', 'text':'Группа условий'});
//    }
//
// function update_tree() {
// 	var v =$('#tasksource_tree').jstree('get_json', "#");
//     var mytext = JSON.stringify(v);
// 	newdata = JSON.parse(mytext);
//
// 	send_current_filter(newdata);
//
// 	$('#tasksource_tree').jstree(true).settings.core.data = newdata;
//     $('#tasksource_tree').jstree(true).refresh();
//    }
//
// function print_json() {
// 	var v =$('#filter_tree').jstree('get_json', "#");
// 	var mytext = JSON.stringify(v);
// 	console.log(mytext);
//    }

