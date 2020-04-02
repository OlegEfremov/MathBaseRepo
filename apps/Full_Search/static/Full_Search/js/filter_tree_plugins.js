
//Плагин editNode_2
(function ($, undefined) {
	"use strict";
	var img = document.createElement('IMG');
	img.className = "jstree-editNode_2";

	$.jstree.defaults.editNode_2 = $.noop;
	$.jstree.plugins.editNode_2 = function (options, parent) {
		this.bind = function () {
			parent.bind.call(this);
			this.element
				.on("click.jstree", ".jstree-editNode_2", $.proxy(function (e) {
						e.stopImmediatePropagation();
						this.settings.editNode_2.call(this, this.get_node(e.target));
						var svf_dbID = this.get_node(e.target)['a_attr']['dbID'];
						window.location.href = 'edit_savedfilter/'+svf_dbID;
					}, this));
		};
		this.teardown = function () {
			if(this.settings.editNode_2) {
				this.element.find(".jstree-editNode_2").remove();
			}
			parent.teardown.call(this);
		};
		this.redraw_node = function(obj, deep, callback, force_draw) {
			obj = parent.redraw_node.call(this, obj, deep, callback, force_draw);
			if(obj) {
				if (obj.childNodes[2].getAttribute('dbtype') === 'SavedFilter') {
                    if ((obj.childNodes.length > 2 && obj.childNodes[2].id !== 'j2_1_anchor') || obj.childNodes.length === 2) {
                        var tmp = img.cloneNode(true);
                        tmp.src = PATH_JSTREE_PIC + "edit.png";
                        obj.insertBefore(tmp, obj.childNodes[3]);
                    }
                }
			}
			return obj;
		};
	};
})(jQuery);

//Плагин deleteNode
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
				if ((obj.childNodes.length >2  && obj.childNodes[2].id !== 'j2_1_anchor') || obj.childNodes.length === 2){
				var tmp = img.cloneNode(true);
				tmp.src = PATH_JSTREE_PIC + "delete.png";
				obj.insertBefore(tmp, obj.childNodes[3]);
				}
			}
			return obj;
		};
	};
})(jQuery);

//Плагин NOTbutton
(function ($, undefined) {
	"use strict";
	var img = document.createElement('IMG');
	img.className = "jstree-NOTbutton";

	$.jstree.defaults.NOTbutton = $.noop;
	$.jstree.plugins.NOTbutton = function (options, parent) {
		this.bind = function () {
			parent.bind.call(this);
			this.element
				.on("click.jstree", ".jstree-NOTbutton", $.proxy(function (e) {
						e.stopImmediatePropagation();

						var nodeType = this.get_node(e.target).type;
						if (nodeType === 'AND'){set_node_type('NOT-AND', this.get_node(e.target)); e.currentTarget.src = PATH_JSTREE_PIC+"NOT.png";}
						else if (nodeType === 'NOT-AND'){set_node_type('AND',this.get_node(e.target)); e.currentTarget.src = PATH_JSTREE_PIC+"OK.png";}
						else if (nodeType === 'OR'){set_node_type('NOT-OR',this.get_node(e.target)); e.currentTarget.src = PATH_JSTREE_PIC+"NOT.png";}
						else if (nodeType === 'NOT-OR'){set_node_type('OR',this.get_node(e.target)); e.currentTarget.src = PATH_JSTREE_PIC+"OK.png";}

						else if (nodeType === 'MathAttr'){set_node_type('EXCLUDE_MathAttr', this.get_node(e.target)); e.currentTarget.src = PATH_JSTREE_PIC+"NOT.png";}
						else if (nodeType === 'SavedFilter'){set_node_type('EXCLUDE_SavedFilter', this.get_node(e.target)); e.currentTarget.src = PATH_JSTREE_PIC+"NOT.png";}

						else if (nodeType === 'EXCLUDE_MathAttr'){set_node_type('MathAttr', this.get_node(e.target)); e.currentTarget.src = PATH_JSTREE_PIC+"OK.png";}
						else if (nodeType === 'EXCLUDE_SavedFilter'){set_node_type('SavedFilter', this.get_node(e.target)); e.currentTarget.src = PATH_JSTREE_PIC+"OK.png";}
						else {
							console.log('ERROR: unknown node type - 1')
							console.log(nodeType)
						}
						this.settings.NOTbutton.call(this, this.get_node(e.target));
					}, this));
		};
		this.teardown = function () {
			if(this.settings.NOTbutton) {
				this.element.find(".jstree-NOTbutton").remove();
			}
			parent.teardown.call(this);
		};
		this.redraw_node = function(obj, deep, callback, force_draw) {
			obj = parent.redraw_node.call(this, obj, deep, callback, force_draw);

			var current_icon = obj.childNodes[1].childNodes[0].style.backgroundImage.replace('url(\"' + PATH_JSTREE_PIC,"").replace('\")','');
			// if(obj && current_icon!=="leaf-FILTER.png" && current_icon!=="leaf-EXCLUDE.png" && current_icon!=="feature.png" && current_icon!=="fact.png" && current_icon!=="object.png" && current_icon!=="method.png" && current_icon!=="tasktype.png") {
			 if(obj) {

				var tmp = img.cloneNode(true);
                if(current_icon === "folder-AND.png"){tmp.src = PATH_JSTREE_PIC+"OK.png";}
				else if(current_icon === "mathattr.png"){tmp.src = PATH_JSTREE_PIC+"OK.png";}
                else if(current_icon === "folder.png"){tmp.src = PATH_JSTREE_PIC+"OK.png";}
                else if(current_icon === "folder-OR.png"){tmp.src = PATH_JSTREE_PIC+"OK.png";}
				else if (current_icon ==="savedfilter.png"){tmp.src = PATH_JSTREE_PIC+"OK.png";}
				else if (current_icon ==="folder-NOT-AND.png"){tmp.src = PATH_JSTREE_PIC+"NOT.png";}
				else if (current_icon ==="folder-NOT-OR.png"){tmp.src = PATH_JSTREE_PIC+"NOT.png";}
				else if (current_icon ==="mathattr_NOT.png"){tmp.src = PATH_JSTREE_PIC+"NOT.png";}
				else if (current_icon ==="savedfilter_NOT.png"){tmp.src = PATH_JSTREE_PIC+"NOT.png";}
				else {console.log('else'); console.log(current_icon); tmp.src = PATH_JSTREE_PIC+"delete.png";}

				obj.insertBefore(tmp, obj.childNodes[1]);
			}
			return obj;
		};
	};
})(jQuery);

