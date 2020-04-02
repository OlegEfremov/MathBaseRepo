// Дерево всех атрибутов для формирования текущего фильтра
$(function () {
	$('#attr_tree').jstree({
		'plugins': ['dnd', 'types'],
		'core': {
			'data': {
				"url": "attr_tree",
				"dataType": "json"
			},
			'dblclick_toggle': false,
			'multiple': false,
			'expand_selected_onload': false,
			'check_callback': false,
			'themes':{'dots':false},
		},
		"types": {
			"#": {
				"valid_children": ["AND"]
			},
			"EXCLUDE_leaf": {
				"icon": "jstree-folder",
				"valid_children": []
			},
			"FILTER_leaf": {
				"icon": "jstree-folder",
				"valid_children": []
			},
			"AND": {
				"icon": PATH_JSTREE_PIC + "folder.png",
				"valid_children": ['AND', 'FILTER_leaf']
			},
			"OR": {
				"icon": PATH_JSTREE_PIC + "folder.png",
				"valid_children": ['AND', 'FILTER_leaf']
			},
			"NOT-AND": {
				"icon": PATH_JSTREE_PIC + "folder.png",
				"valid_children": ['AND', 'FILTER_leaf']
			},
			"NOT-OR": {
				"icon": PATH_JSTREE_PIC + "folder.png",
				"valid_children": ['AND', 'FILTER_leaf']
			},
            "MathAttr" : {
				"icon" : PATH_JSTREE_PIC + "mathattr.png",
                // "icon": "jstree-file",
				"valid_children" : []
			},
			"SavedFilter": {
				"icon": PATH_JSTREE_PIC + "savedfilter.png",
				"valid_children": []
			}
		}
	});
});
