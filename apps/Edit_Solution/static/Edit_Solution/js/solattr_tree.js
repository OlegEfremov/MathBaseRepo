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
				if (obj.childNodes[1].getAttribute('dbtype') !== 'Solution') {
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
	$('#solattr_tree').jstree({
		'plugins' : [ 'dnd', 'types', 'deleteNode'],
		'deleteNode': function(node){
					var ref = $('#solattr_tree').jstree(true);
					ref.delete_node(node);

    	    		var node_dbType = node['a_attr']['dbType'];
    	    		var node_dbID = node['a_attr']['dbID'];

    				var sendData = 'node_dbType='+node_dbType;
    	    		sendData += '&node_dbID='+node_dbID;
    	    		sendData += '&solid='+solid;

					$.ajax({
						type: 'POST',
	  					url: 'delete_mathattribue_from_solution',
	  					data: sendData,
	  					success: function(data){
							show_tasks(solid)
						}
					});

				},
		'core' : {
			'check_callback' : function(operation, node, node_parent, node_position, more) {
				if(operation == 'copy_node'){
					current_dbID = node['a_attr']['dbID'];
					var ref = $('#solattr_tree').jstree(true);
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

				if (more) {
                    if (more.is_multi) {
                    	// prevent move from source catalog to task - only copy
                        more.origin.settings.dnd.always_copy = true;
                    } else {
                        // prevent self-dnd in tasksource_tree
                        return false
                    }
                }
				return true
			},
            'data' : {
                "url" : "solattr_tree/"+solid,
                "dataType" : "json" // needed only if you do not supply JSON headers
            },
			'themes': {
            	'dots' : false
        	},
			'dblclick_toggle' : false
		},
		"types" : {
			"#" : {
				"valid_children" : []
			},
			"Solution" : {
				"icon" : "fas fa-key",
				"valid_children" : ['MathAttr']
			},
			"MathAttr" : {
				"icon" : PATH_JSTREE_PIC + "mathattr.png",
				"valid_children" : []
			},
		}
	})
        .bind('copy_node.jstree', function(e, data) {

			var nodeNode = data.node;
			var node_dbType = nodeNode['a_attr']['dbType'];
			var node_dbID = nodeNode['a_attr']['dbID'];

			var sendData = 'node_dbType='+node_dbType;
			sendData += '&node_dbID='+node_dbID;
			sendData += '&solid='+solid;


			$.ajax({
			type: 'POST',
			url: 'add_attr_to_sol',
			data: sendData,
			success: function(data){
				show_tasks(solid)
				}
			});
		})
		.bind('move_node.jstree', function (e, data) {})
		.bind('delete_node.jstree', function (e, data) {});
});



// var preventDelete = false;
//
// $('#mathattr_tree').jstree({
//   core : { check_callback : function (operation) { if (preventDelete && operation=="delete_node") { preventDelete = false; return false; } return true; } },
//   ...
// $('#solattr_tree').jstree({
//   core : { check_callback : function (operation) { if (preventDelete && operation=="delete_node") { preventDelete = false; return false; } return true; } },
//   ...
// $('#mathattr_tree, #solattr_tree').on('copy_node.jstree', function (e, data) {
//   if (data.is_multi) {
//     preventDelete = true;
//   }
// });