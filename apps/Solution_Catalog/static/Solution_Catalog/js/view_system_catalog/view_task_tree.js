$(function () {
	$('#system_solution_catalog').jstree({
		'plugins': ['types', 'state'],
		'core': {
			'data': {
				"url": "get_main_tree",
				"dataType": "json"
			},
			'dblclick_toggle': false,
			'multiple': false,
			'expand_selected_onload': true,
			'check_callback': true,
			'themes':{'dots':false}
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
	}).bind('select_node.jstree', function (e, data) {
		select_view_folder(e,data);
  	});
});