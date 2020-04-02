function select_view_folder(e,data){
	    let vf_dbID = data['node']['a_attr']['dbID'];
	    action_data['view_folder'] = vf_dbID;
	    checkbox_values={};
	    // document.getElementById('checkbox_counter').innerHTML = count_checkboxes();
	    checkbox_values = {};
	    show_tasks(vf_dbID, '1', 'show_tasks');
	    //if user change view_folder we need to reset checkbox_values to null because of remove_action
	    // enable_disable_start_massive_action_button()
    }