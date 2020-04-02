function create_task_in_folder(){
    console.log(action_data)
    // let send_data = action_data;
    // send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'create_task_in_folder',
        data: action_data,
        dataType: 'json',
        success: function(data){
            // var pathname = window.location.pathname; // Returns path only
            //
            //
            // if (pathname !== '/edit_source_catalog/main_page' && pathname !== '/edit_source_catalog/main_page_system'){
            //     if (action_data['view_folder']!=='') {
           show_tasks(action_data['view_folder'], 1, 'show_tasks')
            //     }
            // }
        },
        error : function(error) {console.log(error)}
    });

}