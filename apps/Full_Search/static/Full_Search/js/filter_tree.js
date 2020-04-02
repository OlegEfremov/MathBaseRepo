// JSON для пустого фильтра
var empty_filterJson = [{
    'text' : 'Текущий фильтр',
	'type' : 'AND',
    'a_attr': {'dbtype': 'Root', 'dbID' : 'NONE'},
	'state' : {'opened' : true},
	'children' : []
	}];


$(function() {
	$('#filter_tree').jstree({
		'plugins' : [ 'dnd', 'types', 'NOTbutton', 'deleteNode', 'editNode_2'],
		'core' : {
		    'multiple': false,
            'dblclick_toggle' : false,
			'check_callback' : function(operation, node, node_parent, node_position, more) {
				return true
			},
			'data' : empty_filterJson,
            'themes': {'dots':false},
		},
		'deleteNode': function(node){
			var ref = $('#filter_tree').jstree(true);
			ref.delete_node(node);
			},
		"types" : {
			"#" : {
				"valid_children" : []
			},
			"AND" : {
				"icon" : PATH_JSTREE_PIC+"folder-AND.png",
				"valid_children" : ['AND', 'OR', 'NOT-AND', 'NOT-OR', 'EXCLUDE_leaf', 'FILTER_leaf', 'EXCLUDE_MathAttr', 'MathAttr', 'Object', 'Fact', 'Feature', 'TaskType', 'Method', 'Solution', 'Folder', 'SavedFilter']
			},
			"OR" : {
				"icon" : PATH_JSTREE_PIC+"folder-OR.png",
				"valid_children" : ['AND', 'OR', 'NOT-AND', 'NOT-OR', 'EXCLUDE_leaf', 'FILTER_leaf', 'EXCLUDE_MathAttr', 'MathAttr', 'Object', 'Fact', 'Feature', 'TaskType', 'Method', 'Solution', 'Folder', 'SavedFilter']
			},
			"NOT-AND" : {
				"icon" : PATH_JSTREE_PIC+"folder-NOT-AND.png",
				"valid_children" : ['AND', 'OR', 'NOT-AND', 'NOT-OR', 'EXCLUDE_leaf', 'FILTER_leaf',  'EXCLUDE_MathAttr', 'MathAttr', 'Object', 'Fact', 'Feature', 'TaskType', 'Method', 'Solution', 'Folder', 'SavedFilter']
			},
			"NOT-OR" : {
				"icon" : PATH_JSTREE_PIC+"folder-NOT-OR.png",
				"valid_children" : ['AND', 'OR', 'NOT-AND', 'NOT-OR', 'EXCLUDE_leaf', 'FILTER_leaf',  'EXCLUDE_MathAttr', 'MathAttr', 'Object', 'Fact', 'Feature', 'TaskType', 'Method', 'Solution', 'Folder', 'SavedFilter']
			},
			"MathAttr" : {
				"icon" : PATH_JSTREE_PIC+"mathattr.png",
				"valid_children" : []
			},
			"SavedFilter" : {
				"icon" : PATH_JSTREE_PIC+"savedfilter.png",
				"valid_children" : []
			},
			"EXCLUDE_MathAttr" : {
				"icon" : PATH_JSTREE_PIC+"mathattr_NOT.png",
				"valid_children" : []
			},
			"EXCLUDE_SavedFilter" : {
				"icon" : PATH_JSTREE_PIC+"savedfilter_NOT.png",
				"valid_children" : []
			}
		}
	})
        .bind('copy_node.jstree', function(e, data) {
        	for (let i in data.node.children_d){
        	    let node_id =  data.node.children_d[i];
                if($("#filter_tree").jstree(true).get_node(node_id).type === 'AND') {$("#filter_tree").jstree(true).set_icon(node_id, PATH_JSTREE_PIC + "folder-AND.png")};
            }
        	if(data.node.type === 'AND') {$("#filter_tree").jstree(true).set_icon(data.node.id, PATH_JSTREE_PIC + "folder-AND.png");}
		});
}).on("click", ".jstree-anchor", function(e) {
    let node = $("#filter_tree").jstree(true).get_node($(this)),
        type = node.type;

    if(type === 'OR') {set_node_type('AND');}
    else if(type === 'AND') {set_node_type('OR');}
    else if(type === 'NOT-AND') {set_node_type('NOT-OR');}
    else if(type === 'NOT-OR') {set_node_type('NOT-AND');}

   });
