$(function () {
	$('#attr_tree_in_modal').jstree({
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
			"AND": {
				"icon": PATH_JSTREE_PIC + "folder.png",
				"valid_children": ['AND', 'FILTER_leaf']
			},
			"MathAttr": {
				"icon": PATH_JSTREE_PIC + "mathattr.png",
				"valid_children": []
			},
		}
	});
});


// JSON для пустого фильтра
var empty_filterJson = [{
    'text' : 'Выбранные атрибуты',
	'type' : 'ROOT',
    'a_attr': {'dbtype': 'NONE', 'dbID' : 'NONE'},
	'state' : {'opened' : true},
	'children' : []
	}];

//deleteNode
(function ($, undefined) {
	"use strict";
	var img = document.createElement('IMG');
	img.className = "jstree-deleteNode";

	$.jstree.defaults.deleteNode = $.noop;
	$.jstree.plugins.deleteNode = function (options, parent) {
		this.bind = function () {
			parent.bind.call(this);
			this.element
				.on("click.jstree", ".jstree-deleteNode", $.proxy(function (e) {
						e.stopImmediatePropagation();
						this.settings.deleteNode.call(this, this.get_node(e.target));
					}, this));
		};
		this.teardown = function () {
			if(this.settings.deleteNode) {
				this.element.find(".jstree-deleteNode").remove();
			}
			parent.teardown.call(this);
		};
		this.redraw_node = function(obj, deep, callback, force_draw) {
			obj = parent.redraw_node.call(this, obj, deep, callback, force_draw);
			if(obj) {
				if (obj.childNodes[1].getAttribute('dbtype') !== 'NONE') {
                    if ((obj.childNodes.length > 2 && obj.childNodes[2].id !== 'j2_1_anchor') || obj.childNodes.length === 2) {
                        var tmp = img.cloneNode(true);
                        tmp.src = PATH_JSTREE_PIC + "delete.png";
                        obj.insertBefore(tmp, obj.childNodes[2]);
                    }
                }
			}
			return obj;
		};
	};
})(jQuery);

//solattr_tree
$(function() {
	$('#attr_to_add_in_modal').jstree({
		'plugins' : [ 'dnd', 'types', 'deleteNode'],
		'deleteNode': function(node){
					var ref = $('#attr_to_add_in_modal').jstree(true);
					ref.delete_node(node);
				},
		'core' : {
			'check_callback' : function(operation, node, node_parent, node_position, more) {
				if(operation == 'copy_node'){
					current_dbID = node['a_attr']['dbID'];
					var ref = $('#attr_to_add_in_modal').jstree(true);
					var i,j, child;
					for (i = 0; i < node_parent['children'].length; i++) {
						child_id = node_parent['children'][i];
						child = ref.get_node(child_id);
						dbID = child['a_attr']['dbID'];
						if (dbID === current_dbID){
							return false
						}
					}
                }
				return true
			},
            'data' : empty_filterJson,
			'themes': {'dots' : false},
			'dblclick_toggle' : false
		},
		"types" : {
			"#" : {
				"valid_children" : []
			},
			"ROOT" : {
				"icon" : "fas fa-folder",
				"valid_children" : ['MathAttr']
			},
			"MathAttr" : {
				"icon" : PATH_JSTREE_PIC + "mathattr.png",
				"valid_children" : []
			},
		}
	}).bind('copy_node.jstree', function(e, data) {
        	// action_data['attr_to_add'] = $("#attr_to_add_in_modal").jstree(true).get_json()
        attributes_to_add = $("#attr_to_add_in_modal").jstree(true).get_json();
	}).bind('move_node.jstree', function(e, data) {
        	// action_data['attr_to_add'] = $("#attr_to_add_in_modal").jstree(true).get_json()
        attributes_to_add = $("#attr_to_add_in_modal").jstree(true).get_json();
	}).bind('delete_node.jstree', function(e, data) {
        	// action_data['attr_to_add'] = $("#attr_to_add_in_modal").jstree(true).get_json()
        attributes_to_add = $("#attr_to_add_in_modal").jstree(true).get_json();
	})
});


