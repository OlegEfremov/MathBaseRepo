function set_node_type(newType, node = false) {
	var ref = $('#filter_tree').jstree(true);
    if (node === false){
		var	sel = ref.get_selected();
		if(!sel.length) { return false; }
		sel = sel[0];
		ref.set_type(sel, newType);}
	else {
		ref.set_type(node, newType);}
   }

function create_new_node() {
	$('#filter_tree').jstree().create_node('j2_1', {'type':'AND', 'text':'Группа условий'});
   }
