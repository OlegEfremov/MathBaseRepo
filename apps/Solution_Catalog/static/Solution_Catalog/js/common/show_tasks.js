function get_per_page(){
    var e = document.getElementById('select_tasks_per_page');
    return e.options[e.selectedIndex].innerHTML;
}


function show_tasks(dbID, page, url){
    action_data['page'] = page;
    show_tasks_url = url;
    document.getElementById('table_of_tasks').innerHTML = 'Задачи загружаются...<br><img src="../../static/images/loader.gif">';
    // document.getElementById("checkbox_all").checked = false;
    let send_data = {
        'solution_folder_dbID' : dbID
    };
    send_data = JSON.stringify(send_data);

    $.ajax({
        url: url,
        type: "POST",
        data: {'data': send_data, 'page': page, 'per_page': get_per_page()},
        success: function(res) {
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            res = compile_img_in_show_tasks(res);
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
            set_order_numbers();
            order_numbers = {};
            init_checkbox_values();
            checkbox_all_init_vars(); //initialize vars for checkbox_all (file checkbox_all_init_vars)
            set_sols_checkbox();
            set_task_checkbox_by_sols();

            set_access_checkbox();
            // document.getElementById('checkbox_counter').innerHTML = count_checkboxes();
            // reorder_tasks(action_data['view_folder'], action_data['page'], 'show_tasks')

            reset_square_values()
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}
