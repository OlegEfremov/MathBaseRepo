
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
//    }

