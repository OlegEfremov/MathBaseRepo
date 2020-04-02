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
                if (this.settings.deleteNode) {
                    this.element.find(".jstree-deleteNode").remove();
                }
                parent.teardown.call(this);
            };
            this.redraw_node = function (obj, deep, callback, force_draw) {
                obj = parent.redraw_node.call(this, obj, deep, callback, force_draw);
                if (obj) {
                    if (obj.childNodes[1].getAttribute('dbtype') !== 'Task') {
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

